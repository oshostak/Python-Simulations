import random
import matplotlib.pyplot as plt

def round_it(number):
	number = (number//1000)*1000
	return number


results = []
tries = 100000
for i in range(tries):
	calories = 0
	for i in range(random.randint(1,8)):
		for i in range(random.randint(1,30)):
			calories += random.randint(50,500)
	results.append(round_it(calories))

display = [0 for i in range(120001)]

for i in range(len(results)):
	display[results[i]] +=1

plt.plot(display)
plt.show()
