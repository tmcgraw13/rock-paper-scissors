from enum import Enum, auto, unique
from getpass import getpass


class AutoName(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name


@unique
class Option(AutoName):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


class Node:
    """
    Allows circular traversal of values
    """

    def __init__(self, value: Option, after=None, previous=None):
        self.value: Option = value
        self.after: Node = self if after is None else after
        self.previous: Node = self if previous is None else previous

    @staticmethod
    def fromList(options: [Option]):
        n = Node(options[0])
        for opt in options[1:]:
            n.append(opt)
        return n

    def append(self, value: Option):
        after = self.after
        previous = self.previous
        node = Node(value, after, self)
        after.previous = node
        self.after = node
        if previous == self:
            previous = node

    def insert(self, value: Option):
        after = self.after
        previous = self.previous
        node = Node(value, self, previous)
        previous.after = node
        self.previous = node
        if after == self:
            after = node

    def __str__(self):
        return f"[{self.previous.value.value} {self.value.value} {self.after.value.value}]"


def getPlay(player: str):
    validPlay: bool = False
    play: Option
    while not validPlay:
        print(f"{player} do you choose Rock, Paper, or Scissors?")
        hand = getpass(
            "State your play (your input is hidden so nothing will show up as you type): ").upper()
        try:
            play = Option[hand]
            validPlay = True
        except:
            print(f"{hand} is not a valid option")
    return play


# Initialize options
n = Node.fromList([Option.ROCK, Option.PAPER, Option.SCISSORS])

# Get player names and plays
player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")
print("--------------------------------------------")
play1 = getPlay(player1)
play2 = getPlay(player2)

# Determine a winner
while n.value != play1:
    n = n.after

print("--------------------------------------------")
if n.after.value == play2:
    print(f"{n.value.name.title()} beats {play2.name.title()}. {player1} Wins!")
elif n.previous.value == play2:
    print(f"{play2.name.title()} beats {n.value.name.title()}. {player2} Wins!")
else:
    print("Draw!")
