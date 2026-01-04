import sys
s=sys.stdin.readline().strip()
a=s[0]
l=[s[0]]
for i in s:
    if i!=a:
        a=i
        l.append(a)
n=len(l)
if l[0]=='0':
    if n%2==0:
        print(n-1)
    else:
        print(n)
else:
    if n%2==0:
        print(n)
    else:
        print(n-1)