#!/usr/bin/env python3
"""Render the front page for Sunday 22 November 2026.

Build-time renderer only: it draws entry.png (1024x1024, PNG) with Pillow
and DejaVu fonts. Every pixel is drawn by this code -- no photos, no
downloaded images, no borrowed logos. The shipped program (main.py) just
copies the rendered entry.png to the output directory.
"""

import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SR = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


# Palette
NAVY = (16, 32, 64)
NAVY2 = (24, 48, 92)
PAPER = (247, 243, 234)
CARD = (255, 255, 255)
INK = (22, 22, 26)
MUTED = (90, 90, 96)
RED = (178, 34, 34)
GOLD = (212, 175, 55)
TEAL = (14, 122, 110)
ORANGE = (214, 106, 24)
SKY = (52, 110, 168)
RULE = (200, 192, 176)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, fill=INK, leading=1.28):
    """Draw wrapped paragraph; returns y after last line."""
    lines = wrap(draw, text, fnt, width)
    lh = int(fnt.size * leading)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def kicker(draw, x, y, text, color=RED):
    f = font(FB, 17)
    draw.text((x, y), text, font=f, fill=color)
    return y + 24


def headline(draw, x, y, text, size, width, fill=INK, fnt_path=SB):
    f = font(fnt_path, size)
    return para(draw, x, y, text, f, width, fill=fill, leading=1.12)


def panel(draw, x0, y0, x1, y1, fill=CARD):
    draw.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=fill,
                           outline=RULE, width=1)


# ---------------- pictograms (flat vector, drawn in code) ----------------

def pic_gulf(draw, x0, y0, x1, y1):
    """Night sky, radar dome, missile streaks, base silhouettes."""
    draw.rectangle([x0, y0, x1, y1], fill=(18, 30, 58))
    # stars
    for sx, sy in [(0.12, 0.18), (0.3, 0.1), (0.5, 0.22), (0.68, 0.12),
                   (0.85, 0.2), (0.22, 0.32), (0.78, 0.34)]:
        px, py = x0 + int(sx * (x1 - x0)), y0 + int(sy * (y1 - y0))
        draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(255, 255, 255))
    # moon
    draw.ellipse([x1 - 62, y0 + 14, x1 - 30, y0 + 46], fill=(240, 230, 190))
    # radar dome + mast
    cx = x0 + int(0.30 * (x1 - x0))
    base = y1 - 18
    draw.rectangle([cx - 4, base - 52, cx + 4, base], fill=(150, 160, 180))
    draw.pieslice([cx - 34, base - 92, cx + 34, base - 24], 180, 360,
                  fill=(210, 220, 235))
    draw.line([cx, base - 92, cx + 26, base - 116], fill=(255, 210, 90), width=3)
    # missile streaks
    for (mx, my, ln) in [(0.55, 0.30, 46), (0.68, 0.52, 58), (0.82, 0.28, 40)]:
        px, py = x0 + int(mx * (x1 - x0)), y0 + int(my * (y1 - y0))
        draw.line([px, py, px + ln, py + int(ln * 0.55)], fill=(255, 190, 60),
                  width=4)
        draw.ellipse([px + ln - 3, py + int(ln * 0.55) - 3,
                      px + ln + 7, py + int(ln * 0.55) + 7], fill=(255, 120, 40))
    # base buildings + flames
    draw.rectangle([x0 + 8, base - 26, x0 + 78, base], fill=(40, 52, 80))
    draw.rectangle([x1 - 96, base - 20, x1 - 8, base], fill=(40, 52, 80))
    fx = x1 - 52
    draw.polygon([(fx, base - 34), (fx - 12, base - 8), (fx + 12, base - 8)],
                 fill=(255, 140, 40))
    draw.polygon([(fx, base - 24), (fx - 7, base - 8), (fx + 7, base - 8)],
                 fill=(255, 220, 90))


