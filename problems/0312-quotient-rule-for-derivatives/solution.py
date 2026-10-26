import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:

    n = len(g_coeffs)
    d_g = np.diag(np.arange(n-1, 0, -1), k=1)
    n_d = g_coeffs @ d_g

    n_d_x = np.polyval(n_d,x)
    n_x = np.polyval(g_coeffs,x)

    m = len(h_coeffs)
    d_h = np.diag(np.arange(m-1, 0, -1), k=1)
    m_d = h_coeffs @ d_h

    m_d_x = np.polyval(m_d,x)
    m_x = np.polyval(h_coeffs,x)

    f_x = (n_d_x * m_x - m_d_x * n_x) / m_x ** 2 

    return f_x

    pass