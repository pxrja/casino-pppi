class Tournament:
    def __init__(self):
        self.players = []
        self.prize_pool = 1000
        self.status = 'pending'
        self.min_players = 30
        self.rating_points = {}

    def register_player(self, player_id):
        self.players.append(player_id)
        self.rating_points[player_id] = initial_rating
        return f"Игрок {player_id} зарегистрирован с рейтингом {initial_rating}"

    def start_tournament(self):
        if len(self.players) >= self.min_players:
            self.status = 'active'
            return "Турнир начался! Рейтинговая игра"
        return "Нужно минимум 4 игрока для рейтингового турнира"

    def calculate_rating(self, winner_id, loser_id):
        self.rating_points[winner_id] += 25
        self.rating_points[loser_id] -= 15
        return "Рейтинги обновлены"
