class Blackjack:
    def __init__(self):
        self.game_type = 'American'
        self.player_hand = []
        self.dealer_hand = []
        self.deck = []

    def hit(self):
        return "Выдана дополнительная карта"

    def stand(self):
        return "Игрок остановился"
