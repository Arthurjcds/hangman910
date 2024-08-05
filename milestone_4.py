#Milestone_4.py
import random
word_list = ["apple", "mango", "pineapple", "grapefruit", "strawberry"]

class Hangman():
  def __init__(self, word_list, num_lives=5):
    self.word = random.choice(word_list)
    self.word_guessed = ['_' for _ in self.word]
    self.num_letters = len(set(self.word))
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []
    print(self.word)

  def check_guess(self, guess):
    guess = guess.lower()
    if guess in self.word:
      print(f"Good guess, {guess} is in word")
      for idx, letter in enumerate(self.word):
        if letter == guess:
          self.word_guessed[idx] = guess
      self.num_letters -= 1
    else:
      self.num_lives -= 1
      print(f"Sorry, {guess} is not in the word")
      print(f"You have {self.num_lives} lives left")
  
  def ask_for_input(self):
    while True:
      guess = input("Guess a letter here\n")
      if len(guess) != 1 or not guess.isalpha():
        print("Invalid letter. Please, enter a single alphabetical character.")
      elif guess in self.list_of_guesses:
        print("You've already tried that letter!")
      else:
        self.check_guess(guess)
        self.list_of_guesses.append(guess)

game = Hangman(word_list)
game.ask_for_input()
#Calls the game
