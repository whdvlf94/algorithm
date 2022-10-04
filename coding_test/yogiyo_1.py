
def solution(S):
    if "ba" in S:
        return False
    elif len(set(S)) == 1:
        if next(iter(S)) == "b":
            return False
    return True

N = 'b'
print(solution(N))