from PIL import Image, ImageDraw


def picture(file_name, width=500, height=500, sky_color='#87ceeb',
            ocean_color='#017b92', boat_color='#874535',
            sail_color='#ffffff', sun_color='#ffcf40'):
    im = Image.new('RGB', (width, height))
    drawer = ImageDraw.Draw(im)
    drawer.rectangle(((0, 0), (width, height * 0.8)), sky_color)
    drawer.rectangle(((0, height), (width, height * 0.8)), ocean_color)
    drawer.ellipse(((int(0.8 * width), -int(0.2 * height)), (int(1.2 * width), int(0.2 * height))), sun_color)
    drawer.polygon(((int(0.25 * width), int(0.65 * height)), (int(0.49 * width), int(0.65 * height)),
                    (int(0.49 * width), int(0.3 * height)), (int(0.51 * width), int(0.3 * height)),
                    (int(0.51 * width), int(0.65 * height)), (int(0.75 * width), int(0.65 * height)),
                    (int(0.7 * width), int(0.85 * height)), (int(0.3 * width), int(0.85 * height))), boat_color)
    drawer.polygon(((int(0.51 * width), int(0.3 * height)), (int(0.66 * width), int(0.45 * height)),
                    (int(0.51 * width), int(0.6 * height))), sail_color)
    im.save(file_name, 'BMP')
