"""
Task score : 66%

performance test cases
Passed 1 out of 4

리스트 속성 값들로 둘러쌓인 원에서 인접한 속성 값의 쌍의 합이 짝수인 것들 구하기
(단, 이미 한 쌍에 속한 속성 값은 중복해서 사용할 수 없음)

ex)
S = [4,2,5,8,7,3,7]
-> (S[0],S[1]), (S[4],S[5]) or (S[0],S[1]), (S[5],S[6]) : count 2
"""
def solution(S):

    count = 0
    belong_to_other_pair = set()
    for i in range(1,len(S)):
        
        if (i-1) in belong_to_other_pair:
            continue
        
        if (S[i-1]+S[i])%2 == 0:
            belong_to_other_pair.add(i)
            count += 1

        if i == (len(S)-1) and i not in belong_to_other_pair:
            if (S[i]+S[0])%2 == 0:
                count += 1

    return count


S = [4, 2, 5, 8, 7, 3, 7]

print(solution(S))