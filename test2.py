from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
 
img = Image.open("magnetic-reconnection\map.gif")
color = img.getpixel((450, 200))
print(color)
img.show()
