ls = [55, 46, 64, 49, 56, 70, 45, 52]

mean = sum(ls)/len(ls)
lst = []
for x in ls:
    lst.append(x - mean)
print(lst)

def deviation_from_mean(ls):
    mean = sum(ls)/len(ls)
    dvm= [x-mean for x in ls]
    return(dvm)

print(deviation_from_mean(ls))
