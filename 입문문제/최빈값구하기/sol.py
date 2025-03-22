from collections import Counter

def solution(array):
    answer = []
    count = Counter(array)
    for k, v in count.items():
        if v == max(count.values()):
            answer.append(k)
    if len(answer) > 1:
        return -1
    else:
        return answer[0]