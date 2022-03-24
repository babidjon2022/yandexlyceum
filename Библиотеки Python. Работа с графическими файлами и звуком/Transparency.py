from PIL import Image


def combine(tuple1, tuple2):
    tuple_res = tuple(map(lambda x: int(0.5 * tuple1[x] + 0.5 * tuple2[x]), range(3)))
    if max(tuple_res) < 256:
        return tuple_res
    else:
        k = max(tuple_res) / 256
        return tuple(map(lambda x: int(x * k), tuple_res))


def transparency(filename1, filename2):
    im1 = Image.open(filename1)
    im2 = Image.open(filename2)
    x, y = im1.size
    im_res = Image.new('RGB', (x, y))
    for j in range(y):
        for i in range(x):
            im_res.load()[i, j] = combine(im1.load()[i, j], im2.load()[i, j])
    im_res.save('res.jpg')


if __name__ == '__main__':
    transparency('image1.jpg', 'image2.jpg')