def pic_cop(draw, x0, y0, x1, y1):
    """Globe with leaf and sun."""
    draw.rectangle([x0, y0, x1, y1], fill=(14, 96, 88))
    cx = x0 + int(0.38 * (x1 - x0))
    cy = y0 + int(0.52 * (y1 - y0))
    r = int(0.30 * (y1 - y0))
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(52, 152, 132))
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(230, 240, 230),
                 width=3)
    # meridians
    draw.arc([cx - r, cy - r, cx + r, cy + r], 0, 360, fill=(230, 240, 230),
             width=2)
    draw.ellipse([cx - int(r * 0.45), cy - r, cx + int(r * 0.45), cy + r],
                 outline=(230, 240, 230), width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=(230, 240, 230), width=2)
    # leaf: pointed oval
    lx, ly = x1 - 78, y0 + 26
    draw.polygon([(lx - 30, ly + 50), (lx - 26, ly + 12), (lx, ly - 4),
                  (lx + 26, ly + 12), (lx + 30, ly + 50), (lx, ly + 62)],
                 fill=(120, 200, 90))
    draw.line([lx, ly + 56, lx, ly + 6], fill=(60, 140, 60), width=3)
    # sun
    sx, sy = x0 + 34, y0 + 28
    draw.ellipse([sx - 12, sy - 12, sx + 12, sy + 12], fill=(255, 214, 90))
    for ang in range(0, 360, 45):
        import math
        a = math.radians(ang)
        draw.line([sx + int(18 * math.cos(a)), sy + int(18 * math.sin(a)),
                   sx + int(26 * math.cos(a)), sy + int(26 * math.sin(a))],
                  fill=(255, 214, 90), width=3)


def pic_ship(draw, x0, y0, x1, y1):
    """Cargo ship on fire in the Baltic."""
    draw.rectangle([x0, y0, x1, y1], fill=(186, 214, 232))
    # sky sun haze
    draw.ellipse([x1 - 66, y0 + 12, x1 - 34, y0 + 44], fill=(255, 236, 170))
    # hull
    hy = y1 - 52
    draw.polygon([(x0 + 14, hy), (x1 - 14, hy), (x1 - 34, hy + 30),
                  (x0 + 34, hy + 30)], fill=(60, 70, 88))
    draw.rectangle([x0 + 14, hy - 6, x1 - 14, hy], fill=(178, 34, 34))
    # containers
    draw.rectangle([x0 + 40, hy - 34, x0 + 96, hy - 6], fill=(214, 106, 24))
    draw.rectangle([x0 + 102, hy - 34, x0 + 158, hy - 6], fill=(52, 110, 168))
    # bridge
    draw.rectangle([x1 - 84, hy - 52, x1 - 40, hy - 6], fill=(240, 240, 235))
    draw.rectangle([x1 - 80, hy - 46, x1 - 44, hy - 34], fill=(52, 110, 168))
    # flames
    fx = x0 + int(0.52 * (x1 - x0))
    draw.polygon([(fx, hy - 78), (fx - 22, hy - 30), (fx + 22, hy - 30)],
                 fill=(255, 120, 30))
    draw.polygon([(fx, hy - 60), (fx - 12, hy - 30), (fx + 12, hy - 30)],
                 fill=(255, 210, 60))
    # smoke
    for i, (sx, sy, sr) in enumerate([(0.50, 0.22, 12), (0.56, 0.14, 15),
                                      (0.62, 0.20, 10)]):
        px, py = x0 + int(sx * (x1 - x0)), y0 + int(sy * (y1 - y0))
        draw.ellipse([px - sr, py - sr, px + sr, py + sr], fill=(120, 120, 125))
    # waves
    for wy in (y1 - 16, y1 - 8):
        for wx in range(x0 + 6, x1 - 6, 34):
            draw.arc([wx, wy - 6, wx + 22, wy + 8], 180, 360,
                     fill=(255, 255, 255), width=3)


def pic_cricket(draw, x0, y0, x1, y1):
    """Bat, red ball, stumps on green."""
    draw.rectangle([x0, y0, x1, y1], fill=(46, 125, 70))
    # pitch strip
    draw.rectangle([x0, y0 + int(0.62 * (y1 - y0)), x1, y1],
                   fill=(196, 164, 110))
    # stumps
    sx = x0 + int(0.20 * (x1 - x0))
    sy = y0 + int(0.62 * (y1 - y0))
    for i in range(3):
        draw.rectangle([sx + i * 12, sy - 44, sx + i * 12 + 7, sy],
                       fill=(240, 220, 150))
    draw.rectangle([sx - 2, sy - 50, sx + 34, sy - 44], fill=(240, 220, 150))
    # bat (leaning, broad blade) -- kept fully inside the pic box
    bx, by = x0 + int(0.58 * (x1 - x0)), y0 + int(0.70 * (y1 - y0))
    draw.polygon([(bx - 16, by - 52), (bx + 16, by - 52), (bx + 22, by + 34),
                  (bx - 24, by + 34)], fill=(232, 214, 170),
                 outline=(150, 120, 70))
    draw.rectangle([bx - 6, by - 76, bx + 6, by - 50], fill=(90, 60, 30))
    # ball
    ballx, bally = x1 - 52, y0 + 44
    draw.ellipse([ballx - 18, bally - 18, ballx + 18, bally + 18],
                 fill=(178, 34, 34))
    draw.arc([ballx - 18, bally - 18, ballx + 18, bally + 18], 300, 60,
             fill=(255, 255, 255), width=2)
    # score badge
    draw.rounded_rectangle([x0 + 14, y0 + 12, x0 + 118, y0 + 46], radius=8,
                           fill=(255, 255, 255))
    draw.text((x0 + 24, y0 + 20), "629-6", font=font(FB, 22), fill=RED)


