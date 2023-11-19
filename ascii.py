# from PIL import Image

# def resize_image(image, new_width=100):

#     width, height = image.size
#     return image.resize((new_width, int(new_width * height / width)))

# def grayify(image):

#     return image.convert("L")

# def pixels_to_ascii(image):

#     return "".join(["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."] [pixel//25] for pixel in image.getdata())

# print("\n".join(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))[index : (index + 100)] for index in range(0, len(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))), 100)))

# with open("ascii_image.txt", "w") as f:
#     f.write("\n".join(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))[index : (index + 100)] for index in range(0, len(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))), 100)))

# with open("ascii_image.txt", "w") as f:
#     f.write("\n".join(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))[index : (index + 100)] for index in range(0, len(pixels_to_ascii(grayify(resize_image(Image.open("image.jpg"))))), 100)))

from PIL import Image

img_path = input("Enter the path to the image file: ")

while True:
    try:
        img = Image.open(img_path)
    except Exception:
        img_path = input("File not found. Please enter a valid path: ")
        continue

    break

# Arranged from darkest ("@") for darker pixels to lightest (".") for lighter pixels.
ascii_chars = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

# Resizing the image to be 100px wide to limit the amount of text (aspect ratio is maintained).
width, height = img.size
height = int(100 * (height / width))
img.resize((100, height))

# Greyscale
img.convert("L")

pixel_sequence, output = img.getdata(), ""

# Converting the darkness of the pixel to the corresponding ascii character.
for pixel in pixel_sequence:
    output += ascii_chars[pixel[0] // 25]
