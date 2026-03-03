import cv2 as cv
import numpy as np
import time
from histogram import compute_histogram
from threshold import otsu_threshold
from morphology import closing
from ccl import connected_components

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

start = time.time()

hist = compute_histogram(img)
T = otsu_threshold(hist)
binary = apply_inverse_threshold(img, T)
cleaned = closing(binary)
cleaned = np.where(cleaned > 0, 255, 0).astype(np.uint8)
labels, sizes = connected_components(cleaned)
largest_label = max(sizes, key=sizes.get)
largest_size = sizes[largest_label]

end = time.time()

print("Total pixels:", np.sum(hist))
print("Otsu threshold:", T)
print("Segmentation time (seconds):", end - start)
print("Number of components:", len(sizes))
print("Component sizes:", sizes)
print("Largest component label:", largest_label)
print("Largest component size:", largest_size)

# Minimum area to be considered a real ring piece
min_area = 1000

# Find all components larger than threshold
large_components = [label for label, size in sizes.items() if size > min_area]

print("Large components:", large_components)

if len(large_components) == 1:
    result = "PASS"
else:
    result = "FAIL"

print("RESULT:", result)


# Create mask for largest component
ring_only = np.zeros_like(cleaned, dtype=np.uint8)

rows, cols = labels.shape
for i in range(rows):
    for j in range(cols):
        if labels[i, j] == largest_label:
            ring_only[i, j] = 255

cv.imshow("Original", img)
cv.imshow("Binary (Otsu)", binary)
cv.imshow("After Closing", cleaned)
cv.imshow("Largest Component", ring_only)

cv.waitKey(0)
cv.destroyAllWindows()