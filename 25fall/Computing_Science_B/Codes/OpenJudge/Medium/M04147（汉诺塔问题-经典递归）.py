import sys
l=input().split()
def move(x,a,b,c):
    result=[]
    if x==1:
        result.append(f'1:{a}->{c}')
    else:
        result+=move(x-1,a,c,b)+[f'{x}:{a}->{c}']+move(x-1,b,a,c)
    return result
sys.stdout.write('\n'.join(move(int(l[0]),l[1],l[2],l[3]))+'\n')
