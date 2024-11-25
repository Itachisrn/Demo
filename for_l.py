for item in ('python', 'nirob'):
   print(item)
   
for item in range (2, 9, 3):
 print(item)

prices=[10, 20, 30]
total=0
for item in prices:
	total+=item
print(f"Total: {total}")

for x in range(4):
	for y in range (3):
		print(f"({x}, {y})")



numbers=[1, 1, 1, 1, 6]
for x_count in numbers:
	output =''
	for count in range(x_count):
	    output += 'x'
	print(output)
