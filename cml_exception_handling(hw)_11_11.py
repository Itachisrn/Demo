student_id = 3
student_name = "Nirob"

sem_credits = 20
sem_courses = 8

try:
    user_id = student_name + str(student_id)
    print(user_id)

    avg_credits = sem_credits/sem_courses
    print(avg_credits)

except:
    print("Error has detected")



