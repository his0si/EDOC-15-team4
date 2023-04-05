N = int(input())
hill = list(map(int, input().split()))

count = 0
me = 0 #내 봉우리
answer = -1 #초기값은 0보다 작게 설정

for i in hill:
    if i > me:
        me = i
        count = 0
    else:
        count = count + 1 # 내 봉우리보다 커지는 순간까지 카운트한다.

# [3 2 1] 처럼 마지막까지 작아진 경우(더 이상 커진 경우가 없을 경우, for문의 if에 안 걸림)
answer = max(count, answer)
        
print(count)