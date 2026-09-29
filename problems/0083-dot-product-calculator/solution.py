import numpy as np

def calculate_dot_product(vec1, vec2):
	sum_ = 0
	for i in range(len(vec1)):
		vec1[i] *= vec2[i]
		sum_ += vec1[i]
	return sum_
	pass