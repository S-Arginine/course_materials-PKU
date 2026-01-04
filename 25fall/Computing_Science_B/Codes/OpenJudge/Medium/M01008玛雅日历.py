n=int(input())
l=[]
d1={'pop':1,'no':2,'zip':3,'zotz':4,'tzec':5,'xul':6,'yoxkin':7,'mol':8,'chen':9,'yax':10,
    'zac':11,'ceh':12,'mac':13,'kankin':14,'muan':15,'pax':16,'koyab':17,'cumhu':18,'uayet':19}
l1=['imix','ik','akbal','kan','chicchan','cimi','manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib','caban','eznab','canac','ahau']*13
l2=[str(i) for i in range(1,14)]*20
def g(x):
    return l2[x-1]+' '+l1[x-1]
for i in range(n):
    haab=input()
    date,mon,year=int(haab.split('.')[0]),d1[haab.split('.')[1].split()[0]],int(haab.split('.')[1].split()[1])
    days=date+1+(mon-1)*20+year*365
    yearr=days//260
    if days%260==0:
        tzolkin=g(days%260)+' '+str(yearr-1)
    else:
        tzolkin=g(days%260)+' '+str(yearr)
    l.append(tzolkin)
print(n)
for i in l:
    print(i)


