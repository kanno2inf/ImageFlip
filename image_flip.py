from argparse import ArgumentParser

from PIL import Image, ImageOps


def main():
    parser = ArgumentParser(description="Flip an image horizontally.")
    parser.add_argument("path", type=str, nargs="+", help="Image file path to flip.")
    opt = parser.parse_args()
    path_list = opt.path

    for image_path in path_list:
        with Image.open(image_path) as img:
            ImageOps.mirror(img).save(image_path)


if __name__ == "__main__":
    main()
