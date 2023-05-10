num = int(input())

meet = [[0 for j in range(2)] for i in range(num)]

for i in range(num):
        a, b = map(int, input().split())
        meet[i][0] = b
        meet[i][1] = a

meet.sort()

print(meet)

end = 0
result = 0

for i in range(num):
    if(meet[i][1] >= end):
        result += 1
        end = meet[i][0]
        
print(result)
