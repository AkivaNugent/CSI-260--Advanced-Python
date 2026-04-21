#!/usr/bin/env python3
"""
cbz_to_png.py — Convert all CBZ files in a directory to PNG images,
flattened into a single output folder for LoRA training.
"""

from pathlib import Path
from PIL import Image, ImageOps
import zipfile
import io

# ---- SETTINGS ----
INPUT_DIR  = r""       # folder containing your .cbz files
OUTPUT_DIR = r""       # where PNGs will be saved
SIZE       = 1024                             # output image size (square)
# ------------------


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"}


def pad_to_square(img: Image.Image, size: int) -> Image.Image:
    """Resize image to fit within size x size, then pad to exact square with black."""
    img = img.convert("RGB")
    img.thumbnail((size, size), Image.LANCZOS)
    padded = Image.new("RGB", (size, size), (0, 0, 0))
    x = (size - img.width) // 2
    y = (size - img.height) // 2
    padded.paste(img, (x, y))
    return padded


def slugify(name: str) -> str:
    """Turn a filename stem into a safe prefix."""
    return "".join(c if c.isalnum() else "_" for c in name).strip("_")


def cbz_to_pngs(cbz_path: Path, output_dir: Path, size: int) -> int:
    """Extract and save all images from a CBZ as padded PNGs. Returns page count."""
    prefix = slugify(cbz_path.stem)

    with zipfile.ZipFile(cbz_path, "r") as zf:
        image_names = sorted(
            name for name in zf.namelist()
            if Path(name).suffix.lower() in IMAGE_EXTENSIONS
        )

        if not image_names:
            print(f"  [!] No images found in {cbz_path.name}, skipping.")
            return 0

        for i, name in enumerate(image_names, start=1):
            data = zf.read(name)
            img = Image.open(io.BytesIO(data))
            img = pad_to_square(img, size)
            out_path = output_dir / f"{prefix}_page_{i:04d}.png"
            img.save(out_path, "PNG")
            print(f"  [{i}/{len(image_names)}] {out_path.name}")

        return len(image_names)


def main():
    input_dir  = Path(INPUT_DIR)
    output_dir = Path(OUTPUT_DIR)

    if not input_dir.is_dir():
        print(f"Error: '{input_dir}' is not a valid directory. Check your INPUT_DIR setting.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    cbz_files = sorted(input_dir.glob("*.cbz"))
    if not cbz_files:
        print(f"No .cbz files found in '{input_dir}'.")
        return

    print(f"Found {len(cbz_files)} CBZ file(s).")
    print(f"Output dir : {output_dir}")
    print(f"Target size: {SIZE}x{SIZE}\n")

    total = 0
    for cbz in cbz_files:
        print(f"Processing: {cbz.name}")
        try:
            count = cbz_to_pngs(cbz, output_dir, SIZE)
            total += count
        except Exception as e:
            print(f"  [ERROR] Failed to process {cbz.name}: {e}")

    print(f"\nDone! {total} images saved to '{output_dir}'")


if __name__ == "__main__":
    main()