from sys import stdin
import sys
#이걸 하면 일반 input() 입력보다 빨라진다는 걸 주워 들었는데 정확히 뭔진 잘 모르겠어요...
#맨날 시간초과 뜨고 이 문제는 2차원 리스트라 많은 값 입력 받으니까 한번 써봤어요....

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, stdin.readline().split())))  #입력

StartTeam=0
LinkTeam=0

exist = [False] * (N + 1) #스타트팀인지 링크 팀인지 구분, 여기에서 초기화
result=0

def teamfuction(): 
    global result #얘 이렇게 쓰는 건지 모르겠는데 이거 전역변수로 강제 변환? 시켜주는 건가요?
    #그냥 C에서는 메인 함수에서 모든 변수 선언하면 딱히 문제 없었는데 뭔가 변수...쪽에서 자꾸 문제가 나요...
    #메인 함수라고 불러야 하는지는 모르겠지만 걍 바깥에다가 선언했는데 왜 전역변수...가 안되는거죠...
    #지역 변수는 i랑j만 쓸려고 나머지는 다 밖에다 선언(?)했는데...<-근데 파이썬은 선언...안해도 되지 않나요..?

    for i in range(N): 
            for j in range(N): 
                if exist[i] and exist[j]: 
                    StartTeam = StartTeam + (S[i][j] + S[j][i]) #브루트포스(?)로 풀었어요..그냥 냅따 for문 돌리면서 모든 경우 다 찾는 거..
                else: 
                    LinkTeam = LinkTeam + (S[i][j] + S[j][i]) 
        
    result = min(result, abs(StartTeam - LinkTeam)) 

teamfuction()
print(result)

#UnboundLocalError는 for, while, if 안에서 선언된 변수를 바깥에서 쓸려고 할 때 생기는 문제라고 해서
#앞에서 변수 선언을 다 하고 초기화도 다 해줬는데도 뜹니다...뭐가...문제일까요...
