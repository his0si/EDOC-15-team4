import sys
from collections import deque

n = int(sys.stdin.readline())
people =deque([i for i in range(1,n+1) ])
#원으로 앉아 있으니까 원형큐?

