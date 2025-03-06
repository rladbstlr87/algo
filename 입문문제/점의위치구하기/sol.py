def solution(dot):
    x, y = dot # dot = x, y와는 다르다
    if 0 < x and 0 < y:
        answer = 1
    elif 0 > x and 0 < y:
        answer = 2
    elif 0 > x and 0 > y:
        answer = 3
    else:
        answer = 4
    return answer

print(solution(2, 4))
print(solution(-7, 9))