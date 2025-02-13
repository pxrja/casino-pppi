class Baccarat:
    def __init__(self, variant='Punto Banco'):
        self.game_type = variant  # 'Punto Banco' or 'Chemin de Fer'
        self.current_hand = []
        self.banker_score = 0
        self.player_score = 0
        self.banker_cards = []
        self.player_cards = []
        self.current_banker = None  # для Chemin de Fer

    def deal_cards(self):
        if self.game_type == 'Punto Banco':
            return self.deal_punto_banco()
        return self.deal_chemin_de_fer()

    def deal_punto_banco(self):
        self.banker_cards = ['card1', 'card2']
        self.player_cards = ['card1', 'card2']
        return "Карты розданы в режиме Punto Banco"

    def deal_chemin_de_fer(self):
        self.assign_banker()
        self.banker_cards = ['card1', 'card2']
        self.player_cards = ['card1', 'card2']
        return "Карты розданы в режиме Chemin de Fer"

    def assign_banker(self):
        return "Назначен новый банкир"

    def calculate_score(self):
        self.banker_score = self.calculate_hand(self.banker_cards)
        self.player_score = self.calculate_hand(self.player_cards)
        return f"Счет: Банкир {self.banker_score}, Игрок {self.player_score}"

    def calculate_hand(self, cards):
        return sum([card.value for card in cards]) % 10
