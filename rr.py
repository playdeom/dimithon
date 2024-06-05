n=int(input("처리할 작업의 개수를 *정수로 입력하세요\n>>"))
arr=[]
for i in range(n):
    print(f'{i+1}번 작업 : ')
    s,t=map(int,input("작업의 시작시간과 실행시간을 *공백으로 정수를 입력하세요\n>>").split())
    arr.append([i+1,s,t,0,s]) #번호, 시작시간, 작업시간, 대기된 시간, 시작 저장
arr.sort(key=lambda x:x[1])
print(arr)
wait=[[0,0] for i in range(n)]
av_time, av_end=0,0
def round_robin():
    global arr,wait,av_end,av_time,n
    q=int(input("구간실행시간을 *정수로 입력하세요\n>>"))
    now=0
    av_time, av_end=0,0
    qq=[]
    qq.append(arr[0])
    check=[0]*(n+1)
    check[1]=1
    while len(qq):
        i,a,b,c,d=qq.pop(0)
        print(f'P{i}. 현재 시간 {now}, 추가될 시간 {b}')
        if b<=q:
            save=max(now-a,0)+c
            wait[i-1][0]=save
            av_time+=save
            now+=b
            wait[i-1][1]=now-d
            av_end+=now-d
            continue
        if now-a>0:c+=now-a
        now=max(now+q,a+q)
        a=now
        b-=q
        for ii,aa,bb,cc,dd in arr:
            if aa<=now and check[ii]==0:
                qq.append([ii,aa,bb,cc,dd])
                check[ii]=1
        qq.append([i,a,b,c,dd])
def fifo():
    global arr,wait,av_time,av_end
    now=0
    av_time,av_end=0,0
    while len(arr):
        i,a,b,c,d=arr.pop(0)
        print(f'P{i}. 남은 실행시간 {b}, 현재 시간 {now}')
        wait[i-1][0]=now-a
        av_time+=now-a
        now+=b
        wait[i-1][1]=now-d
        av_end+=now-d
def sjt():
    global arr,wait,av_end,av_time
    now=0
    av_time,av_end=0,0
    class cmp:
        def __init__(self,i,a,b,c,d):
            self.i=i
            self.a=a
            self.b=b
            self.c=c
            self.d=d
        def __lt__(self, other):
            if self.b==other.b:
                return self.a<other.a
            return self.b<other.b
    import heapq
    pq=[]
    it=iter(arr)
    heapq.heappush(pq,cmp(next(it)))
    while len(pq):
        i,a,b,c,d=heapq.heappop(pq)
        wait[i-1][0]=now-a
        now+=b
        wait[i-1][1]=now-d
        while 1:
            save=next(it)
            if now>=save[1]:heapq.heappush(pq,cmp(save))
            else:break

# fifo()
round_robin()
# sjt()
print(f'작업\t\t대기시간\t반환시간')
for i in range(n):
    print(f"P{i+1}\t\t{wait[i][0]}\t\t{wait[i][1]}")
print(f'평균 대기시간 : {av_time/n}, 반환시간 : {av_end/n}')
