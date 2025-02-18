# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    numbers = []

    for char in my_string:
        if char.isdigit():
            numbers.append(int(char))
    
    return sum(numbers)

print(solution('aAb1B2cC34oOp'))
print(solution('1a2b3c4d123'))