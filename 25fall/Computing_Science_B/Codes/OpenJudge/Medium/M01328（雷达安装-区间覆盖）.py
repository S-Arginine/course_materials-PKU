from math import sqrt
t,result=0,[]
while True:
    t+=1
    n,d=map(int,input().split())
    if n==0 and d==0:
        break
    l,i=[],0
    while True:
        s=input()
        if not s:
            break
        else:
            a,b=map(int,s.split())
            l.append([a,b])
        l.sort()
        qujian=[]
    for i in range(n):
        if abs(l[i][1])>d:
            qujian=[]
            break
        else:
            if i==0:
                x1,y1=l[0][0]-sqrt(d**2-l[0][1]**2),l[0][0]+sqrt(d**2-l[0][1]**2)
                qujian.append([x1,y1])
            else:
                x2,y2=l[i][0]-sqrt(d**2-l[i][1]**2),l[i][0]+sqrt(d**2-l[i][1]**2)
                if x2>y1:
                    qujian.append([x2,y2])
                    x1,y1=x2,y2
                else:
                    x2,y2=max(x1,x2),min(y1,y2)
                    qujian[-1]=[x2,y2]
                    x1,y1=x2,y2
    if len(qujian)==0:
        result.append(f"Case {t}: -1")
    else:
        result.append(f"Case {t}: {len(qujian)}")
for i in result:
    print(i)


