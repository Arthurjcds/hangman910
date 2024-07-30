import random
word_list = ["apple", "mango", "pineapple", "grapefruit", "strawberry"]
print(word_list)

word = random.choice(word_list)
print(word)

#This part generates a random word from my given list

def check_guess(guess):
  guess = guess.lower()
  if guess in word:
    print(f"Good Guess! '{guess}' is in the word :)")
  else:
    print(f"Womp Womp, '{guess}' isn't in the word :(")

#This check_guess function sees if the the input matches a letter in the random word

def ask_for_input():
  while True:
    guess = input("Write a single letter here:\n")
    if len(guess) == 1 and guess.isalpha():
      break
    else:
      print("Invalid letter. Please, enter a single alphabetical character.")
  #The ask_for_input function makes the input lowercase, and makes sure it is valid
  check_guess(guess)

ask_for_input()
