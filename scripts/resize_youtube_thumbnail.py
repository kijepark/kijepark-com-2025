#!/usr/bin/env python3
"""
Resize YouTube thumbnail to 1000:563 aspect ratio
"""
from PIL import Image
import os

# Paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_dir = os.path.join(base_dir, 'assets/img/kije')

# Target dimensions (1000:563 ratio)
TARGET_WIDTH_LARGE = 1000
TARGET_HEIGHT_LARGE = 563
TARGET_WIDTH_SMALL = 500
TARGET_HEIGHT_SMALL = 281  # 500 * 563 / 1000 ≈ 281

def resize_and_crop(input_path, output_path, target_width, target_height):
    """Resize image to exact dimensions, cropping if necessary"""
    img = Image.open(input_path)

    # Calculate aspect ratios
    target_ratio = target_width / target_height
    img_ratio = img.width / img.height

    if img_ratio > target_ratio:
        # Image is wider - crop width
        new_height = img.height
        new_width = int(new_height * target_ratio)
        left = (img.width - new_width) // 2
        img_cropped = img.crop((left, 0, left + new_width, new_height))
    else:
        # Image is taller - crop height
        new_width = img.width
        new_height = int(new_width / target_ratio)
        top = (img.height - new_height) // 2
        img_cropped = img.crop((0, top, new_width, top + new_height))

    # Resize to target dimensions
    img_resized = img_cropped.resize((target_width, target_height), Image.Resampling.LANCZOS)

    # Save
    if output_path.endswith('.webp'):
        img_resized.save(output_path, 'WEBP', quality=85, method=6)
    elif output_path.endswith('.avif'):
        img_resized.save(output_path, 'AVIF', quality=80)
    else:
        img_resized.save(output_path)

    print(f"Created: {output_path} ({target_width}x{target_height})")

# Process images
print("Resizing YouTube thumbnails to 1000:563 ratio...")

# Large version (1000x563)
resize_and_crop(
    os.path.join(img_dir, 'temp.png'),
    os.path.join(img_dir, 'kijeyoutube1000.webp'),
    TARGET_WIDTH_LARGE,
    TARGET_HEIGHT_LARGE
)

resize_and_crop(
    os.path.join(img_dir, 'temp.png'),
    os.path.join(img_dir, 'kijeyoutube1000.avif'),
    TARGET_WIDTH_LARGE,
    TARGET_HEIGHT_LARGE
)

# Small version (500x281)
resize_and_crop(
    os.path.join(img_dir, 'temp.png'),
    os.path.join(img_dir, 'kijeyoutube500_new.webp'),
    TARGET_WIDTH_SMALL,
    TARGET_HEIGHT_SMALL
)

resize_and_crop(
    os.path.join(img_dir, 'temp.png'),
    os.path.join(img_dir, 'kijeyoutube500_new.avif'),
    TARGET_WIDTH_SMALL,
    TARGET_HEIGHT_SMALL
)

print("Done!")
