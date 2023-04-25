import math

ls = [120, 50, 140, 120, 150, 150, 150, 65, 170, 250, 110]
mean = sum(ls)/len(ls)
lst = []
for i in ls:
    lst.append((i-mean)**2)
sum_square_deviation= sum(lst)
print(sum_square_deviation)
sample_variance= sum_square_deviation/ (len(ls)-1)
##sample_standard_deviation
sdv = math.sqrt(sample_variance)

mean = sum(ls)/len(ls)
sv = sum([(i-mean)**2 for i  in ls])/(len(ls)-1)
sdv = math.sqrt(sv)
print(sv)

