def solution(money):
    answer = [money // 5500, money % 5500]
    return answer

print(solution(5500))
print(solution(15000))