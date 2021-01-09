
import numpy as np

WL = 256
BL = 256
XB = 8
WB = 8

def transform_weights(w):
    assert (len(np.shape(w)) == 2)
    row, col = np.shape(w)

    w = w + (2 ** (WB - 1))
    wb = []
    for b in range(WB):
        wb.append(np.bitwise_and(np.right_shift(w, b), 1))
    wb = np.stack(wb, axis=-1)

    #################################

    assert (np.shape(wb) == (row, col, WB))
    if row % WL:
        pad = np.zeros(shape=(WL - (row % WL), col, WB))
        wb = np.concatenate((wb, pad), axis=0)

    row, col, _ = np.shape(wb)
    wb = np.reshape(wb, (-1, WL, col, WB))

    #################################

    nwl, _, col, _ = np.shape(wb)    
    wb = np.reshape(wb, (nwl, WL, col * WB))
    
    nwl, wl, ncol = np.shape(wb)
    if (ncol % BL):
        zeros = np.zeros(shape=(nwl, WL, BL - (ncol % BL)))
        wb = np.concatenate((wb, zeros), axis=2) 

    wb = np.reshape(wb, (nwl, WL, -1, BL))

    #################################

    return wb
