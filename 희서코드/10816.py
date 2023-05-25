N = int(input())
card = list(map(int, input().split()))
M = int(input())
Mcard = list(map(int, input().split()))
ans = []

for i in range (M):
    ans[i]=0  # 리스트 초기화

card.sort()  # card 리스트 정렬(리스트 내장 함수)

for i in range(M):
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if card[mid] == Mcard[i]:
            ans[i] += 1
            break
        elif card[mid] < Mcard[i]:
            left = mid + 1
        else:
            right = mid - 1

print(*ans)  #print(*ans)는 ans 리스트의 요소들을 공백으로 구분하여 출력
