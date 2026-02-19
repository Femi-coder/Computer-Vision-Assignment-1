import numpy as np

def compute_histogram(image):

    # Create empty histogram (256 intensity levels)
    hist = np.zeros(256, dtype=int)
    
    # Get image dimensions
    rows, cols = image.shape
    
    # Loop through pixels
    for i in range(rows):
        for j in range(cols):
            intensity = image[i, j]
            hist[intensity] += 1
    
    return hist
