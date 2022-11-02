import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
lives = 6
display = []
for i in range(len(chosen_word)):
  display += "_"

game_end = False
while not game_end:
  guess = input("Guess a letter: ").lower()
  
  if guess in display:
    print(f"You have already guessed the letter {guess}.")
  for position in range(len(chosen_word)):
    char = chosen_word[position]
    if char == guess:
      display[position] = char

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life. D:\n")
    lives -= 1
    if lives == 0:
      game_end = True
      print("You lose :(")

  #join list elements into string
  print(f"{' '.join(display)}")

  if "_" not in display:
    game_end = True
    print("You win!")

  print(stages[lives])
