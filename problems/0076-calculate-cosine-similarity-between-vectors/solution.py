import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	a = 0
	b = 0
	c = 0
	if len(v1) == len(v2):
		for i in range(len(v1)):
			c += v1[i] * v2[i]
			a += v1[i]**2
			b += v2[i]**2
		return c/(a**0.5*b**0.5)
		
	pass