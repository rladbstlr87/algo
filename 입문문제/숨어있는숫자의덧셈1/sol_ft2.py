def solution(my_string):
    answer = 0

    for char in my_string:
        if not (ord('A') <= ord(char) <= ord('z')): # not 글자 인가요? -> 숫자인가요?
            answer += int(char)
    
    return answer

print(solution('aAb1B2cC34oOp'))
print(solution('1a2b3c4d123'))