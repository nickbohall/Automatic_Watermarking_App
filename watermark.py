# Import required Image library
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

# Create tkinter window
root = Tk()
root.withdraw()

filename = filedialog.askopenfilename(initialdir='images', title="Select an Image: ")
outputname = filename.split("/")[-1]


def add_watermark(image, wm_text):
    # Create image object and transparency object
    im = Image.open(image).convert("RGBA")
    rgba_im = Image.new('RGBA', im.size, (255, 255, 255, 0))

    image_width, image_height = im.size

    # Create Draw Object
    draw = ImageDraw.Draw(rgba_im)

    # Create font parameters
    font_size = int(image_width / 10)
    font = ImageFont.truetype('arial.ttf', font_size)

    # Get coordinates for where we want the wm
    x, y = int(image_width / 2), int(image_height / 2)

    # Add the watermark to the blank RGBA image
    draw.text((x, y), wm_text, font=font, fill=(204, 204, 255, 50), stroke_width=3, stroke_fill=(34,2,0,125), anchor='ms')

    # Combine the watermark RGBA image with the original image to get transparency effect
    rgba_im = rgba_im.rotate(30)
    watermarked = Image.alpha_composite(im, rgba_im).convert("RGB")

    # Show the result and save in output folder
    watermarked.show()
    watermarked.save(f"watermarked_images/marked_{outputname}")


add_watermark(filename, "Yoonicaps")

