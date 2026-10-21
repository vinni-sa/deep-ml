def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) == len(b):
		l = []
		for i in range(len(a)):
			k = 0
			for j in range(len(a[i])):
				k += a[i][j] * b[j]
			l.append(k)
		return l
	else:
		return -1
	pass