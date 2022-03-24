from PIL import Image


def board(n, s):
    im = Image.new('RGB', (n * s, n * s), (0, 0, 0))
    pixels = im.load()
    r1, r2 = list(), list()
    for i in range(n):
        if i % 2 == 0:
            for _ in range(i * s, s * (i + 1)):
                r1.append((0, 0, 0))
                r2.append((255, 255, 255))
        else:
            for _ in range(i * s, s * (i + 1)):
                r1.append((255, 255, 255))
                r2.append((0, 0, 0))
    for i in range(n):
        if i % 2 == 0:
            for x in range(i * s, s * (i + 1)):
                for y in range(n * s):
                    pixels[x, y] = r1[y]
        else:
            for x in range(i * s, s * (i + 1)):
                for y in range(n * s):
                    pixels[x, y] = r2[y]
    im.save('res.png')
