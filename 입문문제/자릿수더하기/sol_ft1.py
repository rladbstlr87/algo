def solution(n):
    answer = 0
    while n > 0:
        a, b = divmod(n, 10)
        answer = answer + b
        n = a
    return answer

print(solution(1234))
print(solution(930211))