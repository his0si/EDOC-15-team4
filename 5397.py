from collections import deque

N, K = map(int, input().split())

d = deque()
new = []

for i in range(1, N+1):
    d.append(i)

while len(d) != 0:
    for i in range(K-1):
        a = d.popleft()
        d.append(a)
    
    a = d.popleft()
    new.append(a)

print('<', end='')

for i in range(N):
    print(int(new[i]), end='')
    if i != N-1:
        print(', ',end='')

print('>')