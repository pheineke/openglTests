from PIL import Image

def heightgrabber():
    img = Image.open('heightmap3.png')
    img_gray = img.convert('L')
    width, height = img_gray.size
    pixel_matrix = []

    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = img_gray.getpixel((x, y))
            row.append(pixel_value)
        pixel_matrix.append(row)

    print(pixel_matrix)

heightgrabber()