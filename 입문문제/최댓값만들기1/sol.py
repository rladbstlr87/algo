def solution(num_list):
    num_list.sort()
    return num_list[-1] * num_list[-2]

print(solution([0, 31, 24, 10, 1, 9]))