import numpy as np

A = np.array([[2, 3],
              [3, -6]])

# 특성다항식의 계수 (MATLAB: poly(A))
print(np.poly(A))            # [  1.   4. -21.]  →  λ² + 4λ − 21

# 고유값 (MATLAB: eig(A))
print(np.linalg.eigvals(A))  # [ 3. -7.]