from sys import stdin
import sys
from itertools import combinations

N = int(input())
garden = []
for _ in range(N):
    garden.append(list(map(int, stdin.readline().split())))


