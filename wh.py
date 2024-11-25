i=1
while i<=5:
	print('f' *i)
	i=i+1
print("Done")

secret_number=15
guess_count=0
guess_limit=5

while guess_count<guess_limit:
	guess=int(input('Guess: '))
	guess_count+=1
	if guess==secret_number:
		print('You won!')
		break
else:
	print('Sorry, you fail!')
