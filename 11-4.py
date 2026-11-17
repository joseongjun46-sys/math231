import numpy as np

# (1) 상부삼각행렬
A = np.array([[0, 0, 0],
              [0, 2, 5],
              [0, 0, -1]])
print(np.linalg.eigvals(A))  # 0, 2, -1

# (2) 하부삼각행렬
B = np.array([[4, 0, 0],
              [0, 0, 0],
              [1, 0, -3]])
print(np.linalg.eigvals(B))  # 4, 0, -3