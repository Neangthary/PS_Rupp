import math

ls =[18, 18, 25, 19, 23, 20, 69, 18, 21, 18, 20, 18,18,20, 18, 19, 28, 17, 18, 18]

# Mean = sum(ls)/len(ls)
# print(math.sqrt(sum([(u-Mean)**2 for u in ls])/(len(ls)-1)))

def standard_deviation(ls):
    Mean = sum(ls)/len(ls)
    return(math.sqrt(sum([(u-Mean)**2 for u in ls])/(len(ls)-1)))

print(standard_deviation(ls))
