arr = [1, 2, 3, 4, 5]
def var(arr):
    n = len(arr)
    total = 0
    for i in arr:
        total +=i
    mean = total/n
    # mean = sum(arr)/n

    var = 0
    var = sum((i-mean)**2 for i in arr) /n
    print(f"var -->{var}")
    print(f"std-->{var**0.5}")
    return var


def zscore(arr):
    n = len(arr)
    total = 0
    for i in arr:
        total +=i
    mean = total/n
    std_var = var(arr)**0.5

    res = {}
    for i in arr:
        res[i] = round((i-mean)/std_var,4)

    return res
print(f"zscore --> {zscore(arr)}")
