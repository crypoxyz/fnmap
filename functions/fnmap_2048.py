from PIL import Image
import requests
import os

tiles_folder = "tiles/2048"
lines_folder = "lines/2048"


class fnmap_2048:
    def download_tiles(patch):
        x = 0
        y = 0
        count = 1
        while True:
            url = f"https://fortnite.gg/maps/{patch}/3/{x}/{y}.jpg"

            if x == 8:
                break

            img_data = requests.get(url).content
            with open(f"tiles/2048/tile_{x}_{y}.jpg", "wb") as handler:
                handler.write(img_data)
            print(f"{count}/128")
            y += 1
            count += 1

            if y == 8:
                y = 0
                x += 1

    def merge_lines():
        for y in range(8):
            output_image = Image.new("RGB", (2048, 256))

            for x in range(8):
                input_path = os.path.join(tiles_folder, f"tile_{x}_{y}.jpg")
                input_image = Image.open(input_path)

                output_image.paste(input_image, (x * 256, 0))

            output_image.save(f"lines/2048/line_{y}.jpg")

    def merge_image():
        output_image = Image.new("RGB", (2048, 2048))

        for i in range(8):
            input_path = os.path.join(lines_folder, f"line_{i}.jpg")
            input_image = Image.open(input_path)

            output_image.paste(input_image, (0, i * 256))

        output_image.save(f"maps/fnmap_2048.jpg")
