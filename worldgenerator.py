from PIL import Image
import pickle


path = ""
filename = ""

def setpath(path0):
    global path
    path = path0

def setfilename(filename0):
    global filename
    filename = filename0

def pictoheightfile(heightmap):
    filepath = path + heightmap + ".png"
    img = Image.open(filepath)
    img_gray = img.convert('L')
    width, height = img_gray.size
    pixel_matrix = []

    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = img_gray.getpixel((x, y))
            row.append(0.97**(-pixel_value+10))
        pixel_matrix.append(row)

    return pixel_matrix

def save_pixel_matrix(pixel_matrix, filename):
    filepath = path + filename
    print(filepath)
    with open(filepath, 'wb') as file:
        pickle.dump(pixel_matrix, file)

def load_pixel_matrix():
    filepath = path + filename
    print(filepath)
    with open(filepath, 'rb') as file:
        pixel_matrix = pickle.load(file)
    return pixel_matrix

def worldgenerator(path, picname, heightfile):
    setpath(path)
    setfilename(heightfile)
    save_pixel_matrix(pictoheightfile(picname), heightfile)
    return load_pixel_matrix()

