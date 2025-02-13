class Profile:
    def __init__(self):
        self.username = None
        self.vip_status = 'basic'
        self.balance = 0
        self.history = []
        self.settings = {
            'notifications': True,
            'privacy': 'public',
            'sound': True
        }
        self.tournament_rating = 1000
        self.achievements = []

    def register(self, username, email, password):
        self.username = username
        return f"Пользователь {username} зарегистрирован"

    def update_settings(self, setting_name, value):
        self.settings[setting_name] = value
        return f"Настройка {setting_name} обновлена"

    def add_activity(self, activity):
        self.history.append(activity)
        return "Активность записана"

    def upgrade_vip_status(self, new_status):
        self.vip_status = new_status
        return f"VIP статус повышен до {new_status}"

    def update_tournament_rating(self, points):
        self.tournament_rating += points
        return f"Рейтинг обновлен: {self.tournament_rating}"

    def get_stats(self):
        return {
            'games_played': len(self.history),
            'balance': self.balance,
            'status': self.vip_status,
            'tournament_rating': self.tournament_rating,
            'win_rate': self.calculate_win_rate(),
            'achievements': self.achievements
        }

    def calculate_win_rate(self):
        wins = sum(1 for game in self.history if game['result'] == 'win')
        return wins / len(self.history) if self.history else 0
