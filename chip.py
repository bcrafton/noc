
import numpy as np
from modules import *
from transform_weights import transform_weights
from transform_inputs import transform_inputs

############################

def wbits(model):
    ws = {}
    for layer in model.keys():
        w = model[layer]['f']
        k, _, c, n = np.shape(w)
        w = np.reshape(w, (k * k * c, n)).astype(int)
        ws[layer] = transform_weights(w)
    return ws

############################

def xbits(inputs):
    xs = {}
    for layer in inputs.keys():
        x = inputs[layer].astype(int)
        xs[layer] = transform_inputs(x[0], 3, 1, 1, 1)
    return xs

############################

def malloc(ws, xs):
    assert (ws.keys() == xs.keys())

    layer_cycles = {}
    total_cycles = 0
    for layer in ws.keys():
        w = ws[layer] # [NWL, WL, NBL, BL]
        x = xs[layer] # [P, NWL, WL, XB]

        nwl, wl, nbl, bl = np.shape(w)
        # np, nwl, wl, nb = np.shape(x)

        ADC = 8
        ones = np.sum(x, axis=2)
        cycles = np.ceil(ones / ADC)
        layer_cycles[layer] = np.sum(cycles * nbl)
        total_cycles += layer_cycles[layer]

    '''
    print (total_cycles.keys())
    print (total_cycles.values())

    share = {}
    for layer in ws.keys():
        share[layer] = layer_cycles[layer] / total_cycles

    print (share.values())
    '''

    alloc = {}
    for layer in ws.keys():
        alloc[layer] = 0

    # use the same algorithm as before
    array = 128
    for layer in ws.keys():
        alloc[layer] = nwl * nbl
        array -= nwl * nbl

    # so clear problem here is with our choice of data structures.
    # want np array, not stupid dictionary.

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
        xs = xbits(inputs)
        alloc = malloc(ws, xs) # breaking barriers
        # place = placement(alloc)
        # route = routing(place)

############################


            
            
            
            
            
            
            
            
            

