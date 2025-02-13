class Tournament:
    def __init__(self):
        self.players = []
        self.prize_pool = 1000
        self.status = 'pending'
        self.min_players = 30
        self.rating_points = {}
        self.schedule = []
        self.rules = {
            'format': 'elimination',
            'rounds': 3,
            'time_limit': 60,
            'buy_in': 100
        }
        self.leaderboard = {}

    def create_schedule(self, start_date, end_date):
        self.schedule.append({
            'start': start_date,
            'end': end_date,
            'rounds': self.generate_rounds()
        })
        return "Расписание турнира создано"

    def register_player(self, player_id, initial_rating=1000):
        self.players.append(player_id)
        self.rating_points[player_id] = initial_rating
        self.leaderboard[player_id] = {
            'wins': 0,
            'losses': 0,
            'points': 0
        }
        return f"Игрок {player_id} зарегистрирован"

    def calculate_prize_distribution(self):
        return {
            '1st': self.prize_pool * 0.5,
            '2nd': self.prize_pool * 0.3,
            '3rd': self.prize_pool * 0.2
        }

    def update_leaderboard(self, player_id, result):
        if result == 'win':
            self.leaderboard[player_id]['wins'] += 1
            self.leaderboard[player_id]['points'] += 3
        return "Таблица лидеров обновлена"

    def get_tournament_rules(self):
        return self.rules

    def start_tournament(self):
        if len(self.players) >= self.min_players:
            self.status = 'active'
            return "Турнир начался!"
        return f"Нужно минимум {self.min_players} игроков"
