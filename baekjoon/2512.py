
#4
#120 110 140 150
#485
N = int(input())
requests = list(map(int, input().split()))
max_budget = int(input())

low = 0
high = max(requests)

def budget_sum(mid: int):
    
    budget_sum = 0
    for request in requests:
        budget_sum += min(request,mid)

    return budget_sum

upper_limit = -1
while low <= high:
    mid = (high + low) // 2
    
    if budget_sum(mid) <= max_budget:
        upper_limit = mid
        low = mid + 1
    else:
        high = mid - 1

answer = -1
for request in requests:
    min_vaule = min(request,upper_limit)
    answer = max(answer, min_vaule)

print(answer)

