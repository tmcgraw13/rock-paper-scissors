from enum import Enum

# Let's play Rock-Paper-Scissors


def hand_check(hand: str, possible_moves: []):
    if hand.lower() not in possible_moves:
        print("Read the instructions you Idiot...")
        exit(1)


# Take enum input
# map it to a number between the other options
# return new move map
#  def map_choice(input: int):
#      input = 2

possible_moves = ["rock", "paper", "scissssssors"]

print("Welcome to Rock Paper and Scissssssors")

val = input(f"Player 1 - Enter Rock, Paper, or Scissssssors: ")
# prompt = f"Player 1 - Enter {possible_moves}: "
# val = input("Player 1 - Enter %s: " %
#             [print(move) for move in possible_moves])
hand_check(val, possible_moves)

val2 = input("Player 2 - Enter Rock, Paper, or Scissssssors: ")
hand_check(val2, possible_moves)


# TODO: Compare hands
# Declare a winner
# Make it rain on the winner

# To declare winner


# TODO: Make it smart
#Rock > scissors
#Scissors > Paper
#Paper > Rock

print(val)


# if hand_1 == scissssssors:
#     paper = 1
#     scissssssors = 2
#     rock = 3
# elif hand_1 == rock:
#     scissssssors = 1
#     rock = 2
#     paper = 3
# else hand_1 == paper:
#     rock = 1
#     paper = 2
#     scissssssors = 3
# hand_1 = 2

# if hand_2 > hand_1:
#     print("Player Two, a winner is you!")
# elif hand_2 == hand_1:
#     print("Tie Game, you both suck!")
# else:
#     print("Player One, you won son!")
