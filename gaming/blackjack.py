class Blackjack:
    def __init__(self, variant='American'):
        self.game_type = variant  # 'American' or 'European'
        self.player_hand = []
        self.dealer_hand = []
        self.deck = []
        self.insurance = False
        self.bet_amount = 0
        self.insurance_amount = 0

    def hit(self):
        card = self.deck.pop()
        self.player_hand.append(card)
        return "Выдана дополнительная карта"

    def stand(self):
        return "Игрок остановился"

    def deal_initial_cards(self):
        if self.game_type == 'American':
            return self.deal_american()
        return self.deal_european()

    def deal_american(self):
        # Две карты игроку, две дилеру (одна открыта)
        return "Карты розданы по американским правилам"

    def deal_european(self):
        # Две карты игроку, одна дилеру
        return "Карты розданы по европейским правилам"

    def offer_insurance(self):
        if self.dealer_hand[0].rank == 'A':
            self.insurance_amount = self.bet_amount / 2
            return "Предложена страховка"
        return "Страховка недоступна"

    def check_blackjack(self):
        return sum([card.value for card in self.player_hand]) == 21
