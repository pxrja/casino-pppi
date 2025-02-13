class Tournament:
    def __init__(self):
        self.players = []
        self.prize_pool = 0
        self.status = 'pending'
        self.min_players = 2

    def register_player(self, player_id):
        self.players.append(player_id)
        return f"Игрок {player_id} зарегистрирован"

    def start_tournament(self):
        if len(self.players) >= self.min_players:
            self.status = 'active'
            return "Турнир начался"
        return "Недостаточно игроков"
