# Practical Application Lab - 5/31/2024

## 1. Sprint Retrospective with Steph

Steph will review retrospective cards at the start of class.

## 2. Choose Your Own Text-based Game Lab

Choose one of the four options, create a new GitHub repository, and publish your solution to it.

As your first commit, write a README.md describing which lab you have chosen.

All games will require `input()` to get input from the player, and `print()` to return output.

Feel free to work on more than one if you complete your chosen activity before class is over.

# Guess The Number
Write a Python script that secretly chooses a random number between 1 and 20,
and asks the player to pick numbers until they find it.

**Required Tools**: `random.randint()` ([docs.python.org](https://docs.python.org/3/library/random.html#random.randint)), `if` statements, `while` loops, `int()` casting

**Challenge**: Limit the player to 5 guesses.

# Mad Libs
Write a Python script that asks the player for an adjective,
a plural noun, and a celebrity name. Then print out a sentence
using those words. Examples: [thewordfinder.com/wordlibs](https://www.thewordfinder.com/wordlibs/)

**Required Tools**: string `format()` or `+`

**Challenge**: Give the player the option of playing again with different words and sentence.

# Rock, Paper, Scissors
Write a Python script that secretly chooses a string `'rock'`,
`'paper'`, or `'scissors'`, asks the player to input a string, and
prints out the winner. The winner is decided with the following rules:
Rock beats scissors, scissors beat paper, paper beats rock.

**Required Tools**: `random.choice()` ([docs.python.org](https://docs.python.org/3/library/random.html#random.choice)), `if` statements, `while` loops

**Challenge**: Add a fourth choice, `'peace'`, which always wins, except against `'peace'`, which is a tie.

# Choose Your Own Adventure
Write a Python script that begins by printing a one-sentence story,
asks the player to choose what to do, and prints a different result
based on their choice.

**Required Tools**: `if` statements

**Challenge**: Add another step to the story, asking the player to
make a second choice, with two more unique results.