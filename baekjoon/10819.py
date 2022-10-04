from itertools import permutations

N = int(input())
A = list(map(int,input().split()))

answer = -1
for p in permutations(A):

    sum = 0
    for j in range(1,N):
        sum += abs(p[j-1]-p[j])

    if answer < sum:
        answer = sum

print(answer)