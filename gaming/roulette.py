class Roulette:
    def __init__(self, variant='European'):
        self.type = variant
        self.last_numbers = []
        self.wheel_numbers = self.initialize_wheel()
        self.bets = []
        self.payouts = {
            'straight': 35,
            'split': 17,
            'street': 11,
            'corner': 8,
            'line': 5,
            'dozen': 2,
            'column': 2,
            'even': 1,
            'odd': 1,
            'red': 1,
            'black': 1
        }

    def initialize_wheel(self):
        if self.type == 'American':
            return list(range(0, 37)) + [38]  # 0, 00
        return list(range(0, 37))  # 0-36

    def spin(self):
        from random import choice
        result = choice(self.wheel_numbers)
        self.last_numbers.append(result)
        self.check_all_bets(result)
        return f"Выпало число {result}"

    def place_bet(self, bet_type, amount, numbers=None):
        bet = {
            'type': bet_type,
            'amount': amount,
            'numbers': numbers
        }
        self.bets.append(bet)
        return f"Ставка {amount} на {bet_type} принята"

    def check_all_bets(self, winning_number):
        total_winnings = 0
        for bet in self.bets:
            winnings = self.calculate_win(bet, winning_number)
            total_winnings += winnings
        return total_winnings

    def calculate_win(self, bet, winning_number):
        if winning_number in bet['numbers']:
            return bet['amount'] * self.payouts[bet['type']]
        return 0

    def apply_french_rules(self):
        # La Partage and En Prison rules
        if self.type == 'French':
            return "Применены французские правила"
