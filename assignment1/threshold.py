import numpy as np

def otsu_threshold(hist):
    total = np.sum(hist)
    
    #total sum of intensities
    sum_total = 0
    for i in range(256):
        sum_total += i * hist[i]
        
    sum_bg = 0
    w_bg = 0
    max_var = -1
    best_t = 0
    
    for t in range(256):
        w_bg += hist[t]
        if w_bg ==0:
            continue
        
        w_fg = total - w_bg
        if w_fg == 0:
            break
        
        sum_bg += t * hist[t]

        mu_bg = sum_bg / w_bg
        mu_fg = (sum_total - sum_bg) / w_fg

        var_between = w_bg * w_fg * (mu_bg - mu_fg) ** 2

        if var_between > max_var:
            max_var = var_between
            best_t = t

    return best_t