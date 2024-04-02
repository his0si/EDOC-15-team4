P, K = map(int, input().split())
a = True

for i in range(2,K):
    if P % i == 0:
        print('BAD', i)
        a = False
        break
if a:
    print('GOOD')
    
#두 소수는 K보다 커야 하기 때문에 어떠한 수로도 나누어 떨어지면 X
