def solution(num1, num2):
    answer = 0

    if num1 == num2:
        answer = 1
    else:
        answer = -1

    return print(answer)

solution(2, 3)
solution(11, 11)
solution(7, 99)