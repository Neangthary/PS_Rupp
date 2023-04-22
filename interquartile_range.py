import math

ls = [18, 18, 25, 19, 23, 20, 69, 18, 21, 18, 20, 18,18,20, 18, 19, 28, 17, 18, 18]
# find sample deviation
mean = sum(ls)/len(ls)
# append in list
lst =[]
for i in ls:
    # pow(i,2)
    lst.append((i-mean)**2)
print(lst)
sum_square_deviation = sum(lst)
print(sum_square_deviation)
sample_variance = sum_square_deviation/(len(ls)-1)
# standard deviationn
adv = math.sqrt(sample_variance)
print(sample_variance)

# or
mean = sum(ls)/len(ls)
sv = sum([(i-mean)**2 for i in ls])/(len(ls)-1)
print(sv)

# interquartile 

ls = [18, 18, 25, 19, 23, 20, 69, 18, 21, 18, 20, 18,18,20, 18, 19, 28, 17, 18, 18]
# print(lst[3])

def median(ls):
    lst = sorted(ls)
