import random



def finish():
	print("You won!")
	exit()



def slot_maker(slot_for_word, secret_word):
	for i in range(len(secret_word)) :
		slot_for_word = slot_for_word+str(i)
	return(slot_for_word)



def print_word(slot_for_word, secret_word):
	for i in range(len(secret_word)) :
		if (slot_for_word[i]).isdigit():
			slot_for_word = slot_for_word.replace(slot_for_word[i], '_', 1)
	print(slot_for_word)



def update(secret_word, slot_for_word, tries, used_letters, score):
     
	if tries == 0 :
		print("You lost.")
		exit()

	if score == len(secret_word) :
		finish()

	guess_letter = str.lower(input("Input a letter: "))

	if len(guess_letter) > 1 :
		print("Please, enter acceptable values.")
		update(secret_word, slot_for_word, tries, used_letters, score)

	elif guess_letter in used_letters:
		print("You've already used this letter.")
		update(secret_word, slot_for_word, tries, used_letters, score)

	for i in range(len(secret_word)) :
		
		
		if guess_letter == secret_word[i] :

			used_letters = used_letters+guess_letter
			score = score+1
			slot_for_word = slot_for_word.replace(str(i), guess_letter, 1)


		elif guess_letter not in secret_word :

			tries = tries-1
			print("You lost one try. Tries left:", tries)
			print_word(slot_for_word, secret_word)
			update(secret_word, slot_for_word, tries, used_letters, score)

	print_word(slot_for_word, secret_word)

	update(secret_word, slot_for_word, tries, used_letters, score)


print("Hello, let's play hangman. You have 5 tries.")
a = ''
word_list = ['play', 'soccer', 'book', 'table', 'class']
secret_word = random.choice(word_list)
slot_for_word = ''
tries = 5
used_letters = str('')
slot_for_word = slot_maker(slot_for_word, secret_word)
score = 0


update(secret_word, slot_for_word, tries, used_letters, score)
