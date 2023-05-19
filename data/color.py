# pip install colorthief

from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

ct = ColorThief("test.jpg")
dominant_color = ct.get_color(quality=1)
print(dominant_color)
plt.imshow([[dominant_color]])
plt.show()