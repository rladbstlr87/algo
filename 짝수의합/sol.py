def solution(n):
    n = 0
    # n은 for i in range(0: (n + 1) % 2): 의 합 근데 for 안에 if들어가야될거같음
    # 아닌가 if 안에 for 들어가야되나
    # n을 어떻게 리스트로 풀어서 반환해야 하는가
    for n in range(n + 1): # << n이 아니라 i를 입력했어야햇다
    # 반환한 리스트를 어떻게 합산하는가
        n = sum(range((n + 1) % 2))

    return answer