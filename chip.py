
import numpy as np
from modules import *
from transform_weights import transform_weights
from transform_inputs import transform_inputs

############################

def wbits(model):
    ws = []
    for layer in model.keys():
        w = model[layer]['f']
        k, _, c, n = np.shape(w)
        w = np.reshape(w, (k * k * c, n)).astype(int)
        ws.append(transform_weights(w))
    return ws

############################

def xbits(model, inputs):
    for layer in model.keys():
        pass
        # need more than just list of weights.
        # need actual CNN model ... with pools and shit.
        # need batches as well
        # generate intermediate activations for profiling.
        # also will make life easy to have real tensors for allocating SRAM.
    return xs

############################

def malloc(ws, xs):
    # nwl, _, nbl, _ = np.shape(ws)
    for x in xs:
        print (np.shape(x))

############################

class chip:

    def __init__(self):

        self.grid = [ [None for _ in range(4)] for _ in range(4) ]

        # generate all [SRAM, PCRAM] pairs
        for i in range(4):
            for j in range(4):
                self.grid[i][j] = {'PCM': PCM(), 'SRAM': SRAM()}

    def map(self, model, inputs):
        ws = wbits(model)
        alloc = malloc(ws, xs) # breaking barriers
        # place = placement(alloc)
        # route = routing(place)




            
            
            
            
            
            
            
            
            

