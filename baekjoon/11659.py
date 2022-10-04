import sys

N, M = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))

psum = [0] * N
psum[0] = numbers[0]

for i in range(1,N):
    psum[i] = psum[i-1] + numbers[i]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())

    if start == 1:
        answer = psum[end-1]
    else:
        answer = psum[end-1] - psum[start-2]
    
    print(answer)
