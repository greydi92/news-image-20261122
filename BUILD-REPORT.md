# BUILD REPORT — news-image-20261122

**Bounty:** "Sum up 22 November's world news in one image" — $100, top 50 share
($20 / $12 / $6 / $2 places 4–10 / $1.20 places 11–50)
**Slug:** `news-image-20261122` · **Opens:** 2026-11-22T00:00:00Z ·
**Deadline:** Mon 2026-11-24 07:00 WIB (2026-11-24T00:00:00Z) ·
**Result due:** 2026-12-08
**Harness:** program/v1, transcript bundle (no sealed recordings).
**Built:** Sun 2026-11-22 ~08:00–08:10 WIB, in-session, fresh composition.

## The image

Front-page infographic, 1024×1024 PNG, masthead "THE WORLD IN ONE PICTURE /
SUNDAY 22 NOVEMBER 2026", lead panel + COP31 panel on row 1, Baltic /
cricket / World-in-Brief on row 2, "The day in one line" footer. Every pixel
drawn in code (Pillow + DejaVu); no photos, no downloaded images, no logos.
New layout — not yesterday's lead-plus-3-cards-plus-2-wide.

## Stories covered (each verified as happened or first reported 22 Nov 2026)

1. **Iran hits US bases in Bahrain (LEAD, Gulf)** — IRGC says its missiles
   and drones struck US Patriot radars at al-Riffa and Awali bases
   overnight; Bahrain sounded air-raid sirens, a factory burned; tankers
   hit in the Strait of Hormuz. First reported Sunday morning.
   Sources: ANI (published 22 Nov 04:11 IST), euronews, Reuters, WSJ.
2. **COP31 close to a deal at last (Antalya)** — after two days in
   overtime, a new package goes to nearly 200 nations on Sunday morning;
   approval session 06:00 GMT. Source: Reuters, updated Sun 22 Nov.
3. **Russian ship still ablaze (Baltic)** — sanctioned cargo ship Sparta II,
   hit by drones on Saturday, still burning in Finnish waters on Sunday;
   Helsinki warns the war is "spilling over". Sources: Reuters, CNN, NY Post.
4. **Pant ton puts India on top (Wellington)** — Rishabh Pant's century,
   India 629-6 at lunch on day four, their highest Test total in New
   Zealand, lead of 261. Source: Reuters, Sun 22 Nov 00:41 UTC.
5. **Trump: Iran deal could last 20 years (Washington, brief)** — wants a
   permanent accord to stop Iran getting a nuclear weapon.
   Source: Fox News / OpenSourceTrades, dated 22 Nov.
6. **FBI probes hack of its crime database (US, brief)** — agents
   investigate an apparent breach of the bureau's criminal records system.
   Source: BBC, Sun 22 Nov.

Deliberately NOT used (they are 20–21 Nov news, not the 22nd): Peru quake
(20 Nov), 'El Chapo Isidro' arrest (20 Nov, reported 21 Nov), Bolsonaro ICU
(21 Nov), Zelensky/Streeting Kyiv meeting (21 Nov), Denmark plot + Estonia
border closure (20 Nov), APEC trilateral (19 Nov), Roundup $7.25bn approval
(20 Nov). Yesterday's lead (Russian missiles in Poland) was not repeated.

## Verification (grader-style, done before this report)

- `main.py` run twice into two different dirs (`/tmp/mf-v1`, `/tmp/mf-v2`):
  both outputs byte-identical.
- SHA-256 (both runs and shipped `entry.png`):
  `f3cd253b8238f401903ea3b8d758f61a8509e4edc4866bdba16e1c0f3bff8204`
- Format: PNG, 1024×1024, 124,362 bytes (≤ 1,048,576). Valid PNG magic bytes.
- Programmatic text check: `gen_image.py` asserts every standfirst/headline
  ends inside its panel (asserts fired twice during development and were
  fixed by shortening text, not by shrinking the check).
- Visual inspection of the final render: all six stories legible, no
  truncated or overlapping text, no pictogram escaping its panel.
- `main.py` is stdlib-only, no network; deterministic by construction
  (copies the shipped PNG).
- No file in the work dir was edited after the final verification run.

## Files (work dir `~/workspace/kerjaan/makefun/news-image-20261122/`)

| File | Lines / size | Notes |
|---|---|---|
| `gen_image.py` | 375 lines | Build-time renderer, authored fresh in-session |
| `main.py` | 24 lines | Entrypoint, stdlib only, copies entry.png |
| `entry.png` | 124,362 bytes | Rendered front page (the deliverable) |
| `README.md` | 56 lines | 3 badge lines + bounty link + referral `qgn48q27` |
| `LICENSE` | MIT | Copyright greydi92 |
| `.makefun/owner.json` | 1 line | `{"wallet": "HbfEuuP4KjMr9bEsv5YhPpxeF7nULnFH442117iDrPeB"}` |

Authorship: 100% of code lines written in this session (gen_image.py was
written fresh; yesterday's file was not read or copied).

## Notes for the parent at submit time

- **Do NOT run `makefun login`** (rotates the key) and **do NOT run
  `makefun record`** — this bounty refuses recordings (HTTP 400); it takes
  a transcript bundle.
- Repo creation, push, bundle and submit are the parent's job (not done here).
- **Redact Grey's personal details in the bundle:** full name
  `Redi Ardiana`, email `greyatri@gmail.com` (pass to bundle with
  `--redact`, as per RULES.txt step 3). Bundle already redacts emails
  itself, but pass both terms explicitly.
- Deadline Mon 2026-11-24 07:00 WIB; result due 2026-12-08.
- Do not edit the work dir / repo after submission.
