l=input().split()
stack=[]
l.reverse()
for i in l:
    if i>'/':
        stack.append(i)
    else:
        a=stack.pop()
        b=stack.pop()
        if i=='+':
            stack.append(str(float(a)+float(b)))
        elif i=='-':
            stack.append(str(float(a)-float(b)))
        elif i=='*':
            stack.append(str(float(a)*float(b)))
        elif i=='/':
            stack.append(str(float(a)/float(b)))
print(f'{float(stack[0]):.6f}')