[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/greydi92/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/greydi92/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# The World in One Picture — Sunday 22 November 2026

One image that sums up the world's news of **Sunday 22 November 2026**:
six stories that happened or were first reported that day, drawn as a
front page — Gulf strikes overnight, a climate deal at dawn in Antalya,
a ship burning in the Baltic, a century in Wellington, and two briefs
from Washington.

Bounty: https://make.fun/bounty/news-image-20261122

## The day's stories

1. **Iran hits US bases in Bahrain** (lead) — Iran's Revolutionary Guard
   says its missiles and drones struck US Patriot radars at two bases
   overnight; Bahrain sounded air-raid sirens as a factory burned, and
   tankers were hit in the Strait of Hormuz. Sources: ANI, euronews,
   Reuters, WSJ.
2. **COP31 close to a deal at last** — after two days in overtime, a new
   package goes to nearly 200 nations on Sunday morning in Antalya.
   Source: Reuters.
3. **Russian ship still ablaze** — the sanctioned cargo ship Sparta II,
   hit by drones on Saturday, burns on in Finnish waters; Helsinki warns
   the war is "spilling over". Sources: Reuters, CNN.
4. **Pant ton puts India on top** — Rishabh Pant's century lifts India to
   629-6 at lunch on day four in Wellington, their highest Test total in
   New Zealand. Source: Reuters.
5. **Trump: Iran deal could last 20 years** — the US president wants a
   permanent accord to stop Iran getting a nuclear weapon. Source: Fox
   News / OpenSourceTrades.
6. **FBI probes hack of its crime database** — agents investigate an
   apparent breach of the bureau's criminal records system. Source: BBC.

## How it works

- `gen_image.py` (build-time renderer, Pillow + DejaVu fonts) draws
  `entry.png` (1024×1024 PNG, ≤1 MiB). Every pixel is drawn by this
  code — no photos, no downloaded images, no borrowed logos. The layout
  asserts that no headline or standfirst overflows its panel.
- `main.py` (Python 3.13, stdlib only, no network) copies the shipped
  `entry.png` to `MAKEFUN_OUTPUT_DIR` (or `/output`), so two runs write
  byte-identical output.

## Run it

```sh
python3 gen_image.py            # re-render entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

Built for the make.fun bounty — referral code `qgn48q27`.
