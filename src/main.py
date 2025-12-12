import cv2
import numpy as np
import matplotlib.pyplot as plt

n_levels = 5

img = "assets/input.jpg"    
img_bgr = cv2.imread(img)

if img_bgr is None:
    raise FileNotFoundError("Image not found. Make sure input.jpg exists.")


img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)


img_rgb_blur = cv2.medianBlur(img_rgb, 5)


def create_lut(n):
    
    levels = np.linspace(0, 255, n).astype(np.uint8)
    lut = np.zeros(256, dtype=np.uint8)

    for i in range(256):
        idx = int(round((n - 1) * i / 255.0))
        lut[i] = levels[idx]

    return lut

lut = create_lut(n_levels)

poster_rgb = cv2.LUT(img_rgb_blur, lut)


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(poster_rgb)
plt.title(f"Posterized (Levels = {n_levels})")
plt.axis("off")

plt.tight_layout()
plt.show()

poster_bgr = cv2.cvtColor(poster_rgb, cv2.COLOR_RGB2BGR)
cv2.imwrite("results/output.jpg", poster_bgr)

print("Saved result as output.jpg")
