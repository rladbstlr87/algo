import bisect

def solution(array, height):
    sorted(array)
    indexed = bisect.bisect_right(array, height)

    return len(array) - indexed
print(solution([149, 180, 192, 170], 167))