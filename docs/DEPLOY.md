# Deploying the lessons site

`apchem.rionature.com` is the HTML edition of the course, generated from the
LaTeX sources into `Lessons/` and served by SiteGround.

## How it flows

1. Work on a branch (`topic/<name>`), never on `main` directly.
2. Edit `.tex` sources, then build and regenerate locally:

   ```powershell
   .\build.ps1 <path\to\file.tex>     # 4 PDF variants, read the output
   python tools\tex2html.py           # whole site, figures included
   ```

   Always regenerate the **whole** site, never a single file: the index
   page is rebuilt from whatever that run converted, so a one-file run would
   publish an index listing one page.
3. Commit the sources **and** `Lessons/` + `Lessons-md/`, push the branch,
   open a pull request into `main`.
4. GitHub Actions (`.github/workflows/deploy.yml`) runs two required checks:
   - **Source and site checks** — `tools/ci_check.py`: the silent-failure
     patterns from CLAUDE.md in every `.tex`, then a regeneration of the
     site compared against the committed pages (stale `Lessons/` fails).
   - **LaTeX build (changed files)** — `tools/ci_build.sh`: every changed
     source compiled in all four variants on TeX Live; a key shorter than
     its student build fails. A change under `shared/` also builds
     `tools/smoke/`.
5. Merge the PR. The push to `main` reruns both checks and, if they pass,
   the **Deploy to SiteGround** job uploads the committed `Lessons/`,
   verifies three files by checksum over SSH, and flushes the cache.

`main` is protected by the **Protect main** ruleset: changes go through a
pull request, both checks must pass, and force-pushes and deletion are
blocked. There is no bypass, for anyone.

## Why the site is not built in CI

`tools/tex2html.py` renders TikZ figures with `pdflatex` and `mgs`
(MiKTeX's Ghostscript), which only the build machine has. CI regenerates
with `--no-figures` purely to compare, ignoring figure markup; what ships is
the committed `Lessons/`.

## GitHub secrets

All five live in the **production** environment (Settings → Environments),
whose deployment-branch policy allows `main` only — a pull request, even
from a fork, can never read them.

| Secret | Value |
|---|---|
| `SG_HOST` | SSH hostname from Site Tools → Devs → SSH Keys Manager → SSH Credentials |
| `SG_USER` | SSH username from the same panel |
| `SG_PATH` | `/home/<user>/www/apchem.rionature.com/public_html` |
| `SG_SSH_KEY` | the **deploy key** private half (below) |
| `SG_KNOWN_HOSTS` | the server's host-key line(s), pinned: `ssh-keyscan -p 18765 <host>`, checked against a connection you already trust |

### The deploy key

CI uses its own key, separate from the personal one in
`tools/deploy.config.ps1`, so it can be revoked without touching local
deploys. Its public half is in the server's `~/.ssh/authorized_keys` with
the comment `github-actions-apchem-deploy`.

To rotate it: generate a new RSA key (SiteGround's importer rejects
ed25519), replace that line in `authorized_keys`, update `SG_SSH_KEY`, and
delete the old private key.

## When a deploy fails

- **Missing secrets** — the "Check the deploy settings" step names which.
- **Host key mismatch** — SiteGround moved the server. Re-read the key over a
  connection you trust and update `SG_KNOWN_HOSTS`; do not just disable the
  check.
- **"does not hold the AP Chemistry site"** — `SG_PATH` is wrong. The guard
  refuses to unpack into any folder whose `index.html` is not this site.
- **Emergency**: the manual path still works from the build machine:
  `.\tools\deploy_site.ps1`.
