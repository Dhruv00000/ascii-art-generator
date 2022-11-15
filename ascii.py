from PIL import Image

def resize_image(image, new_width=100):

    width, height = image.size
    return image.resize((new_width, int(new_width * height / width)))

def grayify(image):

    return image.convert("L")

def pixels_to_ascii(image):

    return "".join(["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."] [pixel//25] for pixel in image.getdata())

print("\n".join(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))[index : (index + 100)] for index in range(0, len(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))), 100)))

with open("ascii_image.txt", "w") as f:
    f.write("\n".join(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))[index : (index + 100)] for index in range(0, len(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))), 100)))

with open("ascii_image.txt", "w") as f:
    f.write("\n".join(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))[index : (index + 100)] for index in range(0, len(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))), 100)))