# build.ps1 -- compile AP Chemistry materials
#
# Four variants from every source file (PLAN.md 8):
#   student-print   student-lms   key-print   key-lms
#
# Usage:
#   .\build.ps1 unit01-atomic-structure\u01-notes.tex     # one file, 4 variants
#   .\build.ps1 unit01-atomic-structure                   # every .tex in a unit
#   .\build.ps1 -All                                      # everything
#   .\build.ps1 <target> -Variant key-print               # single variant
#   .\build.ps1 -Clean                                    # drop aux files

param(
    [Parameter(Position = 0)] [string]$Target,
    [ValidateSet('student-print', 'student-lms', 'key-print', 'key-lms', 'all')]
    [string]$Variant = 'all',
    [switch]$All,
    [switch]$Clean
)

$ErrorActionPreference = 'Stop'
$Root  = $PSScriptRoot
$Build = Join-Path $Root 'build'
$Aux   = Join-Path $Build 'aux'

$Variants = @{
    'student-print' = ''
    'student-lms'   = '\def\ISLMS{1}'
    'key-print'     = '\def\ISKEY{1}'
    'key-lms'       = '\def\ISKEY{1}\def\ISLMS{1}'
}

if ($Clean) {
    if (Test-Path $Aux) { Remove-Item -Recurse -Force $Aux }
    Write-Host 'aux cleaned.'
    return
}

function Invoke-Compile {
    param([System.IO.FileInfo]$Source, [string]$VariantName)

    $stem    = $Source.BaseName
    $jobname = "$stem-$VariantName"
    $outDir  = Join-Path $Build ($Source.Directory.FullName.Substring($Root.Length).TrimStart('\'))
    New-Item -ItemType Directory -Force $outDir, $Aux | Out-Null

    $preamble = $Variants[$VariantName]
    # TEXINPUTS makes shared\ visible from any source directory
    $env:TEXINPUTS = ".;$(Join-Path $Root 'shared');"

    Push-Location $Source.Directory
    try {
        $tex = "$preamble\input{$($Source.Name)}"
        # two passes: tcolorbox/needspace layout stabilises on the second
        foreach ($pass in 1, 2) {
            # quotes force variable expansion: unquoted -x=$var passes "$var" literally
            $log = & pdflatex -interaction=nonstopmode -halt-on-error `
                     "-jobname=$jobname" "-output-directory=$Aux" $tex 2>&1
            if ($LASTEXITCODE -ne 0) {
                $log | Select-Object -Last 25 | Write-Host
                throw "FAILED: $($Source.Name) [$VariantName] pass $pass"
            }
        }
        $outPdf = Join-Path $outDir "$jobname.pdf"
        # A PDF viewer holding the output locks it; report and keep going
        # rather than aborting the whole run over one open file.
        try {
            Move-Item -Force (Join-Path $Aux "$jobname.pdf") $outPdf -ErrorAction Stop
        }
        catch {
            Write-Host ("  LOCKED  {0,-38} -- close the viewer and rebuild" -f "$stem [$VariantName]") -ForegroundColor Yellow
            $script:Locked++
            return
        }
        Write-Host ("  OK  {0,-42} -> {1}" -f "$stem [$VariantName]", $outPdf.Substring($Root.Length + 1))
    }
    finally { Pop-Location }
}

# resolve target list
$sources = @()
if ($All) {
    $sources = Get-ChildItem $Root -Recurse -Filter '*.tex' |
        Where-Object { $_.FullName -notmatch '\\(build|shared|Textbook|tools)\\' }
}
elseif ($Target) {
    $path = Join-Path $Root $Target
    if (Test-Path $path -PathType Container) {
        $sources = Get-ChildItem $path -Recurse -Filter '*.tex'
    }
    elseif (Test-Path $path) { $sources = @(Get-Item $path) }
    else { throw "target not found: $Target" }
}
else {
    Write-Host 'usage: .\build.ps1 <file.tex | unit-folder> [-Variant v] | -All | -Clean'
    return
}

$want = if ($Variant -eq 'all') { $Variants.Keys } else { @($Variant) }
$Locked = 0
$sw = [System.Diagnostics.Stopwatch]::StartNew()
foreach ($src in $sources) {
    foreach ($v in $want) { Invoke-Compile -Source $src -VariantName $v }
}
Write-Host ("done: {0} file(s) x {1} variant(s) in {2:n1}s" -f $sources.Count, $want.Count, $sw.Elapsed.TotalSeconds)
if ($Locked -gt 0) {
    Write-Host ("WARNING: {0} output(s) were locked and NOT updated." -f $Locked) -ForegroundColor Yellow
}
