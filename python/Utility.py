import numpy as np

class Util:
	@classmethod
	def Sigmoid( self, x, gain=1 ):
		return 1.0 / ( 1.0 + np.exp( (-1)*gain*x ) )
