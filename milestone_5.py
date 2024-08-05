#Milestone_5.py
import random
word_list = ["apple", "mango", "pineapple", "grapefruit", "strawberry"]
#Adds a list of words, one of which will be the one we try to guess

class Hangman:
  def __init__(self, word_list, num_lives=5):
    self.word = random.choice(word_list)
    self.word_guessed = ['_' for _ in self.word]
    self.num_letters = len(set(self.word))
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []
#Adds a class, with all the attributes and methods to help the game

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
#First method inside the class, converts guess to lowercse for consistency, 
#checks if word is valid or not and responds accordingly, edits how many words are left to guess and how many lives remain
  
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
        break
#Asks for input, ensures it is a single letter and not one that has been repeated
#Calls the check_guess function and adds to the list of guesses  

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
      if game.num_lives == 0:
        print("Womp Womp. You Lose :()")
        break
      elif game.num_letters > 0:
        print(game.list_of_guesses)
        game.ask_for_input()
      elif game.num_lives != 0 and not game.num_letters > 0:
        print("Congratulations, You Win!")
        break
#First function outside the class, calls in the Hangman class, checks if you can still play, have won or have lost
#Provides necessary feedback  
play_game(word_list)
#Calls the game