import sys
n=int(input())
l=[]
while n!=0:
    tian=sorted(list(map(int,sys.stdin.readline().strip().split())),reverse=True)
    king=sorted(list(map(int,sys.stdin.readline().strip().split())))
    t=-n
    for i in range(n):
        tian=sorted(tian[:i+1])+tian[i+1:]
        x=0
        for j in range(n):
            if tian[j]>king[j]:
                x+=1
            elif tian[j]<king[j]:
                x-=1
        if x>t:
            t=x
    l.append(t*200)
    n=int(input())
sys.stdout.write('\n'.join([str(i)for i in l])+'\n')