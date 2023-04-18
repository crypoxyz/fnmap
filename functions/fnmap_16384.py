from PIL import Image
import requests
import os

tiles_folder = "tiles/16384"
lines_folder = "lines/16384"


class fnmap_16384:
    def download_tiles(patch):
        x = 0
        y = 0
        count = 1
        while True:
            url = f"https://fortnite.gg/maps/{patch}/6/{x}/{y}.jpg"

            if x == 64:
                break

            img_data = requests.get(url).content
            with open(f"tiles/16384/tile_{x}_{y}.jpg", "wb") as handler:
                handler.write(img_data)
            print(f"{count}/4096")
            y += 1
            count += 1

            if y == 64:
                y = 0
                x += 1

    def merge_lines():
        for y in range(64):
            output_image = Image.new("RGB", (16384, 256))

            for x in range(64):
                input_path = os.path.join(tiles_folder, f"tile_{x}_{y}.jpg")
                input_image = Image.open(input_path)

                output_image.paste(input_image, (x * 256, 0))

            output_image.save(f"lines/16384/line_{y}.jpg")

    def merge_image():
        output_image = Image.new("RGB", (16384, 16384))

        for i in range(64):
            input_path = os.path.join(lines_folder, f"line_{i}.jpg")
            input_image = Image.open(input_path)

            output_image.paste(input_image, (0, i * 256))

        output_image.save(f"fnmap_16384.jpg")
