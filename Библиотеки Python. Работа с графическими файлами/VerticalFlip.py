from PIL import Image
from numpy import uint8, fliplr, asarray


def mirror():
    Image.fromarray(uint8(fliplr(asarray(Image.open('image.jpg'))))).save('res.jpg')


if __name__ == '__main__':
    mirror()
