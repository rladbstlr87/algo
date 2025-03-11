def solution(sides):
    max_side = max(sides)
    sides.remove(max(sides))
    if max_side < sum(sides):
        return 1
    else:
        return 2

print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))