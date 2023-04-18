from PIL import Image
import requests
import os

tiles_folder = "tiles/8192"
lines_folder = "lines/8192"


class fnmap_8192:
    def download_tiles(patch):
        x = 0
        y = 0
        count = 1
        while True:
            url = f"https://fortnite.gg/maps/{patch}/5/{x}/{y}.jpg"

            if x == 32:
                break

            img_data = requests.get(url).content
            with open(f"tiles/8192/tile_{x}_{y}.jpg", "wb") as handler:
                handler.write(img_data)
            print(f"{count}/1024")
            y += 1
            count += 1

            if y == 32:
                y = 0
                x += 1

    def merge_lines():
        for y in range(32):
            output_image = Image.new("RGB", (8192, 256))

            for x in range(32):
                input_path = os.path.join(tiles_folder, f"tile_{x}_{y}.jpg")
                input_image = Image.open(input_path)

                output_image.paste(input_image, (x * 256, 0))

            output_image.save(f"lines/8192/line_{y}.jpg")

    def merge_image():
        output_image = Image.new("RGB", (8192, 8192))

        for i in range(32):
            input_path = os.path.join(lines_folder, f"line_{i}.jpg")
            input_image = Image.open(input_path)

            output_image.paste(input_image, (0, i * 256))

        output_image.save(f"maps/fnmap_8192.jpg")
