from sys import stdin
import sys
import math

input = int(input())

for _ in range(input):
    N, M = map(int, stdin.readline().split())  #입력
    for _ in range(input):
        answer = math.factorial(M)/(math.factorial(N)*math.factorial(M-N)) #조합을 사용한 방법
    print(int(answer))