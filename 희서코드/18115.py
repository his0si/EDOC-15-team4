from collections import deque

N = int(input())
initial = deque(map(int, input().split()))
cardskills = deque(range(1, N))

for i in range(N):
    if cardskills[N] == 1:
        result.appendleft(i+1)
    elif cardskills[N] == 2:
        result.n.pop
        #result.2.pop
        #result.append(2)
        '''그....파이썬에선 n.pop?을 사용하면 배열에서 포인터처럼 특정 값에 접근해서 중간 값을 빼 올 수 있다고 하셨는데....
        이걸 사용하면 더 이상 덱으로 문제를 푸는게 아닌가요...?
        18115이 덱 문제인데 첫번 째랑 마지막은 append로 하면 되는데 가운데는.....? 원형큐...? 그걸 쓰는 건가요...?ㅜㅜㅜㅜㅜㅜ
        위에서 두번째꺼니까  n=2를 넣고 싶은데 n=2를 넣으니까 오류가 나요...왠지는 모르겠어요...n.pop에 문자 말고 숫자 쓰면 에러 뜨나요?'''
        
    elif cardskills[N] == 3:
        result.append(i+1)

print(result)
