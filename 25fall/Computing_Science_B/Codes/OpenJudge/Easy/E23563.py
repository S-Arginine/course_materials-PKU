lst=list('+'+input()+'*')
l=[]
for i in range(len(lst)):
    if lst[i]=='+':
        if lst[i+1]=='0':
            lst[i+3]='0'
    if lst[i]=='^':
        k=1
        s=[]
        while '0'<=lst[i+k]<='9':
            s.append(lst[i+k])
            k+=1
        l.append(int(''.join(s)))
if '^' not in lst:
    l.append(0)
print('n^'+str(max(l)))



