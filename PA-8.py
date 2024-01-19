import numpy as np

def strassen(A, B):
    if len(A) == 1:
        return A[0, 0] * B[0, 0]

    mid = len(A) // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]
    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    P = strassen(A11 + A22, B11 + B22)
    Q = strassen(B11, A21 + A22)
    R = strassen(A11, B12 - B22)
    S = strassen(A22, B21 - B11)
    T = strassen(B22, A11 + A12)
    U = strassen(A21 - A11, B11 + B12)
    V = strassen(B21 + B22, A12 - A22)

    C = np.zeros((2 * mid, 2 * mid))
    C[:mid, :mid] = P + S - T + V
    C[:mid, mid:] = R + T
    C[mid:, :mid] = Q + S
    C[mid:, mid:] = P + R - Q + U

    return C

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])


result = strassen(A, B)
print(result)