def pic_doc(draw, x0, y0, x1, y1):
    """Document with pen -- a deal on paper."""
    draw.rectangle([x0, y0, x1, y1], fill=(240, 238, 228))
    cx = (x0 + x1) // 2
    cy = (y0 + y1) // 2
    draw.rounded_rectangle([cx - 26, y0 + 10, cx + 26, y1 - 10], radius=4,
                           fill=(255, 255, 255), outline=(150, 150, 145), width=2)
    for i, ly in enumerate((y0 + 24, y0 + 38, y0 + 52)):
        draw.line([cx - 16, ly, cx + 16, ly], fill=(120, 120, 118), width=2)
    draw.line([cx - 16, y0 + 68, cx + 2, y0 + 68], fill=(178, 34, 34), width=3)
    # pen (kept inside the icon box)
    draw.line([cx + 22, y1 - 16, cx + 32, y0 + 28], fill=(24, 48, 92), width=4)


def pic_laptop(draw, x0, y0, x1, y1):
    """Laptop with warning triangle -- a database hack."""
    draw.rectangle([x0, y0, x1, y1], fill=(232, 236, 242))
    cx = (x0 + x1) // 2
    cy = (y0 + y1) // 2
    draw.rounded_rectangle([cx - 34, y0 + 16, cx + 34, cy + 12], radius=4,
                           fill=(24, 48, 92))
    draw.rectangle([cx - 27, y0 + 23, cx + 27, cy + 5], fill=(120, 190, 220))
    draw.polygon([(cx, y0 + 30), (cx - 12, y0 + 52), (cx + 12, y0 + 52)],
                 fill=(255, 190, 40))
    draw.text((cx - 3, y0 + 40), "!", font=font(FB, 14), fill=(24, 48, 92))
    draw.rectangle([cx - 44, cy + 12, cx + 44, cy + 20], fill=(24, 48, 92))


