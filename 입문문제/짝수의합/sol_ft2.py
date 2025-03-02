def solution(n):

    for i in range(2, n+1, 2):
        answer += i

    return answer

print(solution(10))
print(solution(4))