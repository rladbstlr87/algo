# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
# 제한사항 : 0 ≤ n ≤ 1,000,000
# 입출력 예

def solution(n):
    n = list(map(int, str(n))) # n 을 리스트로 형변환
    for number in n:
        sum(number)
print(solution(n))

    #완성안됐음!!!
# print(solution(1234))
# print(solution(930211))