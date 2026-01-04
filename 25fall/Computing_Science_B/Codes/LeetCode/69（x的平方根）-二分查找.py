import bisect
x=int(input())
l=[i*i for i in range(2**16)]
n=bisect.bisect_right(l,x)-1
print(n)
