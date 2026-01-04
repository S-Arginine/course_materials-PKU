def f(x):
    a=list(map(int,x.split()))
    b=a[0]*100+a[1]
    return b
def g(x):
    c,d=x//100,x%100
    return str(c)+' '+str(d)
n=int(input())
num_dict={}
num_set=set()
for i in range(1,n+1):
    data_list=input().split()
    date_str=' '.join(data_list[1:])
    num_set.add(f(date_str))
    if date_str in num_dict:
        num_dict[date_str].append(data_list[0])
    elif date_str not in num_dict:
        num_dict[date_str]=[data_list[0]]
for p in sorted(num_set):
    if len(num_dict[g(p)])>1:
        print(g(p),' '.join(num_dict[g(p)]))
