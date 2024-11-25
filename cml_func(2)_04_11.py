from multipledispatch import dispatch
@dispatch(int, int)                          ## (It is called function overloading)
def add(a, b):
    sum = a + b
    return sum
@dispatch(int, int, int)
def add (a, b, c):
    sum = a + b + c
    return sum
@dispatch(float, float)
def add (a, b):
    sum = a + b 
    return sum

@dispatch(str, str)
def add (a, b):
    sum = a + b 
    return sum

s=add(6, 7, 8)
s1=add(7, 8)                      ## (always the last function call effective)
s2=add(6.1, 7.5)
s3=add("A", "B")

print(s)
print(s1)
print(s2)
print(s3)