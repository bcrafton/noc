
import numpy as np

WL = 256
BL = 256
XB = 8
WB = 8

def transform_inputs(x, k, s, p1, p2):

    xh, xw, xc, xn = np.shape(x)

    #########################

    yh = (xh - k + s + p1 + p2) // s
    yw = yh
    
    #########################
    
    x = np.pad(array=x, pad_width=[[p1, p2], [p1, p2], [0,0]], mode='constant')
    patches = []
    for h in range(yh):
        for w in range(yw):
            patch = x[h*s:(h*s+k), w*s:(w*s+k), :]
            patch = np.reshape(patch, k * k * xc)
            patches.append(patch)
            
    #########################
    
    patches = np.stack(patches, axis=0).astype(int)
    xb = []
    for b in range(XB):
        xb.append(np.bitwise_and(np.right_shift(patches, b), 1))
    patches = np.stack(xb, axis=-1)

    #########################

    assert (np.shape(patches) == (yh * yw, k * k * xc, 8))
    npatch, nrow, _ = np.shape(patches)

    if (nrow % WL):
        zeros = np.zeros(shape=(npatch, WL - (nrow % WL), XB))
        patches = np.concatenate((patches, zeros), axis=1)
    patches = np.reshape(patches, (npatch, -1, WL, XB))
    
    #########################
    
    return patches
