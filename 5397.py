from collections import deque
data_input = int(input())

for _ in range(test_cases):
    left = []
    right = []
    password = input()

    for x in password:
        if x == ">":
            if right:
                right.append(right.pop()) 
        elif x == "<":
            if left:
                left.append(left.pop())
        elif x == "-":
            if left:
                left.pop()


    print(password)