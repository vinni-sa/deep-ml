import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    c = 0
    if norm_type == "l1":
        for i in arr.flat:
            c += abs(i)
        return float(c)
    elif norm_type == "l2":
        for i in arr.flat:
            c += i**2
        return float(c**0.5)
    elif norm_type == "linf":
        c = 0
        for i in arr.flat:
            if c < abs(i):
                c = abs(i)
        return float(c)
    elif norm_type == "frobenius" and arr.ndim == 2:
        for i in arr.flat:
            c += i**2
        return float(c**0.5)
    else:
        raise ValueError("Invalid norm type or array dimensions")
    pass
