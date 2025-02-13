class Baccarat:
    def __init__(self):
        self.game_type = 'Punto Banco'
        self.current_hand = []
        self.banker_score = 0
        self.player_score = 0

    def deal_cards(self):
        return "Карты розданы"

    def calculate_score(self):
        return f"Счет: Банкир {self.banker_score}, Игрок {self.player_score}"
