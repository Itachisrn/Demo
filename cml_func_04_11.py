def func(a:int, b:int)->int:
    sum = 0
    v=1
    for i in range(a, b+1):
        sum = sum + i

    for i in range(a, b+1):
        v=v*i   
    return sum, v

c, d = func(1, 10)
print(c, d)

