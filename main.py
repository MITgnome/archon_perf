import time
import numpy as np


def main():
    ts_start = time.time()
    image_cube = np.zeros([2000, 1000, 50], dtype=np.uint16)
    ts_elapsed = time.time() - ts_start
    print(ts_elapsed)
    for x in range(0, 1000):
        AnImageCube = get_images()

    ts_start = time.time()
    image_cube = np.zeros([2000, 1000, 50], dtype=np.uint16)
    for x in range(0, 1000):
        AnImageCube = get_images2(image_cube)
    ts_elapsed = time.time() - ts_start
    print(ts_elapsed)

    input("Hit Keyboard to Quit")


def get_images():
    image_cube = np.zeros([2000, 1000, 50], dtype=np.uint16)
    image_cube = image_cube + 1
    return image_cube


def get_images2(image_cube):
    image_cube = image_cube + 1
    return image_cube


if __name__ == '__main__':
    main()
