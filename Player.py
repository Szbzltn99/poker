class Player:
    def __init__(self):
        self.hand = []
        self.chips = 400
        self.action = ""
        self.fold = False
        self.raise_amount = 0
        self.error = False
