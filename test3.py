from PIL import Image

im = Image.open("magnetic-reconnection\map.gif").convert('RGB')
r, g, b = im.getpixel((329, 463))
a = (r, g, b)
print(a)

if(im.getpixel((329, 463)) == 74, 161, 112):
    print("yay!")





