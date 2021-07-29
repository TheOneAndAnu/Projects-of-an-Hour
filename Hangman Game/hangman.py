#Hangman Game
import random 
import os

def hangman():

	print("""\
 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

""")
	
	stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
	
	word = random.choice(open("words.txt", "r").read().split())
	letter_count = len(word)
	new_word = "_" * letter_count
	temp_word = ""
	
	input("Press enter to start.")
	
	tries = 6
	stage_count = 0
	while tries > 0:
		
		os.system('clear')

		print(*new_word, sep=' ')
		print(stages[stage_count])

		if all(i in temp_word for i in word):
			print("\nYou have guessed the correct word!! You win!!")
			break

		guess = input("\nType an alphabet: ")

		if guess == word:
			print("\nYou have guessed the correct word!! You win!!")
			break

		if guess in word:

			if guess in temp_word:
				print(f"You already guessed {guess}. Try Again.")
				input("\nPress enter to continue.")
				
			else:
				temp_word += guess
				for i in range(letter_count):
					if word[i] == guess:
						new_word = new_word[0:i] + guess + new_word[i+1: ]

		else:
			tries -= 1
			stage_count += 1
			print(f"Wrong Guess. There is no {guess} in the word. You lose a life")
			print(f"You have {tries} guesses left")
			input("\nPress enter to continue.")
			
			if tries==0:
				os.system("clear")
				print(stages[6])
				print(f"\nYou Lose! The correct word was {word}. Try Again.")
			


			

hangman()
while True:
	next_round = input("\nDo you want to play again? y/n  ")
	if(next_round == 'y'):
		os.system('clear')
		hangman()
	elif(next_round == 'n'):
		os.system('clear')
		print("Thanks for playing!")
		break
	else:
		os.system('clear')
		print("Invalid option. Type either y/n.")
		
