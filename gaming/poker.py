class Poker:
    def __init__(self):
        self.game_type = 'Texas Holdem'
        self.players = []
        self.current_bet = 0
        self.pot = 0
        self.deck = []

    def start_game(self):
        return "Игра началась, раздаются карты"

    def place_bet(self, amount):
        self.current_bet = amount
        self.pot += amount
        return f"Ставка {amount} принята"

    def fold(self):
        return "Игрок сбросил карты"
