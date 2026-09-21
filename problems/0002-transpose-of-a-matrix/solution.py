def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """

    n = []
    for i in range(len(a[0])):
        m = []
        for j in range(len(a)):
            m.append(a[j][i])
        n.append(m)

    return n

    # Your code here
    pass