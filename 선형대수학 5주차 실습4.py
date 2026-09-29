from fractions import Fraction

def print_augment(title, matrix):
    """첨가행렬 [A|I]를 출력하는 함수"""
    print(f"{title}:")
    for row in matrix:
        left = " ".join(f"{str(x):>4}" for x in row[:2])
        right = " ".join(f"{str(x):>4}" for x in row[2:])
        print(f"[{left} | {right}]")

augmented = [
    [Fraction(3), Fraction(4), Fraction(1), Fraction(0)],
    [Fraction(2), Fraction(3), Fraction(0), Fraction(1)]
]

print_augment("Initial augmented matrix", augmented)

augmented[0]=[
    value/ 3 for value in augmented[0]
]

print_augment("1단계: (1/3)R1->R1", augmented)

augmented[1]=[
    augmented[1][i] - 2 * augmented[0][i] for i in range(4)
]

print_augment("2단계: R2-2R1->R2", augmented)

augmented[1]=[
    3*value for value in augmented[1]
]

augmented[0]=[
    augmented[0][j]- Fraction(4,3)*augmented[1][j] for j in range(4)
]

print_augment("4단계: R1-(4/3)R2->R1", augmented)

A_inverse = [
    row[2:] for row in augmented
]

print("A의 역행렬:")
for row in A_inverse:
    print([str(value) for value in row])