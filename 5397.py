from collections import deque
import sys

data_input = int(sys.stdin.readline())

for _ in range(data_input):

    left = []
    right = []
    password = input()

    for x in password:
        if x == ">":
            if right:
                  left.append(right.pop())
        elif x == "<":
            if left:
                right.append(left.pop())
        elif x == "-":
            if left:
                left.pop()
        else:
                left.extend(reversed(right))
    
    password = ''.join(left)
    print(password)