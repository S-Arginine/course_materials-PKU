from collections import defaultdict
s=input()
d=defaultdict(int)
for i in range(len(s)//5):
    d[s[5*i]]=int(s[5*i+3])
print(d['a'],d['b'],d['c'])
