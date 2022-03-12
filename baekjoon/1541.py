N = input()

s = 0
arr = N.split('-')

#내 답안
for i in range(len(arr)):
    if i == 0:
        for j in arr[i].split('+'):
            s += int(j)
    else:
        for j in arr[i].split('+'):
            s -= int(j)
print(s)

#좋은 답안
s = 0
parsed_list = [sum(map(int, i.split('+'))) for i in arr]
s = parsed_list[0]*2 - sum(parsed_list)
print(s)