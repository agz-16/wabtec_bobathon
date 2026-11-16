# AGENTS.md

This file provides guidance to agents when working with code in this repository.

Static lab-guide website (plain HTML/CSS/vanilla JS, no package.json, no bundler, no lint, no tests). Only `docs/` is published (GitHub Pages). Content is about an IBM i app (FLIGHT400) used with IBM Bob.

## Commands
- Preview: `python3 -m http.server` inside `docs/` (exercises load via `fetch()`, so `file://` shows nothing).
- Rebuild offline copy: `python3 build-offline.py` from repo root (stdlib only). Run it after ANY change under `docs/`, then commit `offline/` and `offline.zip`. Never hand-edit `offline/`.
- Regenerate `docs/setup.md`: `python3 build-setup-md.py` from repo root (stdlib only). Run it after ANY change to `docs/tracks/setup.html`, then commit `docs/setup.md`. Never hand-edit `setup.md`.
- Only validation available is the two build scripts; `build-offline.py` `fail()`s on missing images/track files or if the guide's structure changed (see constraints below).

## Structure gotchas
- `docs/index.html` is a shell. Exercise content lives in `docs/tracks/{setup,track-1..track-7}.html` as HTML partials (no `<html>` wrapper) injected into `#tracks-stream` by `docs/js/app.js`.
- Track slug list is duplicated: `DEFAULT_TRACK_SLUGS` in `docs/js/app.js` and `SLUGS` in `build-offline.py`. Keep both in sync. `ADDITIONAL_SLUGS` (`track-3/4/6`) are collapsed into "Additional Exercises"; grouping is per whole track file, not per step.
- Events: copy `docs/_template/` (never edit it) to `docs/<event>/`, edit only its `js/config.js`. Its `index.html` loads `config.js` BEFORE `<base href="../">`. A `<event>/tracks/<slug>.html` overrides the shared track for that slug only. `docs/setup.html` (the setup-only page) sets `window.FLIGHT400_CONFIG` inline; `docs/index.html` sets none.
- Setup content has ONE source: `docs/tracks/setup.html`. `docs/setup.md` is generated from it by `build-setup-md.py` (relies on the `.use-case`, `.mode-step`, `.step-title`, `.step-desc`, `.step-screenshot`, `.step-prompt`, `.info-box`/`.warn-box`, `#attendee-table` markup; mirror existing markup in new steps). `docs/setup.html` is just the standalone page shell. `docs/setup-export.html` and `docs/setup.pdf` are gitignored and must not be committed (stale exports; the setup guide has no PDF/export version).
- `instructor-setup/` is never served by Pages; `setup_flight400_lab.sh` runs on the IBM i (PASE), not locally. Use `--dry-run` first. `FLGHT400` is the golden master; attendees get `FLGHT401…FLGHT4nn`, port `3000+nn`.
- `*-plan.md`, `bob-file-write-paths.md`, `SAMPLE-SKILL*.md` at root are working notes/sample content, not code.

## Placeholder autofill (non-obvious, easy to break)
`app.js` rewrites tokens after the attendee picks a library row (step 0.3) and pastes their IP: `FLGHT4nn`, `FLIGHT4nn`, `flght4nn`, `flight4nn`, `4nn`, `30nn`, `nn`, `<myIPaddress>`. Write guide text with these literal tokens; never hardcode a library number or IP. The key file is always the literal `ae_primary_key.pem` (there is no server/backup picker and no `<server>` token).
- Replacement runs ONLY inside `pre`, `code`, `.step-title`, `.step-desc`, `.uc-desc`, `.info-box`, `.warn-box`, `.detail-intro`, `.data-table td`, `.step-screenshot-caption`. Tokens in `.uc-title`, `.card-desc`, or other elements are not replaced.
- Token order in `replaceTokens()` matters (most specific first). Selection is persisted in localStorage keys `flight400-{student,ip}-v1`.
- Copy buttons only work inside `.step-prompt`, `.prompt-box`, or `.code-block` containing a `<pre>`.

## Offline-build constraints (`build-offline.py` enforces these)
- Images in tracks/index must be referenced as `src="img/<file>"` or `href="img/<file>"` (relative, in `docs/img/`); they are base64-inlined.
- `docs/css/styles.css` must not use `url(...)`; `docs/js/app.js` must not contain the string `img/`.
- `docs/index.html` must keep the Google Fonts `<link>` tags, `<link rel="stylesheet" href="css/styles.css...">` and `<script src="js/app.js...">` in that exact form (regex-matched).
- In `app.js`, offline mode reads `window.FLIGHT400_INLINE_TRACKS` instead of `fetch()`.

## Style
- JS: ES5 style IIFE (`var`, `function`, no modules/arrow functions), 2-space indent, single quotes, section banners like `// ── NAME ───`. Wrap `localStorage` access in `try/catch`.
- Python: stdlib only, `fail(msg)` for fatal errors.
- HTML partials: card markup `.bubble-card > .card-summary + .card-detail`, per-track CSS vars `--c1..`; mirror an existing track file when adding exercises.
- Security rules apply (see global rules): bind dev servers to `127.0.0.1`, no secrets in repo. Private keys and server IPs are shared by the instructor out of band; never commit them or link to where they are stored (the guide deliberately has no Box link or `boxFolderUrl` option).
