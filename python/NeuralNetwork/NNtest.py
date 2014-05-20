import numpy as np
import sys
sys.path.append('../')
from NeuralNetwork import Layer
from Utility import Util

inputLayer = Layer( 10 )
outputLayer = Layer( 2 )

inputLayer.SetNextLayer( outputLayer )
inputLayer.InitWeight()

inputLayer.nodeValues = np.array( [1, 0, 0, 1, 0, 1, 1, 0, 0, 1] )
outputLayer.nodeValues = Util.Sigmoid( np.dot( inputLayer.weights.T, inputLayer.nodeValues ) )
