def solution(dot):
    quad = [(3, 2), (4, 1)]
    return quad[dot[0] > 0][dot[1] > 0]

# 불리언 인덱싱
# 인덱스 값 안에 조건문이 들어가면 true, false 즉, 1과 0으로 반환하고 이를 인덱스를 찾아가는 숫자로 사용할 수 있다