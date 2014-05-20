import numpy as np

class Layer:
	def __init__( self, dim ):
		self.dim = dim
		self.nodeValues = np.zeros( dim )
		
		self.nextLayer    = None
		self.nextLayerDim = None
		self.weights      = None
	
	# ------------------------------------------------- #
	
	def SetNextLayer( self, layer ):
		self.nextLayer    = layer
		self.nextLayerDim = layer.dim
	
	# ------------------------------------------------- #
	
	def InitWeight( self, initMode='random' ):
		if self.nextLayer==None:
			print '!!!Error!!! Next layer is not found --- setNextLayer() must be called first.'
			return
		
		if initMode=='random':
			self.weights = np.random.rand( self.dim, self.nextLayerDim )
		else:
			self.weights = np.zeros( ( self.dim, self.nextLayerDim ) )
	
	# ------------------------------------------------- #
	
	def ShowMembers( self ):
		print 'dim : ' + str( self.dim )
		print 'nodeValues : ' + str( self.nodeValues )
		print 'weights : ' + str( self.weights )
		print ''
	
	# ------------------------------------------------- #
	
