from PIL import Image


def twist_image(input_file_name, output_file_name):
    im = Image.open(input_file_name)
    pixels = im.load()
    x, y = im.size
    for j in range(y):
        d = [pixels[i, j] for i in range(x)]
        if len(d) % 2 == 0:
            d = d[int(len(d) / 2):] + d[:int(len(d) / 2)]
        else:
            d = d[int(len(d) / 2) + 1:] + \
                d[int(len(d) / 2)] + d[:int(len(d) / 2)]
        for i in range(x):
            pixels[i, j] = d[i]
    im.save(output_file_name)
