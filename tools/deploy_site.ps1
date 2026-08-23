# deploy_site.ps1 -- publish Lessons\ to the apchem subdomain over SSH
#
# Ships the CONTENTS of Lessons\ into the remote document root, so that
# index.html lands at the root and every relative link resolves. Uses a
# tarball rather than scp -r: the remote `tar -x` unpacks in place, which
# is exactly what SiteGround's File Manager "Extract" will not do (it
# buries everything in a folder named after the archive).
#
# One-time setup:
#   1. Site Tools > Devs > SSH Keys Manager > generate or import a key.
#   2. Save the private key locally, then fill in tools\deploy.config.ps1
#      (see -Init below). That file is git-ignored -- it holds your
#      hostname, username, and key path, which do not belong in the
#      public repo.
#
# Usage:
#   .\tools\deploy_site.ps1 -Init        # write a blank config to fill in
#   .\tools\deploy_site.ps1 -DryRun      # stage + report, connect to nothing
#   .\tools\deploy_site.ps1              # stage, upload, extract
#   .\tools\deploy_site.ps1 -Test        # just check the SSH connection

param(
    [switch]$Init,
    [switch]$DryRun,
    [switch]$Test
)

$ErrorActionPreference = 'Stop'

$Root      = Split-Path $PSScriptRoot -Parent
$Source    = Join-Path $Root 'Lessons'
$ConfigPath = Join-Path $PSScriptRoot 'deploy.config.ps1'

# Files that live in Lessons\ for our benefit but must not be published.
$Exclude = @('conversion-report.txt')

# ---------------------------------------------------------------- config

if ($Init) {
    if (Test-Path $ConfigPath) {
        throw "$ConfigPath already exists -- edit it rather than overwriting."
    }
    @'
# deploy.config.ps1 -- local only, git-ignored. Values come from
# Site Tools > Devs > SSH Keys Manager > (kebab menu) > SSH Credentials.

@{
    # Hostname shown in SSH Credentials, NOT the website domain.
    SshHost   = 'REPLACE.siteground.biz'

    # SSH username shown in SSH Credentials.
    SshUser   = 'REPLACE'

    # SiteGround uses a non-standard SSH port.
    SshPort   = 18765

    # Path to the PRIVATE key you generated or imported.
    KeyPath   = 'C:\Users\CHANGEME\.ssh\siteground_apchem'

    # Absolute document root of the apchem subdomain. Subdomains get their
    # own directory OUTSIDE the main domain's public_html -- confirm the
    # real path in File Manager before the first run.
    RemoteDir = '/home/customer/www/apchem.rionature.com/public_html'
}
'@ | Set-Content -Path $ConfigPath -Encoding UTF8
    Write-Host "Wrote $ConfigPath -- fill it in, then re-run." -ForegroundColor Yellow
    return
}

if (-not (Test-Path $ConfigPath)) {
    throw "No $ConfigPath. Run: .\tools\deploy_site.ps1 -Init"
}

$cfg = & $ConfigPath
foreach ($k in 'SshHost', 'SshUser', 'SshPort', 'KeyPath', 'RemoteDir') {
    if (-not $cfg.$k) { throw "deploy.config.ps1 is missing '$k'." }
    if ("$($cfg.$k)" -match 'REPLACE|CHANGEME') {
        throw "deploy.config.ps1 still has a placeholder in '$k'."
    }
}
if (-not (Test-Path $cfg.KeyPath)) {
    throw "Private key not found: $($cfg.KeyPath)"
}

$target  = "$($cfg.SshUser)@$($cfg.SshHost)"
$sshArgs = @('-i', $cfg.KeyPath, '-p', "$($cfg.SshPort)", '-o', 'StrictHostKeyChecking=accept-new')

# scp spells the port -P, not -p. With -p it silently means "preserve
# times" and eats the port number as a source filename.
$scpArgs = @('-i', $cfg.KeyPath, '-P', "$($cfg.SshPort)", '-o', 'StrictHostKeyChecking=accept-new')

# ------------------------------------------------------------------ test

if ($Test) {
    Write-Host "Connecting to $target ..." -ForegroundColor Cyan
    & ssh @sshArgs $target "echo OK; ls -la '$($cfg.RemoteDir)'"
    if ($LASTEXITCODE -ne 0) { throw "SSH connection failed (exit $LASTEXITCODE)." }
    return
}

# ----------------------------------------------------------------- stage

if (-not (Test-Path $Source)) { throw "Missing source directory: $Source" }

$stage = Join-Path ([IO.Path]::GetTempPath()) "apchem-deploy-$PID"
if (Test-Path $stage) { Remove-Item $stage -Recurse -Force }
New-Item -ItemType Directory -Path $stage -Force | Out-Null

try {
    Copy-Item -Path (Join-Path $Source '*') -Destination $stage -Recurse -Force

    foreach ($name in $Exclude) {
        $drop = Join-Path $stage $name
        if (Test-Path $drop) { Remove-Item $drop -Force }
    }

    $files = Get-ChildItem $stage -Recurse -File
    $html  = ($files | Where-Object Extension -eq '.html').Count
    $bytes = ($files | Measure-Object Length -Sum).Sum

    if (-not (Test-Path (Join-Path $stage 'index.html'))) {
        throw "index.html is not at the staging root -- links would break."
    }

    Write-Host ("Staged {0} files ({1} HTML, {2:N0} KB)" -f $files.Count, $html, ($bytes / 1KB))

    # tar.exe ships with Windows 10+. '-C $stage .' keeps paths relative so
    # the remote extract drops files straight into RemoteDir.
    $tarball = Join-Path ([IO.Path]::GetTempPath()) "apchem-site-$PID.tar.gz"
    & tar -czf $tarball -C $stage .
    if ($LASTEXITCODE -ne 0) { throw "tar failed (exit $LASTEXITCODE)." }

    if ($DryRun) {
        Write-Host "DRY RUN -- nothing uploaded." -ForegroundColor Yellow
        Write-Host "  would upload : $tarball"
        Write-Host "  to           : ${target}:$($cfg.RemoteDir)"
        return
    }

    # ---------------------------------------------------------- upload

    Write-Host "Uploading to ${target}:$($cfg.RemoteDir) ..." -ForegroundColor Cyan
    $remoteTar = "$($cfg.RemoteDir)/.apchem-deploy.tar.gz"

    & scp @scpArgs $tarball "${target}:$remoteTar"
    if ($LASTEXITCODE -ne 0) { throw "scp failed (exit $LASTEXITCODE)." }

    # Extract in place, then remove the tarball so it is never served.
    $remoteCmd = "set -e; cd '$($cfg.RemoteDir)'; tar -xzf '$remoteTar'; rm -f '$remoteTar'; ls -1 | head -5"
    & ssh @sshArgs $target $remoteCmd
    if ($LASTEXITCODE -ne 0) { throw "Remote extract failed (exit $LASTEXITCODE)." }

    Write-Host "Deployed. Check https://apchem.rionature.com/" -ForegroundColor Green
}
finally {
    if (Test-Path $stage) { Remove-Item $stage -Recurse -Force }
    Get-ChildItem ([IO.Path]::GetTempPath()) -Filter "apchem-site-$PID.tar.gz" -ErrorAction SilentlyContinue |
        Remove-Item -Force
}
