import math

def solution(a, A, b, B):
    g = math.gcd(n := a * B + b * A, d := A * B)
    return [n // g, d // g]

print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))