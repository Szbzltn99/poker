import tkinter as tk


class PokerGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Poker Game")
        self.geometry("400x300")

        self.card_label = tk.Label(self, text="Cards:")
        self.card_label.pack()

        self.card_text = tk.StringVar()
        self.card_text.set("Ace of Spades, King of Hearts")
        self.card_display = tk.Label(self, textvariable=self.card_text)
        self.card_display.pack()

        self.bet_label = tk.Label(self, text="Bet:")
        self.bet_label.pack()

        self.bet_amount = tk.StringVar()
        self.bet_amount.set("$50")
        self.bet_display = tk.Label(self, textvariable=self.bet_amount)
        self.bet_display.pack()

        self.bet_entry = tk.Entry(self)
        self.bet_entry.pack()

        self.bet_button = tk.Button
        self.bet_button = tk.Button(self, text="Place Bet", command=self.place_bet)
        self.bet_button.pack()

    def place_bet(self):
        bet_value = self.bet_entry.get()
        self.bet_amount.set(f"${bet_value}")


if __name__ == "__main__":
    game = PokerGame()
    game.mainloop()