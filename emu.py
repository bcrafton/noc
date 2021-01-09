
import numpy as np
import tensorflow as tf

from transform_weights import transform_weights
from transform_inputs import transform_inputs

############################################

# put weights into 256x32 groups
# 128 array
# 128x256x32
# = 1 MB 
# wow thats clean.

# [64, 128, 256] -> 1144512 
# [32, 64, 128] -> 286560

# use this smaller CNN.

############################################

weights = np.load('cnn.npy', allow_pickle=True).item()

w_arrays = []
for layer in [0, 1, 2, 3, 4, 5]:
    w = weights[layer]['f']
    k1, k2, c, n = np.shape(w)
    assert (k1 == k2)
    w = np.reshape(w, (k1 * k2 * c, n)).astype(int)
    w_arrays.append(transform_weights(w))

############################################

def quantize(x, low, high):
    scale = np.max(np.abs(x)) / high
    x = x / scale
    x = np.round(x)
    x = np.clip(x, low, high)
    return x.astype(int)

############################################

(_, _), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_test = quantize(x_test, -128, 127)
# inputs = transform_inputs(x_test[0], k1, s, p1, p2)

############################################
'''
for w in w_arrays:
    nwl, _, nbl, _ = np.shape(w)
    print (nwl, nbl)
'''
############################################

# now we need to create some graph.
# where we can do the mappings of {SRAM / ARRAY / VECTOR}
# thinking vectors will be tied to SRAM

############################################

# 256 arrays
# vectors + SRAM ... PCRAM
# what are bandwidth of each block ? 
# > dont worry about specs, we need to get something going.

# so we need to create 2D NoC data structure
# (1) 2D list of objects ? 
# (2) or graph with {key : value} lookups ? 

############################################

from chip import chip

c = chip()

############################################

















