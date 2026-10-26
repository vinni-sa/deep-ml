import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	
	s = {}
	k = 0
	for i in range(len(gradient)):
		k += gradient[i] ** 2
	L2 = k**0.5

	s['magnitude'] = L2
	s['direction'] = []
	s['descent_direction'] = []
	for i in range(len(gradient)):
		if L2 != 0:
			s['direction'].append(gradient[i]/L2)
			s['descent_direction'].append(-1 * gradient[i]/L2)
		else:
			s['direction'].append(0.0)
			s['descent_direction'].append(0.0)
	
	return s
	
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	
	pass