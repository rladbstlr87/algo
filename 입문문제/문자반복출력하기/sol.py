def solution(my_string, n):
    answer = ''
    for word in my_string:
        answer = answer + word * n
    return answer

print(solution('hello', 3))