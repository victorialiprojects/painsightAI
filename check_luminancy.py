import cv2
from PIL import Image
import PIL
import math

def calculate_luminance(R, G, B):
    # RGB to luminance formula: https://www.w3.org/WAI/GL/wiki/Relative_luminance
    return 0.2126 * R + 0.7152 * G + 0.0722 * B

def get_average_luminance(image, threshold):
    img = Image.open(image)
    img = img.convert('RGB')
 
    common_color = most_common_used_color(img)
    R, G, B = 0, 0,0 
    RsRGB, GsRGB, BsRGB = common_color[0]/255, common_color[1]/255, common_color[2]/255


    if RsRGB <= 0.03928:
        R = RsRGB/12.92
    else:
        R = math.pow(((RsRGB+0.055)/1.055), 2.4)
    
    if GsRGB <= 0.03928:
        G = GsRGB/12.92
    else:
        G = math.pow(((GsRGB+0.055)/1.055), 2.4)
    
    if BsRGB <= 0.03928:
        B = BsRGB/12.92
    else:
        B = math.pow(((BsRGB+0.055)/1.055), 2.4)
    
    
    # Calculate the average luminance
    average_luminance = calculate_luminance(R, G, B)
    print(average_luminance)
    
    return average_luminance>threshold

def most_common_used_color(img):
    # Get width and height of Image
    width, height = img.size
 
    # Initialize Variable
    r_total = 0
    g_total = 0
    b_total = 0
 
    count = 0
 
    # Iterate through each pixel
    for x in range(0, width):
        for y in range(0, height):
            # r,g,b value of pixel
            r, g, b = img.getpixel((x, y))
 
            r_total += r
            g_total += g
            b_total += b
            count += 1
 
    return (r_total/count, g_total/count, b_total/count)
