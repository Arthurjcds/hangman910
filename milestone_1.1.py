guess = input("Write a single letter here:\n")
if len(guess) == 1 and guess.isalpha():
  print("Good Guess!")
else:
  print("Oops, thats not a valid input :(")
