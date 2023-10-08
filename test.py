from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
 
plt.title("Sheep Image")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")
 
image = mpimg.imread("magnetic-reconnection\map2.png")
#color = image.getpixel((300, 200))
#print(color)
plt.imshow(image)
plt.show()

