## def function_name(parameters):

def summation(a, b):
    sum = 0
    for i in range(a,b+1):
        sum = sum + i
    #print(sum)
    return sum

#B=[4, 5, 6, 10]
#summation(B,5)     ## for divide
#summation(a=6, b=10) ## order select

s = summation(6, 10)
print(s)
#h=[40, 4, 5, 1]
#summation(h)