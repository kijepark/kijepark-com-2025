import os
import subprocess


def get_file_type(filepath):
    try:
        result = subprocess.run(["file", filepath], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error checking file {filepath}: {e}")
        return ""


def fix_image(filepath):
    file_type = get_file_type(filepath)
    if "Web/P image" in file_type:
        print(f"Fixing mismatch: {filepath}")
        temp_path = filepath + ".webp"
        try:
            os.rename(filepath, temp_path)

            # Determine output format based on extension
            if filepath.lower().endswith(".png"):
                subprocess.run(["ffmpeg", "-y", "-i", temp_path, filepath], check=True)
            elif filepath.lower().endswith(".jpg") or filepath.lower().endswith(
                ".jpeg"
            ):
                subprocess.run(
                    ["ffmpeg", "-y", "-i", temp_path, "-q:v", "2", filepath], check=True
                )

            os.remove(temp_path)
            print(f"Fixed: {filepath}")
        except Exception as e:
            print(f"Failed to fix {filepath}: {e}")
            if os.path.exists(temp_path):
                os.rename(temp_path, filepath)  # Restore original file
                print(f"Restored original (broken) file: {filepath}")


def scan_and_fix(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                filepath = os.path.join(root, file)
                fix_image(filepath)


if __name__ == "__main__":
    scan_and_fix("Mikael HTML")
