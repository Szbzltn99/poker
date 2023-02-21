from Deck import Deck
from Table import Table


class Game:
    def __init__(self):  #itt adjuk meg hogy egymás után mik történjenek--ami ott van a startban
        self.table = Table(5)
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []  #először üres aztán"self.table.initialize_players(self.players)" belekerülnek a játékosok
        self.flop_turn_river = []

    def start(self): #start metódus
        self.table.initialize_players(self.players)
        self.table.deal(self.deck, self.players)
        self.table.print_cards(self.players)
        self.table.update_player_actions(self.players, 0)
        self.table.print_flop(self.deck, self.flop_turn_river)
        self.table.flop_action(self.players)
