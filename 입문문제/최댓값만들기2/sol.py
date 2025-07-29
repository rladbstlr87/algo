def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])


numbers1 = [1, 2, -3, 4, -5]
numbers2 = [0, -31, 24, 10, 1, 9]
numbers3 = [10, 20, 30, 5, 5, 20, 5]