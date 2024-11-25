## Write program for Generating ID and Calculating Average Credit using Python.

def generate_id(a,b):
    try:
        sum = a + b
        return sum
    except:
        print("There is some error detected.")


def calculate_avg_credit(a, b):
    try:
        avg = a / b 
        return avg
    except:
        print("There is some error detected.")

student_id = 17
student_name = "Shohanur"

sem_credits = 20
sem_courses = 8

x = generate_id(student_name, str(student_id))
y = calculate_avg_credit(sem_credits, sem_courses)

print("ID is:", x)
print("Average Credit:", y)
