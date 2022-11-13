
"""
Task score : 100%

중복되지 않는 최소 단위로 문자열 나누기

ex.
- cycle -> (cy,cle) or (c, ycle) : count 2
- world -> (world) : count 1
- dddd -> (d,d,d,d) : count 4
"""
def solution(S):

    if len(S) == len(set(S)):
        return 1
    
    count = 1
    letters = set()
    for char in S:
        if char in letters:
            letters.clear()
            count += 1
        letters.add(char)
    
    return count

print(solution("cycle"))
