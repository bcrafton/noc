
import numpy as np
np.set_printoptions(threshold=1000)

#############

class model:
    def __init__(self, layers):
        self.layers = layers
        
    def forward(self, x):
        y = x
        for layer in self.layers:
            y = layer.forward(y)
        return y

#############

class layer:
    layer_id = 0

    def __init__(self):
        assert(False)
        
    def forward(self, x):        
        assert(False)
        
#############
        
class conv(layer):
    def __init__(self, w, s):
        self.layer_id = layer.layer_id
        layer.layer_id += 1

        self.w = w
        self.s = s

    def forward(self, x):
        pad = k // 2

        xh, xw, xc = np.shape(x)
        yh, yw, yc = (xh // s), (xw // s), xc

        x = np.pad(array=x, pad_width=[[pad,pad], [pad,pad], [0,0]], mode='constant')
        y = np.zeros(shape=(yh, yw, yc))
        for h in range(yh):
            for w in range(yw):
                y[h, w, :] = np.mean(x[h*s:(h*s+k), w*s:(w*s+k), :], axis=(0, 1))

        return y

#############

class avg_pool(layer):
    def __init__(self, s, p):
        self.layer_id = layer.layer_id
        layer.layer_id += 1
    
        self.s = s
        self.p = p
        
    def forward(self, x):        
        pad = k // 2

        xh, xw, xc = np.shape(x)
        yh, yw, yc = (xh // s), (xw // s), xc

        x = np.pad(array=x, pad_width=[[pad,pad], [pad,pad], [0,0]], mode='constant')
        y = np.zeros(shape=(yh, yw, yc))
        for h in range(yh):
            for w in range(yw):
                y[h, w, :] = np.mean(x[h*s:(h*s+k), w*s:(w*s+k), :], axis=(0, 1))

        return y
    
#############

class max_pool(layer):
    def __init__(self, s, p, weights=None):
        self.layer_id = layer.layer_id
        layer.layer_id += 1
    
        self.s = s
        self.p = p
        
    def forward(self, x):        
        p = k // 2

        xh, xw, xc = np.shape(x)
        yh, yw, yc = (xh // s), (xw // s), xc

        x = np.pad(array=x, pad_width=[[p,p], [p,p], [0,0]], mode='constant')
        y = np.zeros(shape=(yh, yw, yc))
        for h in range(yh):
            for w in range(yw):
                y[h, w, :] = np.max(x[h*s:(h*s+k), w*s:(w*s+k), :], axis=(0, 1))

        return y

#############




        
        
        
