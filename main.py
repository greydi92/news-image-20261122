#!/usr/bin/env python3
"""Entry point: copy the rendered front page to the output directory.

The image is drawn at build time by gen_image.py (Pillow + DejaVu fonts,
every pixel drawn in code) and shipped as entry.png. This program does no
network and no drawing: it just copies the file, so two runs always write
byte-identical output.
"""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out / "entry.png")


if __name__ == "__main__":
    main()
