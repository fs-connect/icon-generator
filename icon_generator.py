import sys
import os
from PIL import Image, ImageFilter

def generate_base_16_16_png (filename):
    size = (16, 16)
    saved = "connect_icon.png"
    try:
        img = Image.open(filename)
        width, height = img.size
        if (width != height):
            print ("Error: Aspect ratio of image must be 1:1")
            return
        img.thumbnail(size)
        img.save(saved)

        return img

    except:
        print( "Error: Unable to load image " + filename)




def generate_grayscale_png (img):
    img = img.convert('LA')
    img.save("gray_connect_icon.png")
    return

def generate_failed_png(img):
    try:
        filename = "failed.png"
        img_failed = Image.open(filename, 'r')
        final_img = Image.new('RGBA', (16,16), (0, 0, 0, 0))
        final_img.paste(img, (0,0))
        final_img.paste(img_failed, (0,11))
        final_img.save("failed_connect_icon.png", format="png")
    except:
        print("Error: Unable to crate failed_connect.png verify base failed.png is present")


def generate_waitting_png(img):
        try:
            filename = "waiting.png"
            img_waiting = Image.open(filename, 'r')
            final_img = Image.new('RGBA', (16,16), (0, 0, 0, 0))
            final_img.paste(img, (0,0))
            final_img.paste(img_waiting, (0,11))
            final_img.save("waiting_connect_icon.png", format="png")
        except:
            print("Error: Unable to crate waiting_connect.png verify base waiting.png is present")


def main():
    try:
        path = sys.argv[1]
    except:
        print ("Error: Exception Must pass in the base image filename")
    if (len(sys.argv) != 2):
        print("Error: Must pass in exactly one argument")
        return

    if not os.path.exists(path):
        print ("Error: No such file")
        return

    if path.lower().endswith(('.png', '.jpg', '.jpeg')):
        img = generate_base_16_16_png(path)
        if (img):
            generate_grayscale_png(img)
            generate_failed_png(img)
            generate_waitting_png(img)
        else:
            print("Error: Failed to generate icons")
            return


    else:
        print ("Invalid File type: icon generator can accept .png, .jpg, and .jpeg")
        return




if __name__ == "__main__":
    main()
