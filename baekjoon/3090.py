
N, T = map(int, input().split())
A = list(map(int, input().split()))

def count_operation(diff: int) -> int:
# 차이를 x 이하로 만들기 위해 필요한 연산(1을 감소시키는)의 횟수를 구함
    B = [A[i] for i in range(N)]

    count = 0
    for i in range(N-1):
        if B[i] + diff < B[i+1]:
            count += B[i+1] - B[i] - diff
            B[i+1] = B[i] + diff

    for i in range(N-1,0,-1):
        if B[i] + diff < B[i-1]:
            count += B[i-1] - B[i] - diff
            B[i-1] = B[i] + diff

    return count

low = 0
high = int(1e9)
answer = -1

while low <= high:
    mid = (low + high) // 2

    if count_operation(mid) <= T:
        answer = mid
        high = mid -1
    else:
        low = mid + 1

for i in range(N-1):
    if A[i] + answer < A[i+1]:
        A[i+1] = A[i] + answer

for i in range(N-1,0,-1):
    if A[i] + answer < A[i-1]:
        A[i-1] = A[i] + answer

print(" ".join(list(map(str,A))))