import subprocess
import re
import os


def get_image_dimensions(file_path):
    try:
        # Run sips to get width and height
        result = subprocess.run(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", file_path],
            capture_output=True,
            text=True,
        )
        output = result.stdout

        width_match = re.search(r"pixelWidth: (\d+)", output)
        height_match = re.search(r"pixelHeight: (\d+)", output)

        if width_match and height_match:
            return width_match.group(1), height_match.group(1)
    except Exception as e:
        print(f"Error getting dimensions for {file_path}: {e}")
    return None, None


def update_html_with_dimensions(html_file):
    with open(html_file, "r") as f:
        content = f.read()

    # Find all img tags
    # This regex is simple and might need adjustment for complex tags
    # It looks for src="..." inside <img ...>

    def replace_match(match):
        full_tag = match.group(0)
        if "width=" in full_tag or "height=" in full_tag:
            return full_tag  # Already has dimensions

        src_match = re.search(r'src="([^"]+)"', full_tag)
        if not src_match:
            return full_tag

        src_path = src_match.group(1)
        # Handle relative paths if needed, assuming src is relative to html file
        local_path = src_path

        if not os.path.exists(local_path):
            # Try removing query strings or anchors if any
            local_path = local_path.split("?")[0].split("#")[0]

        if os.path.exists(local_path):
            width, height = get_image_dimensions(local_path)
            if width and height:
                # Insert width and height before src
                # return full_tag.replace('<img ', f'<img width="{width}" height="{height}" ')
                # Better: append to the end before closing >
                return full_tag.replace(
                    "<img", f'<img width="{width}" height="{height}"'
                )

        return full_tag

    # Regex to match <img ... > tags.
    # Non-greedy match until >
    new_content = re.sub(r"<img[^>]+>", replace_match, content)

    with open(html_file, "w") as f:
        f.write(new_content)
    print(f"Updated {html_file}")


update_html_with_dimensions("index.html")
