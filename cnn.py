
import numpy as np

weights = np.load('cifar10_weights.npy', allow_pickle=True).item()

# print (weights.keys())
# dict_keys([0, 1, 2, 3, 4, 5, 6, 7])

# print (weights[0].keys())
# dict_keys(['f', 'b', 'q'])

weights[0].update({'k': 3, 's': 1, 'p1': 1, 'p2': 1})
weights[1].update({'k': 3, 's': 1, 'p1': 1, 'p2': 1})
weights[2].update({'k': 3, 's': 1, 'p1': 1, 'p2': 1})
weights[3].update({'k': 3, 's': 1, 'p1': 1, 'p2': 1})
weights[4].update({'k': 3, 's': 1, 'p1': 1, 'p2': 1})
weights[5].update({'k': 3, 's': 1, 'p1': 1, 'p2': 1})

del weights[6]
del weights[7]

np.save('cnn', weights)

