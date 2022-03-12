N, K = map(int,input().split())

coin_list: list = []
for i in range(N):
    coin_value = int(input())
    if coin_value <= K:
        coin_list.append(coin_value)

result = 0
for i in list(reversed(coin_list)):
    share,remainder = divmod(K,i)
    result += share
    if remainder > 0:
        K = remainder
    else:
        break
print(result)
