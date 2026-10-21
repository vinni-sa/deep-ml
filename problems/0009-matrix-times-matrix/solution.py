def matrixmul(a:list[list[int|float]],b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) == len(b):
        c = []
        for i in range(len(a)):
            k = []
            for j in range(len(b[0])):
                l = 0
                for y in range(len(b)):
                    l += a[i][y] * b[y][j]
                k.append(l)
            c.append(k)
        return c
    else:
        return -1