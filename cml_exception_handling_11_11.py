x = 5
y = 7
w = 3
t = 10

try:
    z=x+y
    print(z)

    l=t/w
    print(l)
#except TypeError:
    #print("TypeError has Detected")

#except ZeroDivisionError:
    #print("ZeroDivisionError has Detected")

except :
    print("Error has Detected")
else:
    print("No Error")

finally:
    print("Danger block passed")