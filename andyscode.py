from enum import Enum

# Let's play Rock-Paper-Scissors
def hand_1_choice(hand_1):
    if hand_1 == "scissssssors":
        result = {'paper': 1, 'scissssssors': 2, 'rock': 3}
    elif hand_1 == "rock":
        result = {'paper': 3, 'scissssssors': 1, 'rock': 2}
    else:
        result = {'paper': 2, 'scissssssors': 3, 'rock': 4}
    return result

def hand_2_choice(hand_2, result):

    hand_2 = result[hand_2]
    return hand_2

def score(hand_2):
    if hand_2 == 2:
        print("Tie Game, you both suck!")
    elif hand_2 > 2:
        print("Player Two, a winner is you!")
    else:
        print("Player One, you won son!")

def hand_check(hand: str, possible_moves: []):
    if hand.lower() not in possible_moves:
        print("Read the instructions you Idiot...")
        exit(1)


possible_moves = ["rock", "paper", "scissssssors"]


print("Welcome to Rock Paper and Scissssssors")

hand_1 = input(f"Player 1 - Enter Rock, Paper, or Scissssssors: ")
hand_check(hand_1, possible_moves)

hand_2 = input("Player 2 - Enter Rock, Paper, or Scissssssors: ")
hand_check(hand_2, possible_moves)

result = hand_1_choice(hand_1)
hand_2 = hand_2_choice(hand_2, result)
score(hand_2)
