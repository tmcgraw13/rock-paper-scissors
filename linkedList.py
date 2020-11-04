class Node:
    """
    Allows circular traversal of values
    """

    @staticmethod
    def from_list(args: []):
        pass

    def __init__(self, value: str, after=None, previous=None):
        self.value = value
        self.after = self if after is None else after
        self.previous = self if previous is None else previous

    def add(self, value: str):
        after = self.after
        previous = self.previous
        node = Node(value, after, self)
        after.previous = node
        self.after = node
        if previous == self:
            previous = node

    def __str__(self):
        return f"[{self.previous.value} {self.value} {self.after.value}]"


n = Node("rock")
n.add("paper")
n.add("scissors")
print(n)

print("Rock, paper, or scissors?")
hand = input("State your play: ").lower()
