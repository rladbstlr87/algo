# 숫자 오름차순으로 정렬을 하면 가장 큰 두 숫자를 골라낼 수 있고 그 숫자들을 곱하면 최댓값이 될거다
def solution(numbers):
    numbers.sort()

    return numbers[-1] * numbers[-2]
#       맨뒤:가장큰숫자 * 맨뒤에서두번째:두번째로큰숫자
print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))