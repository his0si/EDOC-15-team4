import sys
input = sys.stdin.readline

N , M = map(int, input().split())
tree = list(map(int, sys.stdin.readline().split()))
sum=0

tree.sort() 

left=tree[0]
right=tree[N-1]
mid=(left+right)//2

for i in tree: #벌목된 나무 총합
    if i >= mid:
        sum = sum + i - mid

if sum >= M: #벌목 높이를 이분탐색
    left = mid + 1
else:
    right = mid - 1

print(right)