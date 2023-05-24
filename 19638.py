import sys, heapq #힙
input = sys.stdin.readline

n, h, t = map(int, input().split())
giants = [-int(input()) for _ in range(n)]
heapq.heapify(giants)
cnt = 0
ㅌ
for i in range(t):
    if -giants[0] == 1 or -giants[0] < h:
        break
    else:
        heapq.heapreplace(giants, -(-giants[0] // 2))
        cnt = cnt + 1

if -giants[0] >= h:
    print('NO', -giants[0], sep='\n')
else:
    print('YES', cnt, sep='\n')