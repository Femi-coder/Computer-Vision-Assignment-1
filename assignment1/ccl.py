import numpy as np
from collections import deque

def connected_components(binary_img):
    rows, cols = binary_img.shape
    labels = np.zeros((rows, cols), dtype=int)
    
    label = 0
    component_sizes = {}
    
    for i in range(rows):
        for j in range(cols):
            
            #If Pixel is foreground and not labelled
             if binary_img[i, j] == 255 and labels[i, j] == 0:
                 
                label += 1
                queue = deque()
                queue.append((i, j))
                labels[i, j] = label
                size = 1
                
                while queue:
                    x, y = queue.popleft()
                
                # 8-Connectivity
                for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            nx = x + dx
                            ny = y + dy
                            
                            if (0 <= nx < rows and
                                0 <= ny < cols and
                                binary_img[nx, ny] == 255 and
                                labels[nx, ny] == 0):
                                
                                labels[nx, ny] = label
                                queue.append((nx, ny))
                                size += 1
                                
                        component_sizes[label] = size
                                
    return labels, component_sizes
