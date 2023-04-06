import math
ls = [250, 300, 500, 650, 700, 800, 900, 1000, 1200, 1500]
#input salary_IT = 2000
def mean(ls):
    return(sum(ls)/len(ls))

def standard_deviation(ls):
    Mean = sum(ls)/len(ls)
    return(math.sqrt(sum([(u-Mean)**2 for u in ls])/(len(ls)-1)))

def z_score(ls):
    value = int(input("Please input your salary:"))
    z_score = (value-mean(ls))/standard_deviation(ls)
    return z_score

print(z_score(ls))

