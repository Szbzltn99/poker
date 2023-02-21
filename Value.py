class Value: #gethandvalue minden metódust meghív és true or false a vissazteres
                #legmagasabb true
                #2 parameter palyers-flopturnriver
                #megkülönböztetni a rankokat (self.getpairranks ) ..maybe
                #get_hand_value 2 paramérter players,fploturnriver
                #
    def __init__(self):

    def _is_pair(self,players,flop_turn_river):
        player_hand = []
        flop_turn_river_values = []
        for i in range(len(flop_turn_river)):
            flop_turn_river_values.append(flop_turn_river[i][0])
        for i in range(len(players)):
            player_hand.append(players[i].hand[0][0])
            player_hand.append(players[i].hand[1][0])
            for k in range(flop_turn_river):
                if player_hand[0]==flop_turn_river_values[k]:
                    players[i].hand_value.append(player_hand[0])
                    return True
                elif  player_hand[1]==flop_turn_river_values[k]:
                    players[i].hand_value.append(player_hand[1])
                    return True

    def get_hand_value(self):
        if self._is_straight_flush():
            return 9, self.ranks[-1]
        elif self._is_four_of_a_kind():
            return 8, self._get_four_of_a_kind_rank()
        elif self._is_full_house():
            return 7, self._get_full_house_ranks()
        elif self._is_flush():
            return 6, self.ranks[-1]
        elif self._is_straight():
            return 5, self.ranks[-1]
        elif self._is_three_of_a_kind():
            return 4, self._get_three_of_a_kind_rank()
        elif self._is_two_pairs():
            return 3, self._get_two_pair_ranks()
        elif self._is_pair():
            return 2, self._get_pair_rank()
        else:
            return 1, self.ranks[-1]