import math
s=input()
m=int(math.log(len(s),2))
left,right=0,m
result=[]
while left<right:
    result.append(s[int(2**left)-1])
    result.append(s[int(2**right)-1])
    left+=1
    right-=1
if left==right:
    result.append(s[int(2**left)-1])
print(''.join(result))