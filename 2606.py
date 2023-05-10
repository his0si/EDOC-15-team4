import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
link=[[0]*(n+1) for _ in range(n+1)]
visit=[0]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    link[a][b]=link[b][a]=1

def dfs(v):
    visit[v]=1
    for i in range(1,n+1):
        if link[v][i]==1 and visit[i]==0:
            dfs(i)

dfs(1)

count=0

for i in range(2,n+1):
    if visit[i]==1:
        count+=1
print(count)