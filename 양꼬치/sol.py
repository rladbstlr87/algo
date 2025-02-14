def solution(n, k):
    yang = 12000
    drink = 2000
    answer = yang * n + drink * k
    if n // 10 >= 1: # 몫을 구하면 (몫 * k)를 빼면 해결됨
        answer = answer - n // 10 * drink
    else:
        answer = answer
    return answer

print(solution(10, 3))
print(solution(64, 6))