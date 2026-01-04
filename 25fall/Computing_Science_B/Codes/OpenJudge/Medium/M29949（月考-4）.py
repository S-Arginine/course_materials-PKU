from collections import defaultdict
d=defaultdict(float)
N,M=map(int,input().split())
for i in range(N):
    a,b=map(int,input().split())
    d[a/b]+=b
v=0
for key in sorted(d.keys(),reverse=True):
    if M>0:
        c,e=M,d[key]
        M=max(0,c-e)
        d[key]=max(0,e-c)
        v+=key*(e-d[key])
print(f"{v:.2f}")