age = [20.5, 20.1, 19.7, 18.9, 19.6, 19.8, 19.9,20.4, 21.8, 21.2]

s=len(age)

a = sum(age)
d = a/s
##print(d)
sum = 0
for i in range(0, s):
    sum = sum + age[i]

print(sum)
w=sum/s
print(w)

    
for i in range(0, s):
    if age[i] > 20:
        print(age[i])

##tuple
t1 = (20.5, 20.1, 19.7, 18.9, 19.6, 19.8, 19.9,20.4, 21.8, 21.2)
prod = 1
for x in t1:
    prod = prod * x
print(prod)