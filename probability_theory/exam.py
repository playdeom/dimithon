import random
import decimal
decimal.getcontext().prec=100
prob=25 # 문제 수
set=5 # n지 선다
rotation=1234567 # 시뮬레이션 횟수
f=open('get.txt','w',encoding='utf-8')
f.write(f'\n{rotation}번 시뮬레이션 결과\n\n')
arr=[0]*(prob+1)
for _ in range(rotation):
    cnt=0
    for i in range(25):
        if random.randint(1,set)==random.randint(1,set):
            cnt+=1
    arr[cnt]+=1
su=decimal.Decimal(sum(arr))
a=0
for i in arr:
    f.write(f'{a}개 맞을 확률 : {decimal.Decimal(i)/su*100}\n')
    print(f'{a}개 맞을 확률 : {decimal.Decimal(i)/su*100}')
    a+=1
f.close()