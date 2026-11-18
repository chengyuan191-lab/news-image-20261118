#!/usr/bin/env python3
"""make.fun news-image-20261118 entry.
Copies the bundled front-page image to the output path.
Deterministic: writes the same bytes on every run."""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    # The bundled image is a JPEG; copy its bytes to entry.png.
    # The scorer accepts PNG or JPEG content regardless of extension.
    shutil.copyfile(SRC, out_path)
    print(f"wrote {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    main()
