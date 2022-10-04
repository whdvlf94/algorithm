N = int(input())
k = int(input())
  

def get_num_smaller(x: int) -> int:
    num_smaller = 0
    for i in range(1, N+1):
        #i번째 행에서 x보다 작은 수의 개수는 열의 인덱스와 동일(인덱스가 1부터 시작하기 떄문) 
        num_smaller += min(N, (x-1) // i)
    
    return num_smaller

def get_num_bigger(x: int) -> int:
    num_bigger = 0
    for i in range(1, N+1):
        num_bigger += N - min(N, x //  i)

    return num_bigger

low = 1
high = min(N*N, int(1e9))
answer = -1
while low <= high: 
    mid = (low + high) // 2

    num_smaller = get_num_smaller(mid)
    num_bigger = get_num_bigger(mid)
    
    if num_smaller > k-1: 
        high = mid - 1
    elif num_bigger > (N*N - k):
        low = mid + 1
    else:
        answer = mid
        break

print(answer)