import sys,math
MAXP = 10**6
is_prime = [True]*(MAXP+1)
is_prime[0] = is_prime[1] = False
for p in range(2, int(math.isqrt(MAXP)) + 1):
    if is_prime[p]:
        is_prime[p*p: MAXP+1: p] = [False]*len(range(p*p, MAXP+1, p))
tprimes = {p*p for p, flag in enumerate(is_prime) if flag}
data = sys.stdin.read().split()
n = int(data[0])
nums = map(int, data[1:n+1])
out = []
for x in nums:
    out.append("YES" if x in tprimes else "NO")
sys.stdout.write('\n'.join(out))
