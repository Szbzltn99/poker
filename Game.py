from Deck import Deck
from Table import Table


class Game:
    def __init__(self):
        self.table = Table(5)
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        self.flop_turn_river = []

    def start(self):
        self.table.initialize_players(self.players)
        self.table.deal(self.deck, self.players)
        self.table.print_cards(self.players)
        self.table.update_player_actions(self.players, 0)
        self.table.print_flop(self.deck, self.flop_turn_river)
        self.table.flop_action(self.players)
