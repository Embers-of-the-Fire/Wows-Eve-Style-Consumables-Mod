from PIL import Image

image = Image.open('banned-red.png')

width, height = image.size

new_image = Image.new("RGBA", (width, height))

for x in range(width):
    for y in range(height):
        r, g, b, a = image.getpixel((x, y))
        if r >= 230 and g > 70 and b > 55:
            r, g, b = 247, 146, 21
        else:
            r, g, b = 197, 122, 29
        new_image.putpixel((x, y), (r, g, b, a))

new_image.save('banned-orange.png', mode='RGBA')


