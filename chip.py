
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

def malloc_PCM(ws, xs):
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

    cost = np.zeros(shape=nlayer)
    alloc = np.ones(shape=nlayer)
    for layer in range(nlayer):
        nwl, _, nbl, _ = np.shape(ws[layer])
        cost[layer] = nwl * nbl
    assert (np.sum(alloc * cost) <= narray)

    argmax = np.argmax(layer_cycles / alloc)
    while np.sum(alloc * cost) + cost[argmax] < narray:
        alloc[argmax] += 1
        argmax = np.argmax(layer_cycles / alloc)

    return alloc

############################

def malloc_SRAM(ws, xs, alloc_PCM):
    assert (ws.keys() == xs.keys())
    assert ( len(ws.keys())-1 == max(list(ws.keys())) )

    ################################################

    nSRAM = 128
    nlayer = len(ws.keys())

    ################################################

    # need {cycles, macs}, ect for this function
    # so we need to abtract from malloc_PCM

    layer_bandwidth = np.zeros(shape=nlayer)
    layer_capacity = np.zeros(shape=nlayer)

    for layer in range(nlayer):
        layer_bandwidth[layer] = 0.

    ################################################

    # problem is not optimization
    # problem is satisfaction
    
    # if we have tons of SRAM, then no problem.
    # if not much SRAM, where it is bottleneck or barely enof:

    # challenge will be difference between capacity and bandwidth

    # do we have to do that here though ? 
    # shouldnt this function just allocate, routing figures the rest out ? 

    # what if we are capacity constrained ? 
    # its realistic because 
    # (1) we have all activations on chip
    # (2) we are trying to support all kinds of modes
    # layer-by-layer 1b-8b could save you here.
    # if not enough capacity -> layer-by-layer

    # we have to make an assumption though.
    # assume there exists enough SRAM capacity 
    # BUT, you might have to parition and share SRAMs with bandwidth and capacity.

    ################################################

    alloc = None
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
        alloc_PCM = malloc_PCM(ws, xs) # breaking barriers
        alloc_SRAM = malloc_SRAM(ws, xs, alloc_PCM)
        # 
        # place = placement(alloc)
        # route = routing(place)

############################


            
            
            
            
            
            
            
            
            

