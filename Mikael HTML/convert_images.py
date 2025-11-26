import os
from PIL import Image

files_to_convert = [
    "assets/img/22.png",
    "assets/img/IMG_0770-EDIT.jpg",
    "assets/img/Heo-Tae-yoon.jpeg",
    "assets/img/Jang-Jun-woo.jpeg",
    "assets/img/Jeong-Min-ji.jpg",
    "assets/img/Kim-Joong-won.jpeg",
    "assets/img/leedongchang.jpeg",
    "assets/img/Park-Seon-woo.jpeg",
    "images/sum/UXER.png",
    "images/sum/ads_project.png",
    "images/sum/doubleup.png",
    "images/sum/realdeveloper.png",
    "images/sum/retargetinginstore.png",
    "images/sum/scrollads.png",
    "images/sum/supersocialproof.png",
]

for file_path in files_to_convert:
    try:
        if os.path.exists(file_path):
            img = Image.open(file_path)
            new_path = os.path.splitext(file_path)[0] + ".webp"
            img.save(new_path, "WEBP", quality=80)
            print(f"Converted {file_path} to {new_path}")
        else:
            print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Failed to convert {file_path}: {e}")