# ---------------- page ----------------

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 112], fill=NAVY)
    d.rectangle([0, 112, W, 116], fill=GOLD)
    d.text((W // 2, 14), "THE WORLD IN ONE PICTURE",
           font=font(SB, 40), fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 66), "SUNDAY  22  NOVEMBER  2026",
           font=font(FB, 26), fill=GOLD, anchor="ma")

    # ---- row 1: lead (Gulf) + COP31 ----
    # LEAD panel
    x0, y0, x1, y1 = 22, 130, 616, 452
    panel(d, x0, y0, x1, y1)
    pic_gulf(d, x0 + 2, y0 + 2, x1 - 2, y0 + 138)
    ty = y0 + 150
    ty = kicker(d, x0 + 18, ty, "GULF CRISIS  •  LEAD STORY")
    ty = headline(d, x0 + 18, ty + 2, "Iran hits US bases in Bahrain",
                  33, x1 - x0 - 36)
    end = para(d, x0 + 18, ty + 8,
               "Iran's Revolutionary Guard says its missiles and drones "
               "struck US Patriot radars at two bases overnight. Bahrain "
               "sounded air-raid sirens as a factory burned.",
               font(FR, 18), x1 - x0 - 36)
    assert end <= y1 - 10, f"lead standfirst overflows: {end} > {y1 - 10}"

    # COP31 panel
    x0, y0, x1, y1 = 630, 130, 1002, 452
    panel(d, x0, y0, x1, y1)
    pic_cop(d, x0 + 2, y0 + 2, x1 - 2, y0 + 132)
    ty = y0 + 144
    ty = kicker(d, x0 + 18, ty, "CLIMATE  •  ANTALYA", color=TEAL)
    ty = headline(d, x0 + 18, ty + 2, "COP31 close to a deal at last",
                  28, x1 - x0 - 36)
    end = para(d, x0 + 18, ty + 8,
               "A new package goes to nearly 200 nations on Sunday "
               "morning after two days in overtime.",
               font(FR, 18), x1 - x0 - 36)
    assert end <= y1 - 10, f"COP31 standfirst overflows: {end} > {y1 - 10}"

    # ---- row 2: Baltic | Cricket | World in brief ----
    # Baltic
    x0, y0, x1, y1 = 22, 466, 344, 800
    panel(d, x0, y0, x1, y1)
    pic_ship(d, x0 + 2, y0 + 2, x1 - 2, y0 + 120)
    ty = y0 + 132
    ty = kicker(d, x0 + 16, ty, "BALTIC SEA", color=SKY)
    ty = headline(d, x0 + 16, ty + 2, "Russian ship still ablaze",
                  26, x1 - x0 - 32)
    end = para(d, x0 + 16, ty + 8,
               "The sanctioned ship Sparta II, hit by drones on Saturday, "
               "burns on in Finnish waters as Helsinki warns the war is "
               "“spilling over”.",
               font(FR, 16), x1 - x0 - 32)
    assert end <= y1 - 10, f"Baltic standfirst overflows: {end} > {y1 - 10}"

    # Cricket
    x0, y0, x1, y1 = 358, 466, 680, 800
    panel(d, x0, y0, x1, y1)
    pic_cricket(d, x0 + 2, y0 + 2, x1 - 2, y0 + 120)
    ty = y0 + 132
    ty = kicker(d, x0 + 16, ty, "CRICKET  •  WELLINGTON", color=(46, 125, 70))
    ty = headline(d, x0 + 16, ty + 2, "Pant ton puts India on top",
                  26, x1 - x0 - 32)
    end = para(d, x0 + 16, ty + 8,
               "Rishabh Pant's century lifts India to 629-6 at lunch on day "
               "four — their highest Test total in New Zealand, a lead "
               "of 261.",
               font(FR, 16), x1 - x0 - 32)
    assert end <= y1 - 10, f"cricket standfirst overflows: {end} > {y1 - 10}"

    # World in brief
    x0, y0, x1, y1 = 694, 466, 1002, 800
    panel(d, x0, y0, x1, y1)
    d.text((x0 + 16, y0 + 14), "WORLD IN BRIEF", font=font(FB, 17), fill=RED)
    d.line([x0 + 16, y0 + 42, x1 - 16, y0 + 42], fill=RULE, width=2)

    # brief 1: Trump / Iran deal
    bx, by = x0 + 16, y0 + 56
    pic_doc(d, bx, by, bx + 72, by + 92)
    tx = bx + 84
    ty2 = headline(d, tx, by, "Trump: Iran deal could last 20 years",
                   19, x1 - tx - 14)
    end = para(d, tx, ty2 + 6,
               "He wants a permanent accord to stop Iran getting a "
               "nuclear weapon.",
               font(FR, 14), x1 - tx - 14)
    assert end <= y0 + 178, f"brief 1 overflows: {end}"

    d.line([x0 + 16, y0 + 186, x1 - 16, y0 + 186], fill=RULE, width=1)

    # brief 2: FBI hack
    bx, by = x0 + 16, y0 + 196
    pic_laptop(d, bx, by, bx + 72, by + 92)
    tx = bx + 84
    ty2 = headline(d, tx, by, "FBI probes hack of its crime database",
                   19, x1 - tx - 14)
    end = para(d, tx, ty2 + 6,
               "Agents are probing an apparent breach of the bureau's "
               "crime records.",
               font(FR, 14), x1 - tx - 14)
    assert end <= y1 - 10, f"brief 2 overflows: {end}"

    # ---- footer: the day in one line ----
    fx0, fy0, fx1, fy1 = 22, 814, 1002, 1002
    d.rounded_rectangle([fx0, fy0, fx1, fy1], radius=10, fill=NAVY)
    d.text((W // 2, fy0 + 16), "THE DAY IN ONE LINE",
           font=font(FB, 17), fill=GOLD, anchor="ma")
    d.text((W // 2, fy0 + 46),
           "Gulf strikes overnight, a climate deal at dawn in Antalya, a ship",
           font=font(SR, 24), fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, fy0 + 78),
           "burning in the Baltic — and a century in Wellington.",
           font=font(SR, 24), fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, fy0 + 124),
           "All six stories happened or were first reported on Sunday 22 November 2026.",
           font=font(FR, 15), fill=(200, 205, 215), anchor="ma")
    d.text((W // 2, fy0 + 148),
           "Drawn from live reporting: Reuters • BBC • ANI • euronews • CNN",
           font=font(FR, 13), fill=(160, 165, 178), anchor="ma")

    img.save(OUT, "PNG", optimize=True)
    print("saved", OUT)


if __name__ == "__main__":
    main()
