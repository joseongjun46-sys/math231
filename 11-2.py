import numpy as np

A = np.array([[3, 2],
              [3, -2]])

# MATLAB: [X, lamda] = eig(A)
lamda, X = np.linalg.eig(A)

print(X)               # 고유벡터 (각 열이 하나의 고유벡터)
# [[ 0.8944 -0.3162]
#  [ 0.4472  0.9487]]

print(np.diag(lamda))  # 고유값을 대각행렬로 (MATLAB의 lamda와 같은 형태)
# [[ 4.  0.]
#  [ 0. -3.]]