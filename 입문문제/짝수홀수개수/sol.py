def solution(num_list):
    answer1 = []
    answer2 = []
    for i in num_list:
        if i % 2 == 0:
            answer1.append(i)
        else:
            answer2.append(i)
    return len(answer1), len(answer2)

print(solution([1, 2, 3, 4, 5]))