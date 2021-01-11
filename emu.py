
import numpy as np
import tensorflow as tf

from transform_weights import transform_weights
from transform_inputs import transform_inputs

from chip import chip

############################################

weights = np.load('cnn.npy', allow_pickle=True).item()

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
inputs = transform_inputs(x_test[0], 3, 1, 1, 1) # params should be taken from loaded model

############################################

c = chip()
c.map(weights, inputs)

############################################













