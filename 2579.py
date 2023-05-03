N=int(input())

stairs=[int(input()) for _ in range(N)] # 계단 리스트 입력 받기6
dp=[0]*(N) # dp 리스트

if len(stairs)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(stairs))

else: # 계단이 3개 이상일 때
    dp[0]=stairs[0] # 첫째 계단 수동 계산
    dp[1]=stairs[0]+stairs[1] # 둘째 계단까지 수동 계산
    for i in range(2,N): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    print(dp[-1])