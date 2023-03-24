from collections import deque
from sys import stdin
import sys

N = int(input())
skill = list(map(int, stdin.readline().split()))
##반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않는다
card = deque([i+1 for i in range(N)])
real = [0]*N

new = deque()

for i in range (N):
    if skill[i] == 1:
        new.appendleft(card.popleft())
    
    elif skill[i] == 3:
        new.appendleft(card.pop())

    else:
        a = card.popleft()
        new.appendleft(card.popleft())
        card.appendleft(a)
    

for i in range (N):
    real[new[i]-1] = i+1

print = sys.stdout.write

print(" ".join(map(str, real)) + "\n")