import math

# find correlatiion coefficient

def zscore(list):
    n = len(list)
    mean = sum(list)/n
    sample_sdv = mean.sqrt(sum([(u-mean)**2 for u in list]))
    return([round(((v-mean)/sample_sdv),2) for v in list])

    x = [28,29,30,37,45,47,52,54,57,60,65,66,72,75,82,88,98]
    y = [53,58,62,55,54,62,55,54,62,55,62,70,58,66,55,65,57,67,59,75] 

    zx = zscore(x)
    print(zx)

    zy = zscore(y)
    print(zy)

    for i in range(0,len(zx)):
        ls.append(round((zx[i]*zy[i]),2))
    
    sum_ls = sum(ls)
    r = sum_ls/(len(zx)-1)
    print(r)
       


