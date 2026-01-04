k = int(input())
h = list(map(int, input().split()))
f = [1] * k
for i in range(k):
    for j in range(i):
        if h[j] >= h[i]:
            f[i] = max(f[i], f[j] + 1)
print(max(f))
