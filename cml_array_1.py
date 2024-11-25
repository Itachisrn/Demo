age = [20.5, 20.1, 19.7, 18.9, 19.6, 19.8, 19.9,20.4, 21.8, 21.2]

## For putting value
age.append(22.1)
age.append(22.3)                 
age.append(22.2)

## For removing value
age.pop(1)
age.remove(21.8)

## For finding value
b = age.index(18.9)

## For changing value
age[0]=22.2

age[0] = age[0] +5


##for a in age:
    ##print(a)

s=len(age)
for i in range(0, s-1):
    age[i] = age[i] + 5
    ##print(age[i])

a = sum(age)
d = a/s
print(d)
sum = 0
for i in range(0, s):
    sum = sum + age[i]
    
print(sum)
w=sum/s
print(w)
##print(b)
##print(age)
##print(age[10])

##print(s)