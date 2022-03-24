from PIL import Image

im = Image.open('image.jpg')
pixels = im.load()
x, y = im.size
R = sum(pixels[i, j][0] for j in range(y) for i in range(x)) // (x * y)
G = sum(pixels[i, j][1] for j in range(y) for i in range(x)) // (x * y)
B = sum(pixels[i, j][2] for j in range(y) for i in range(x)) // (x * y)
print(R, G, B)
