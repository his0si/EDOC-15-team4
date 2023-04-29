from sys import stdin
import sys

N, M = map(int, input().split())
Maze = []
for _ in range(N):
    Maze.append(list(map(int, stdin.readline().split())))  #입력
    
dp = [[0 for c in range(M)] 
for r in range(N)] # Dynamic Programming 리스트 초기화

