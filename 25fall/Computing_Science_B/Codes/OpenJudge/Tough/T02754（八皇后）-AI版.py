col, linel, line2 = set(), set(), set()
results = []
def f(x,path):
    if x==8:
        results.append(''.join(map(str,path)))
        return
    for i in range(8):
        if i not in col and x+i not in linel and x-i not in line2:
            col.add(i)
            linel.add(x+i)
            line2.add(x-i)

            f(x+1,path+[i+1])

            col.remove(i)
            linel.remove(x+i)
            line2.remove(x-i)

f(0, [])

lst = sorted(results)

n = int(input())
for _ in range(n):
    b = int(input())
    print(lst[b - 1])
