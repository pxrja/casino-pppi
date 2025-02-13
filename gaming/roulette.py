class Roulette:
    def __init__(self):
        self.type = 'European'
        self.last_numbers = []
        self.wheel_numbers = range(0, 37)

    def spin(self):
        from random import choice
        result = choice(self.wheel_numbers)
        self.last_numbers.append(result)
        return f"Выпало число {result}"

    def place_bet(self, bet_type, amount):
        return f"Ставка {amount} на {bet_type} принята"
