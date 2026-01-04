col,line1,line2=set(),set(),set()
l=[]
def f(x):
    if x==8:

        return l
    else:
        s=[]
        for i in range(8):
            if i not in col and x+i not in line1 and x-1 not in line2:
                s.append(i+1)
                col.add(i)
                line1.add(x+i)
                line2.add(x-i)
        f(x+1).append(s)
        return l
lst=sorted([int(''.join(list(map(str,j))))for j in f(0)])
n=int(input())
result=[]
for j in range(n):
    b=int(input())
    result.append(lst[b-1])
for j in result:
    print(j)