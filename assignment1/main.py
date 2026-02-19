import cv2 as cv
import numpy as np
from histogram import compute_histogram

img = cv.imread("images/Oring1.jpg", 0)

hist = compute_histogram(img)

print("Total pixels:", np.sum(hist))

cv.imshow("Original", img)

cv.waitKey(0)

cv.destroyAllWindows()