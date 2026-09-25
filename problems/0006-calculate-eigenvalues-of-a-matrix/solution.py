def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]
	Det = a*d - b*c
	trA = a + d
	D = ((a+d)**2) - (4 * Det)
	if D >= 0:
		x1 = ((a+d) + D**0.5)/2
		x2 = ((a+d) - D**0.5)/2
		k = []
		k.append(x1)
		k.append(x2)
		return k
	else:
		return 0
	
	#return eigenvalues
	return eigenvalues