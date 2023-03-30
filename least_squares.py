def mean(ls):
    return (sum(ls)/len(ls))

x=[11,15,19,23,27]
y=[150,270,450,580,740]

dx = [i-mean(x) for i in x]
dy = [i-mean(y) for i in y]
sum_dxdy= sum([round((dx[i]*dy[i]),2) for i in range(0,len(x))])
square_deviation = [(i-mean(x))**2 for i in x]
b = sum_dxdy/sum(square_deviation)
print(b)

a = mean(y)-(b*mean(x))
x = int(input("Please input days after injection of cancer cells:"))
y = a +(b*x)
print(y)







    

