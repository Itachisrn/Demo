dict={"nishat": 100, "rahim": 110}
#print(dict["nishat"])

dict1={"U_name": "JUST", "E_year": 2008, "N_dept": 28, "V_grade": 'A'}
#print(dict1)

## for update

dict1.update({"N_stu": 5000})
#print(dict1)  

dict1["N_hall"]=3
print(dict1)
print("\n")

for element in dict1:
    print(element)  
print("\n")

for element in dict1.keys():
    print(element)
print("\n")

for element in dict1.values():
    print(element)
print("\n")

for element in dict1.items():
    print(element)
print("\n")

for key, value in dict1.items():
    print(key, value)
