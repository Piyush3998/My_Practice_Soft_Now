import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\piyus\OneDrive\W_O_R_K_S\SoftwareNow\logo.png")

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("Image with RGB Translation")
plt.show()

print("Type:", type(image))
print("Numpy Array:\n", image)
