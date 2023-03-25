from collections import deque

N = int(input())
result = deque(map(int, input().split()))
cardskills = deque(range(1, N))

for i in range(N):
    if cardskills[N] == 1:
        result.appendleft(i+1)
    elif cardskills[N] == 3:
        result.append(i+1)

print(result)