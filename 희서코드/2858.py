R, B = map(int, input().split())

#R=L*W-(L-2)*(W-2)
#B=(L-2)*(W-2)

LpW = (R + 4) // 2 #L+W
LW = R + B #L*W

for i in range(1, LpW):
    if (LpW - i) * i == LW:
        print(max(i, LpW-i), min(i, LpW-i))
        break

#변수가 2개인 식은 풀 수 X
#전개해서 lvalue에 변수 하나만 남기기!!
