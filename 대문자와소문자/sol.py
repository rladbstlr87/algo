def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer

my_string1='cccCCC'
my_string2='abCdEfghIJ'
print(solution(my_string1))
print(solution(my_string2))