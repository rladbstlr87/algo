def solution(numbers):
    answer = 0
    total = 0
    i = 0

    for number in numbers:
        # 뭐시기 하고
        total += number
        # 더하고
        i += 1
# 나누고
    answer = total / i

    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))