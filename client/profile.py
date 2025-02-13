class Profile:
    def __init__(self):
        self.username = None
        self.vip_status = 'basic'
        self.balance = 0
        self.history = []

    def register(self, username):
        self.username = username
        return f"Пользователь {username} зарегистрирован"

    def get_stats(self):
        return {
            'games_played': len(self.history),
            'balance': self.balance,
            'status': self.vip_status
        }
