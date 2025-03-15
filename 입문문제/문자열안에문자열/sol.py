def solution(str1, str2):
    for i in range(0, len(str1)):
        if str1[i : i+len(str2)] == str2:
            return 1
    return 2

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
print(solution("ppprrrogrammers", "pppp"))
print(solution("AbcAbcA", "AAA"))
