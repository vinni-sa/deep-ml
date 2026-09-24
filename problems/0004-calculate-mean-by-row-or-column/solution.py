def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if mode == 'column':
		n = len(matrix)
		m = len(matrix[0])
	else:
		n = len(matrix[0])
		m = len(matrix)
	
	means = []
	for i in range (m):
		avg = 0
		count = 0
		for j in range (n):
			if mode == 'column':
				avg += matrix[j][i]
			else:
				avg += matrix[i][j]
			count += 1
		means.append(avg / count)

	return means