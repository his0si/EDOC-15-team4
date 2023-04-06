N=int(input())

stairs = list(map(int, input().split()))

for _ in range(N):
    dp=[[0]*(N+1)]