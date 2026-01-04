from collections import deque
k=list(input())
keyword=[]
for i in range(len(k)):
    if k[i]=='j':
        k[i]='i'
    if k[i] not in keyword:
        keyword.append(k[i])
for i in range(97,123):
    if chr(i)!='j':
        if chr(i) not in keyword:
            keyword.append(chr(i))
matrix=[[0]*5 for i in range(5)]
n=0
d=dict()
for i in range(5):
    for j in range(5):
        if n<len(keyword):
            d[keyword[n]]=(i,j)
            matrix[i][j]=keyword[n]
            n+=1
def f(x):
    while x>=5:
        x-=5
    return x
n=int(input())
result=[]
for i in range(n):
    string=deque(input())
    for j in range(len(string)):
        if string[j]=='j':
            string[j]='i'
    s=[]
    r=[]
    while string:
        if len(string)==1:
            st=(string[0],'x') if string[0]!='x' else (string[0],'q')
            s.append(st)
            string.popleft()
        else:
            a,b=string[0],string[1]
            if a==b:
                sm='x' if a!='x' else 'q'
                D=string.popleft()
                string.appendleft(sm)
                string.appendleft(D)
            else:
                s.append((a,b))
                string.popleft()
                string.popleft()
    for j in s:
        if d[j[0]][0]==d[j[1]][0]:
            r.append(matrix[d[j[0]][0]][f(d[j[0]][1]+1)])
            r.append(matrix[d[j[1]][0]][f(d[j[1]][1]+1)])
        elif d[j[0]][1]==d[j[1]][1]:
            r.append(matrix[f(d[j[0]][0]+1)][d[j[1]][1]])
            r.append(matrix[f(d[j[1]][0]+1)][d[j[1]][1]])
        else:
            r.append(matrix[d[j[0]][0]][d[j[1]][1]])
            r.append(matrix[d[j[1]][0]][d[j[0]][1]])
    result.append(''.join(r))
for i in result:
    print(i)