def percentile(arr,p):
    n = len(arr)
    arr.sort()
    pos = (p*(n+1))/100
    k = int(pos)

    if pos == k:
        return arr[k-1]
    else:
        f = pos - k
        if k>=len(arr):
            return arr[-1]
        return arr[k-1] + f*(arr[k]- arr[k-1])
arr = [-100,10, 12, 11, 13, 12, 14, 55, 80]
print(percentile(arr,p = 45.2312))

def outliers(arr):
    q1 = percentile(arr,25)
    q3 = percentile(arr,75)
    iqr = q3 - q1
    lb = q1 - 1.5*iqr
    ub = q3 + 1.5*iqr
    res = []
    for i in arr:
        if i < lb or i > ub:
            res.append(i)

    if res:
        return f"outliers found -->{res}"
    else:
        return f"not found"
    
print(outliers(arr))