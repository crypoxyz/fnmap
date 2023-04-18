from functions import *

patch = "24.10"


def get_task():
    print(
        """which image size do you want? (more pixels = more quality)

        #1 - 16384 x 16384 px
        #2 - 8192 x 8192 px
        #3 - 4096 x 4096 px
        #4 - 2048 x 2048 px
        #5 - 1024 x 1024 px
        #6 - 512 x 512 px
        #7 - 256 x 256 px
        """
    )
    size = input("""enter number: #""")
    task = input(
        """do you want to (d)ownload the tiles or (m)erge already existing tiles to a full map?\n\nenter task (d/m):"""
    )

    return [size, task]


value = get_task()
size = value[0]
task = value[1]

if task == "d":
    if size == "1":
        fnmap_16384.fnmap_16384.download_tiles(patch)
    elif size == "2":
        fnmap_8192.fnmap_8192.download_tiles(patch)
    elif size == "3":
        fnmap_4096.fnmap_4096.download_tiles(patch)
    elif size == "4":
        fnmap_2048.fnmap_2048.download_tiles(patch)
    elif size == "5":
        fnmap_1024.fnmap_1024.download_tiles(patch)
    elif size == "6":
        fnmap_512.fnmap_512.download_tiles(patch)
    elif size == "7":
        fnmap_256.fnmap_256.download_tiles(patch)
    else:
        exit

elif task == "m":
    if size == "1":
        fnmap_16384.fnmap_16384.merge_lines()
        fnmap_16384.fnmap_16384.merge_image()
    elif size == "2":
        fnmap_8192.fnmap_8192.merge_lines()
        fnmap_8192.fnmap_8192.merge_image()
    elif size == "3":
        fnmap_4096.fnmap_4096.merge_lines()
        fnmap_4096.fnmap_4096.merge_image()
    elif size == "4":
        fnmap_2048.fnmap_2048.merge_lines()
        fnmap_2048.fnmap_2048.merge_image()
    elif size == "5":
        fnmap_1024.fnmap_1024.merge_lines()
        fnmap_1024.fnmap_1024.merge_image()
    elif size == "6":
        fnmap_512.fnmap_512.merge_lines()
        fnmap_512.fnmap_512.merge_image()
    elif size == "7":
        fnmap_256.fnmap_256.merge_lines()
        fnmap_256.fnmap_256.merge_image()
    else:
        exit
else:
    exit
