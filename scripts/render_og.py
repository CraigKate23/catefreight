#!/usr/bin/env python3
"""Render the SVG OG card to public/og-default.png so the static site can ship it."""
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "public" / "og-default.svg"
OUT = ROOT / "public" / "og-default.png"

if not SRC.exists():
    raise SystemExit(f"missing {SRC}")

cairosvg.svg2png(
    bytestring=SRC.read_bytes(),
    write_to=str(OUT),
    output_width=1200,
    output_height=630,
)
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
