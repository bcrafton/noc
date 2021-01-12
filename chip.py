
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
        xs[layer] = transform_inputs(x[0], 3, 1, 1, 1) # hardcoded.
    return xs

############################

def compute_params(ws, xs):
    assert (ws.keys() == xs.keys())
    assert ( len(ws.keys())-1 == max(list(ws.keys())) )

    ################################################

    ADC = 8
    narray = 128 # not accurate because we only have groups of 8.
    nlayer = len(ws.keys())

    ################################################

    layer_cycles = np.zeros(shape=nlayer)
    for layer in range(nlayer):
        w = ws[layer] # [NWL, WL, NBL, BL]
        x = xs[layer] # [P, NWL, WL, XB]

        nwl, wl, nbl, bl = np.shape(w)
        # np, nwl, wl, nb = np.shape(x) # cant use "np"

        ones = np.sum(x, axis=2)
        cycles = np.ceil(ones / ADC)
        layer_cycles[layer] = np.sum(cycles * nbl)

    ################################################

    params = {}
    params['cycles'] = layer_cycles
    params['nLayer'] = nlayer
    params['ADC'] = 8
    params['nPCM'] = 128
    params['nSRAM'] = 128

    return params

############################

def malloc_PCM(ws, xs, params):
    assert (ws.keys() == xs.keys())
    assert ( len(ws.keys())-1 == max(list(ws.keys())) )

    cost = np.zeros(shape=params['nLayer'])
    alloc = np.ones(shape=params['nLayer'])
    for layer in range(params['nLayer']):
        nwl, _, nbl, _ = np.shape(ws[layer])
        cost[layer] = nwl * nbl
    assert (np.sum(alloc * cost) <= params['nPCM'])

    argmax = np.argmax(params['cycles'] / alloc)
    while np.sum(alloc * cost) + cost[argmax] < params['nPCM']:
        alloc[argmax] += 1
        argmax = np.argmax(params['cycles'] / alloc)

    return alloc

############################

def malloc_SRAM(ws, xs, params, alloc_PCM):
    assert (ws.keys() == xs.keys())
    assert (len(ws.keys())-1 == max(list(ws.keys())))

    ################################################

    # do we need {cycles, macs}, for this function ?
    # only if we are bandwidth limited I think

    layer_bandwidth = np.zeros(shape=params['nLayer'])
    layer_capacity = np.zeros(shape=params['nLayer'])

    for layer in range(params['nLayer']):
        layer_bandwidth[layer] = 0.

    ################################################

    return alloc    

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
        params = compute_params(ws, xs)
        alloc_PCM = malloc_PCM(ws, xs, params) # breaking barriers
        alloc_SRAM = malloc_SRAM(ws, xs, params, alloc_PCM)
        # 
        # place = placement(alloc)
        # route = routing(place)

############################


            
            
            
            
            
            
            
            
            

