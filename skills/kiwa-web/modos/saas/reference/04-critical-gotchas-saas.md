# SaaS-specific gotchas (Tier S)

Se añaden a `diseno/reference/04-critical-gotchas.md` (la base común).

## TIER S — SaaS-specific, each cost a real production session

These are not shared web gotchas — they are the ones this skill's builds hit.
Every one was diagnosed live; treat them as settled, not as suggestions.

### S.1 ❌🔴 A database inside `public_html` is wiped on every deploy
`hosting_deployStaticWebsite` replaces the whole web folder. `usuarios.json` in
`datos/` → every account and credit balance erased on the next publish. Store it
**one level above `public_html`** via `ruta_db()` (`15` §2). **Verify: create the
test account, redeploy, log in again.** This is the single worst bug in the skill.

### S.2 ❌ Gemini's retired models + invalid JSON
`gemini-2.5-flash*` → HTTP 404 for new keys. And Gemini's structured JSON
intermittently closes an array with a duplicated `]` (`… ] ] }`, `finishReason:
STOP`) → strict `json_decode` fails. Fixes: use `gemini-3.5-flash → 3.6-flash →
flash-latest`; **default to Claude Haiku** (doesn't do this); parse tolerantly
(first `{` to last `}`). Never send `thinkingConfig` — *-lite models HTTP 400.
(`05` §2/§3b.)

### S.3 ❌ pdf.js 6 render hangs / freezes in a background tab
`page.render({canvasContext})` hangs forever in v6 — pass `{canvas, viewport,
intent:'print'}`. `intent:'print'` is also the only mode that keeps going when
the tab is hidden (`display`/`OffscreenCanvas` wait on `requestAnimationFrame`,
which a background tab never fires). (`14` / `06`.)

### S.4 ❌ The AI is bad at coordinates — position locally
Claude returns badly misplaced bounding boxes; on a redaction tool that leaves
personal data visible. Never ask any engine for coordinates in `censurar-pdf`.
The browser owns *where* (pdf.js text layer / Tesseract OCR); the AI only says
*which* text is personal data (`06`).

### S.5 ❌ Tesseract.js self-hosted hangs silently
`corePath` pointing at the FOLDER → the worker hangs at "loading tesseract core"
with no error. Point it at the exact file `tesseract-core-simd.wasm.js`, set
`workerBlobURL:false`, use absolute paths, and ship the `.wasm` binary next to
its `.wasm.js` glue (easy to forget). (`14` §3b.)

### S.6 ❌ `alert()` in a background tab reads as a crash
A blocking `alert()`/`confirm()` freezes the tab and looks like the app died —
especially mid-job. Use a small in-page toast/notice; keep `confirm()` only for
destructive, user-triggered actions (cancel plan, delete history).

### S.7 ❌ Keys pasted in chat / setup gated on `AIza`
Google now also issues `AQ.…` keys, and Anthropic keys are `sk-ant-…` — don't
gate `setup.php` on `AIza`; detect the provider and validate against it. And if
a key lands in chat, it's compromised: save it, tell them to rotate it (`05` §10).

---
