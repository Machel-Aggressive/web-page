

def func(x):
    return list(map(lambda x:max(0, x), x))

arr = [[-1,-2,-4],[1,2,-4],[-3,4,5]]

result = list(map(func, arr))
print(result)