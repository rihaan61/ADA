# Algorithm: Definition-based Matrix Multiplication
#
# Input: Two n x n matrices A and B
# Output: n x n matrix C = A x B
#
# for i = 0 to n-1:
#     for j = 0 to n-1:
#         C[i][j] = 0
#         for k = 0 to n-1:
#             C[i][j] += A[i][k] * B[k][j]
# return C
# ---------------------------------------------


def matrix_multiplication(A, B):
    n = len(A)
    # Compute C using list comprehension
    C = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return C

# ---------------- Main Program ----------------
n = int(input("Enter size of matrix n: "))

print("Enter matrix A row by row:")
A = [list(map(int, input().split())) for _ in range(n)]

print("Enter matrix B row by row:")
B = [list(map(int, input().split())) for _ in range(n)]

C = matrix_multiplication(A, B)

print("Matrix C = A x B is:")
for row in C:
    print(*row)
