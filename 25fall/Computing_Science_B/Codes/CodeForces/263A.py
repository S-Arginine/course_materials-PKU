matrix=[input().split() for _ in range(5)]
def index(x,y):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j]==y:
                return [i,j]
a=index(matrix,'1')[0]
b=index(matrix,'1')[1]
print(abs(a-2)+abs(b-2))

