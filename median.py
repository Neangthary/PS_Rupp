ls = [120, 50, 140, 120, 150, 150, 150, 65, 170, 250, 110]

lst= sorted(ls)
n = len(lst)
mid = (n//2)

if n%2:
    print(lst[mid])
    
else:
    print((lst[mid-1] + lst[mid])/2)

def median(ls):
    lst= sorted(ls)
    n = len(lst)
    mid = (n//2)
    return (lst[mid] if n%2 else (lst[mid-1] + lst[mid])/2)