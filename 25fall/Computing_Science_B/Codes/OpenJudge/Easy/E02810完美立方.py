n=int(input())
result=[]
for a in range(2,n+1):
    for b in range(2,a+1):
        for c in range(2,b+1):
            for d in range(2,c+1):
                if a**3==b**3+c**3+d**3:
                    result.append((a,d,c,b))
result.sort(key=lambda x:x[3])
result.sort(key=lambda x:x[2])
result.sort(key=lambda x:x[1])
result.sort(key=lambda x:x[0])
for item in result:
    print(f'Cube = {item[0]}, Triple = ({item[1]},{item[2]},{item[3]})')