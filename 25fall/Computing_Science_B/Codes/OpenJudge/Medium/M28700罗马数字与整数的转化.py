d1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
l1=['I','II','III','IV','V','VI','VII','VIII','IX']
l2=['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
l3=['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
l4=['M','MM','MMM']
def f(x):
    lst=list(x)
    a=0
    for i in range(len(lst)):
        if i<len(lst)-1 and d1[lst[i]]<d1[lst[i+1]]:
            a-=d1[lst[i]]
        else:
            a+=d1[lst[i]]
    return a
def g(x):
    b=''
    a1,a2,a3,a4=x//1000,x//100%10,x//10%10,x%10
    if a1!=0:
        b+=l4[a1-1]
    if a2!=0:
        b+=l3[a2-1]
    if a3!=0:
        b+=l2[a3-1]
    if a4!=0:
        b+=l1[a4-1]
    return b
s1=input()
if 'A'<s1[0]<'Z':
    print(f(s1))
elif int(s1[0])>0:
    print(g(int(s1)))


