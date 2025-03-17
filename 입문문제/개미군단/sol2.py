def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        div, hp = divmod(hp, ant)
        answer += div
    return answer