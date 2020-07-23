import random

#che main random walk function. I used a list to operate, felt more comfortable with

def main(try_number):
	results = []
	for a in range(1000):
		x = [0,0]
		temp_list = [-1,1]

		for i in range(try_number):
			temp_position = random.randint(0,1)
			x[temp_position] += random.choice(temp_list)

		distance = abs(x[0]) + abs(x[1])
		results.append(distance)

	home = 0

	for b in range(len(results)-1):
		if results[b] <= 4:
			home+=1

	final_data = home/10

	return(final_data)

#checking till the percent of gettinghomeable tries gets lower than 50, then printing the previous number as a secure one

for i in range(10,30):
	if main(i) >= 50:
		pass
	else:
		print(i-1)
		print(main(i-1))
		print('Secured choice: ',str(i-1),', home = ',main(i-1))
		break


