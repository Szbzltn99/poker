from Deck import Deck
from Player import Player


class Table:
    def __init__(self, players_num):
        self.num_players = players_num
        self.pot = 0
        self.max_raise_amount = 0

    def initialize_players(self, players):
        for i in range(self.num_players):
            player = Player()
            players.append(player)

    def deal(self, deck, players):
        for _ in range(2):
            for i in range(len(players)):
                players[i].hand.append(deck.cards.pop())

    def print_cards(self, players):
        for i in range(len(players)):
            print(players[i].hand)

    def update_player_actions(self, players, first_player_index):
        for i in range(len(players)):
            player_index = (first_player_index + i) % len(players)
            if players[player_index].fold is False:
                print(f"Enter the action for player {player_index}")
                players[player_index].action = input()
                if players[player_index].action == "fold":
                    players[player_index].fold = True
                elif players[player_index].action.startswith("raise"):
                    raise_amount = int(players[player_index].action[5:])
                    if raise_amount < self.max_raise_amount:
                        raise Exception("Nem emelhetsz kissebbet mint a max")
                    if raise_amount > players[player_index].chips:
                        raise Exception("Nincs elegendő chiped")
                    players[player_index].raise_amount = raise_amount
                    self.pot = self.pot + raise_amount
                    players[player_index].chips = players[player_index].chips - raise_amount
                    self.max_raise_amount = raise_amount
                elif players[player_index].action == "call":
                    if self.max_raise_amount == 0:
                        raise Exception("Nincs mit hívnod")
                    call_amount = self.max_raise_amount - players[player_index].raise_amount
                    if call_amount > players[player_index].chips:
                        raise Exception("Nincs elegendő chiped")
                    players[player_index].raise_amount = self.max_raise_amount
                    self.pot = self.pot + call_amount
                    players[player_index].chips = players[player_index].chips - call_amount
                elif players[player_index].action == "check":
                    if self.max_raise_amount > players[player_index].raise_amount:
                        raise Exception("Nem hagyhatod abba a hívást")
                else:
                    raise Exception("Érvénytelen művelet")
            if all(player.fold for player in players):
                raise Exception("Az összes játékos kiestett")

    def print_flop(self, deck, flop_turn_river):
        for i in range(3):
            flop_turn_river.append(deck.cards.pop())
        for cards in flop_turn_river:
            print(cards)

    def flop_action(self, players):
        while True:
            if sum([1 for player in players if player.action in ["call", "fold"]]) == len(players):
                break
            for i in range(len(players)):
                if players[i].action not in ["fold"]:
                    print(f"Enter the action for player {i}")
                    players[i].action = input()
