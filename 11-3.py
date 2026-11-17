import numpy as np

A = np.array([[3, -1, -1],
              [-12, 0, 5],
              [4, -2, -1]])

# MATLAB: [X, lamda] = eig(A)
lamda, X = np.linalg.eig(A)

print(X)               # 고유벡터 (각 열이 하나의 고유벡터)
print(np.diag(lamda))  # 고유값을 대각행렬로 (MATLAB의 lamda와 같은 형태)