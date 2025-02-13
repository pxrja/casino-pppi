class Poker:
    def __init__(self, variant='Texas Holdem'):
        self.game_type = variant
        self.players = []
        self.current_bet = 0
        self.pot = 0
        self.deck = []
        self.community_cards = []
        self.tournament_mode = False
        self.blinds = {'small': 10, 'big': 20}
        self.tournament_level = 1

    def start_game(self):
        if self.game_type == 'Draw':
            return self.start_draw_poker()
        elif self.game_type == 'Texas Holdem':
            return self.start_holdem()
        return self.start_omaha()

    def start_draw_poker(self):
        return "Классический покер начался"

    def start_holdem(self):
        return "Техасский холдем начался"

    def start_omaha(self):
        return "Омаха холдем начался"

    def place_bet(self, amount):
        self.current_bet = amount
        self.pot += amount
        return f"Ставка {amount} принята"

    def fold(self):
        return "Игрок сбросил карты"

    def start_tournament(self):
        self.tournament_mode = True
        return "Турнир начался"

    def increase_blinds(self):
        self.tournament_level += 1
        self.blinds['small'] *= 2
        self.blinds['big'] *= 2
        return f"Уровень {self.tournament_level}: Блайнды повышены"

    def calculate_tournament_points(self, position):
        points = {1: 100, 2: 50, 3: 25}
        return points.get(position, 0)
