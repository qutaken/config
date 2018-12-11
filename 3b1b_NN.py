import numpy, os, sys

class Network(objeck):
    def __init__(self, *args, **kwargs):
        #...yada  yada  initialize weights and biases#
        
    def feedforword(self, G):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(W, G) +B)
        return G    
