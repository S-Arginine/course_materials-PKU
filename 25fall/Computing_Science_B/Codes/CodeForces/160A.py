n=int(input())
l=sorted(list(map(int,input().split())),reverse=True)
a,b=0,0
while b<=sum(l):
    a+=1
    b+=l[0]
    del l[0]
print(a)



