N = int(input())

while True:
    time_list = list(map(int,input().split()))
    if N == len(time_list):
        break

sorted_time_list = sorted(time_list)
waiting_time: int = 0
for i in range(len(sorted_time_list)):
    waiting_time += sorted_time_list[i]*(N-int(i))

print(waiting_time)