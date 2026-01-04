n,k=map(int,input().split())
l=sorted(list(map(int,input().split())),reverse=True)
print(f'{sum(l)/k:.3f}')
