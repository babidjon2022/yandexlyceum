from PIL import Image


def choose_color(color):
    if color in {'r', 'R'}:
        return 255, 0, 0
    if color in {'g', 'G'}:
        return 0, 255, 0
    if color in {'b', 'B'}:
        return 0, 0, 255


def gradient(color):
    im = Image.new('RGB', (512, 200), choose_color(color))
    colors = im.load()
    d = list(map(lambda i: tuple(
        map(lambda x: x * (i // 2 + 1) // 256, choose_color(color))), range(512)))
    for i in range(512):
        for j in range(200):
            colors[i, j] = d[i]
    im.save('res.png')
