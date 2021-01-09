
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

    def step(self):
        pass

    def map(self, model, inputs):
        # set PCM and SRAM to hold specific parts of our model and activations.
        # this is probably a whole field we dont know about.
        #
        ws, xs = bits(model, inputs)
        
        grid = np.zeros(shape=(4, 4))
        for (w, x) in zip(ws, xs):
            # malloc - where to place w and x ? 
            malloc(grid, w, x)
            # what about when we cant store the whole input in the SRAM ? 
            # need to "orchestrate" the transfer to all adjacent nodes.
            # 
            # allocate
            # placement / mapping
            # routing
            # 
            # think problem is small enough such that we can find optimal solution
            # 
            # we already did allocation with breaking barriers.
            # but now we have to do the other parts.
            # 
            # 
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
