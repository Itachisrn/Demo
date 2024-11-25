## Object Oriented Programming

class Human:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.head = 1
        self.age = 0
    
    def age_inc(self, a):
        self.age += a
    #Head = 1
    #Name = " "
    #Age = 0

kk = Human("Shohanur", "Male")
kk1  = Human("Nirob", "Male")
kk.age = 24
kk1.age = 23


#kk = Human()
#kk.Name = "Shohanur"
#kk.Age = 24

#print(kk.name)
#print(kk.gender)

print("Before\n", kk.age)
kk.age_inc(5)
print("\nAfter\n", kk.age)


#kk1 = Human()
#kk1.Name = "Nirob"
#kk1.Age = 23

#print(kk1.name)
#print(kk1.gender)

print("\nBefore\n", kk1.age)
kk1.age_inc(5)
print("\nAfter\n", kk1.age)

def gen_func(num1, num2):
    print("\n ", num1+num2)

gen_func(11, 21)