import string
import random

key_word = 'war'

match = 0
tries = 1000

def create_string():
	random_string = [random.choice(string.ascii_lowercase) for i in range(20)]
	return random_string

def word_finder(word, array):
	temp_score = 0
	for x in range(len(word)-1):
		for y in range(len(array)-1):
			if array[y] == word[x]:
				temp_score+=1
				break
	if temp_score == len(word)-1:
		return True

for i in range(tries):
	a = create_string()
	if word_finder(key_word,a) == True:
		match+=1

print(match/tries)
