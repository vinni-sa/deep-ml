import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	n = []
	m = []
	for i in range (len(a)):
		if (len(a[i])*len(a)) % new_shape[1] == 0:
			for j in range(len(a[i])):
				m.append(a[i][j])
				if len(m) == new_shape[1]:
					n.append(m)
					m = []
		else:
			return n

	if len(n) == new_shape[0]:
		return n
	else:
		return []

	return reshaped_matrix