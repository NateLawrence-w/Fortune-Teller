#!/usr/bin/env python3
"""Extract embedded PNG from a Piskel .piskel file into a usable PNG

Place this script in the project root and run it with the project's venv Python.
It will look for a .piskel file in `fortunes/static/` and write
`fortunes/static/fortunes/magic-ball.png`.
"""
import json
import base64
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    piskel_dir = root / "fortunes" / "static"
    piskel_files = list(piskel_dir.glob("*.piskel"))
    if not piskel_files:
        print("No .piskel files found in:", piskel_dir)
        return 1
    src = piskel_files[0]
    print("Using .piskel file:", src)

    try:
        data = json.loads(src.read_text(encoding="utf-8"))
    except Exception as exc:
        print("Failed to parse .piskel JSON:", exc)
        return 1

    piskel = data.get("piskel") or {}
    layers = piskel.get("layers") or []
    if not layers:
        print("No layers found inside .piskel")
        return 1

    layer0 = layers[0]
    if isinstance(layer0, str):
        try:
            layer0 = json.loads(layer0)
        except Exception as exc:
            print("Failed to parse layer JSON:", exc)
            return 1

    chunks = layer0.get("chunks") or []
    if not chunks:
        print("No chunks found in layer")
        return 1

    b64str = chunks[0].get("base64PNG")
    if not b64str:
        print("No base64PNG entry found in chunk")
        return 1

    # base64 data may be a data URI: data:image/png;base64,AAAA...
    if "," in b64str:
        _, b64data = b64str.split(",", 1)
    else:
        b64data = b64str

    try:
        img = base64.b64decode(b64data)
    except Exception as exc:
        print("Failed to decode base64 PNG:", exc)
        return 1

    dest_dir = root / "fortunes" / "static" / "fortunes"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_file = dest_dir / "magic-ball.png"
    dest_file.write_bytes(img)
    print("Wrote PNG to:", dest_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
