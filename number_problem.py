def game_round():
        while True:
                try:
                        num = int(input("Pick a number between 1 and 5: "))
                except ValueError:
                        print("That's not an integer.")
                        game_round()
		
                if num > 5 or num < 1:
                        num = int(input("That's out of range."))
                        game_round()
                else:
                        break

game_round()
print("Success!")
