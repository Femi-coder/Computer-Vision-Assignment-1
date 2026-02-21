import cv2 as cv
import numpy as np
from histogram import compute_histogram
from threshold import otsu_threshold

img = cv.imread("images/Oring1.jpg", 0)

hist = compute_histogram(img)

print("Total pixels:", np.sum(hist))

T = otsu_threshold(hist)

print("Otsu threshold:", T)

cv.imshow("Original", img)

cv.waitKey(0)

cv.destroyAllWindows()