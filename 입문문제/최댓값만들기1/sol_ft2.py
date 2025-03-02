# 정렬 알고리즘을 구현해본다(버블정렬)

def solution(numbers):
    n = len(numbers)

    # .sort()를 아래처럼 구현할 수 있다
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers[-1] * numbers[-2]

print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))