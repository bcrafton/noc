
import numpy as np
from modules import *
from transform_weights import transform_weights
from transform_inputs import transform_inputs

############################

def bits(model, inputs):
    xh, xw, xc, xn = np.shape(inputs)    
    size = xh
    ws = []
    xs = []
    for layer in model.keys():
        w = model[layer]['f']
        k, _, c, n = np.shape(w)
        p1 = model[layer]['p1']
        p2 = model[layer]['p2']
        s  = model[layer]['s']
        
        w = np.reshape(w, (k * k * c, n)).astype(int)
        ws.append(transform_weights(w))

        x = (size, size, c)
        xs.append(x)
        size = (size - k + s + p1 + p2) // s

    return ws, xs

############################

def malloc(grid, w, x):
    nwl, _, nbl, _ = np.shape(w)
    nd = 8 // nbl
    
    # allocate [nwl] grid cells.
    col = np.floor(np.sqrt(nwl))
    row = nwl // col
    rem = nwl % col
    # nwl=3 -> [col=1, row=3, rem=0]

    # pick a start address
    # this should be an optimization problem
    # create clusters, then figure out how to route them.
    # 

############################

class chip:

    def __init__(self):

        self.grid = [ [None for _ in range(4)] for _ in range(4) ]

        # generate all [SRAM, PCRAM] pairs
        for i in range(4):
            for j in range(4):
                self.grid[i][j] = {'PCM': PCM(), 'SRAM': SRAM()}

    def map(self, model, inputs):
        ws, xs = bits(model, inputs)
        alloc = malloc(ws, xs) # breaking barriers
        place = placement(alloc)
        route = routing(place)




            
            
            
            
            
            
            
            
            

