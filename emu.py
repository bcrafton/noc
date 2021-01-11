
import numpy as np
import tensorflow as tf

from transform_weights import transform_weights
from transform_inputs import transform_inputs

from chip import chip

############################################

# use "layers.py" to verify accuracy correctness.
# build simple numpy cnn model
weights = np.load('./data/cnn.npy', allow_pickle=True).item()
inputs = np.load('./data/act.npy', allow_pickle=True).item()

############################################

c = chip()
c.map(weights, inputs)

############################################













