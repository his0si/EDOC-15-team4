import sys
from itertools import permutations
#입력에서 길이가 주어진 모든 가능한 순열을 반환하는 함수

N = int(input())
num = list(permutations([1,2,3,4,5,6,7,8,9], 3))
#permutations(리스트, 길이)-순열
#combinations(리스트, 길이)-조합

test = strike_input = ball_input = map(int, input().split()) #정수
strike_cnt = ball_cnt = 0

test = list(str(test)) #테스트를 리스트로 변환
remove_cnt = 0 #remove_cnt 변수가 없을 경우 리스트에서 순열을 제거할 때, 리스트의 인덱스가 변하기 때문에 불편해짐

for _ in range(N):

    for i in range(len(num)):
        i -= remove_cnt 

        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num[i]:
                if j == num[i].index(test[j]):
                    strike_cnt = strike_cnt + 1
                else:
                    ball_cnt = ball_cnt+ 1
    
        if strike_cnt != strike_input or ball_cnt != strike_cnt:
            num.remove(num[i])
            remove_cnt += 1

print(len(num))