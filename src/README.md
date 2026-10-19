# Recompiling the Slides on Overleaf

Each chapter deck (`ecp01.tex` – `ecp16.tex`) is a self-contained Beamer
presentation. All of them share the `styles/` theme and `assets/` images in
this folder, so the easiest way to compile any of them on Overleaf is to
upload this whole `src/` folder as one project.

## Option 1 — Upload the whole `src/` folder (recommended)

1. On Overleaf, create a **New Project → Upload Project**, and upload this
   entire `src/` folder as a `.zip` (or drag the folder in if your browser
   supports it).
2. In the Overleaf project, set the **main document** to whichever chapter
   you want to compile — e.g. `ecp01.tex` for Chapter 1. (Menu → Settings →
   Main document.)
3. Compiler should be **pdfLaTeX** (Overleaf's default). No XeLaTeX or
   LuaLaTeX is needed.
4. Click Recompile. The relative paths (`styles/...`, `assets/...`) already
   match this folder's layout, so nothing needs editing.

To compile a different chapter later, just change the main document setting
— all 16 `.tex` files live side by side and share the same `styles/` and
`assets/`.

## Option 2 — Upload a single chapter only

If you only want one chapter's deck:

1. Create a new Overleaf project and upload that chapter's `.tex` file
   (e.g. `ecp09.tex`) as the main document.
2. Also upload the `styles/` folder and `assets/` folder into the project,
   keeping them as subfolders named exactly `styles` and `assets` at the
   same level as the `.tex` file — the source references them as
   `styles/fluxmacros` and `assets/<filename>.png`, so the folder names and
   relative paths must match.
3. Compiler: pdfLaTeX.

## What's in this folder

- `ecp01.tex` – `ecp16.tex` — one Beamer source file per chapter
- `styles/` — the shared `flux` Beamer theme (6 `.sty` files)
- `assets/` — the UTM logo and the chapter figures referenced by the slides

## Notes

- Every deck pulls in standard packages available on Overleaf/TeX Live by
  default (`tikz`, `booktabs`, `listings`, `roboto`, `beramono`, etc.) —
  no extra package installation is needed.
- If Overleaf reports a missing package, it almost always means the project
  structure doesn't match what's described above (e.g. `styles/` or
  `assets/` not uploaded, or renamed) rather than something actually
  missing from Overleaf's TeX Live.
