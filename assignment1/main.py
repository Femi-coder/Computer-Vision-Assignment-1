import cv2 as cv
import numpy as np
from histogram import compute_histogram
from threshold import otsu_threshold

def apply_inverse_threshold(img, T):
    out = np.zeros_like(img, dtype=np.uint8)

    rows, cols = img.shape

    for i in range(rows):
        for j in range(cols):
            if img[i, j] < T:
                out[i, j] = 255   # ring foreground
            else:
                out[i, j] = 0     # background

    return out

img = cv.imread("images/Oring1.jpg", 0)

hist = compute_histogram(img)

print("Total pixels:", np.sum(hist))

T = otsu_threshold(hist)

print("Otsu threshold:", T)

binary = apply_inverse_threshold(img, T)

cv.imshow("Original", img)

cv.imshow("Binary (Otsu)", binary)

cv.waitKey(0)

cv.destroyAllWindows()