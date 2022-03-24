from PIL import Image


def make_preview(size, n_colors):
    Image.open('image.jpg').resize(size).quantize(
        n_colors).save('res.bmp', format='BMP')


if __name__ == '__main__':
    make_preview((400, 200), 64)
