
import numpy as np
import tensorflow as tf

from transform_weights import transform_weights
from transform_inputs import transform_inputs

from chip import chip

############################################

weights = np.load('cnn.npy', allow_pickle=True).item()
inputs = np.load('act.npy', allow_pickle=True).item()

############################################

c = chip()
c.map(weights, inputs)

############################################













