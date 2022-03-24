from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#75bbfd',
            snow_color='#fffafa', trunk_color='#a45a52',
            needls_color='#01796f', sun_color='#ffdb00'):
    im = Image.new('RGB', (width, height), sky_color)
    drawer = ImageDraw.Draw(im)
    drawer.polygon(((int(0.5 * width), int(0.1 * height)), (int(0.6 * width), int(0.3 * height)),
                    (int(0.55 * width), int(0.3 * height)
                     ), (int(0.65 * width), int(0.5 * height)),
                    (int(0.6 * width), int(0.5 * height)
                     ), (int(0.7 * width), int(0.7 * height)),
                    (int(0.3 * width), int(0.7 * height)
                     ), (int(0.4 * width), int(0.5 * height)),
                    (int(0.35 * width), int(0.5 * height)
                     ), (int(0.45 * width), int(0.3 * height)),
                    (int(0.4 * width), int(0.3 * height)), (int(0.5 * width), int(0.1 * height))),
                   fill=needls_color)
    drawer.ellipse(((int(0.8 * width), -int(0.2 * height)),
                   (int(1.2 * width), int(0.2 * height))), fill=sun_color)
    drawer.polygon(((0, height), (0, 0.8 * height),
                    (width, 0.8 * height), (width, height)), fill=snow_color)
    drawer.polygon(((0.45 * width, 0.9 * height), (0.45 * width, 0.7 * height),
                    (0.55 * width, 0.7 * height), (0.55 * width, 0.9 * height)), fill=trunk_color)
    im.save(file_name, 'BMP')


if __name__ == '__main__':
    picture('pic1.bmp', 1000, 1000)
