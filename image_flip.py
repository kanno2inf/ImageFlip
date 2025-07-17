import os
from argparse import ArgumentParser
from multiprocessing import Pool

from PIL import Image, ImageOps


def flip_image(image_path):
    with Image.open(image_path) as img:
        print(f"{os.path.basename(image_path)}", flush=True)
        ImageOps.mirror(img).save(image_path)


def main():
    parser = ArgumentParser(description="Flip an image horizontally.")
    parser.add_argument("path", type=str, nargs="+", help="Image file path to flip.")
    opt = parser.parse_args()
    path_list = opt.path

    with Pool() as pool:
        pool.map(flip_image, path_list)


if __name__ == "__main__":
    main()
