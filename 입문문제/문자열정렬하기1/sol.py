def solution(my_string):
    answer = []
    for char in my_string:
        if char.isdigit():
            answer.append(int(char))
    answer.sort()
    return answer

my_string1 = 'hi12392'
my_string2 = 'p2o4i8gj2'
my_string3 = 'abcde0'

print(solution(my_string1))
print(solution(my_string2))
print(solution(my_string3))