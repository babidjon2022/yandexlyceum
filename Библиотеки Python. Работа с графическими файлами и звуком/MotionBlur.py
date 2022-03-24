from PIL import Image, ImageFilter


def motion_blur(n):
    Image.open('image.jpg').transpose(Image.ROTATE_270).filter(
        ImageFilter.GaussianBlur(radius=n)).save('res.jpg')


if __name__ == '__main__':
    motion_blur(10)
