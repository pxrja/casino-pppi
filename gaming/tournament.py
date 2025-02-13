class Tournament:
    """
    Класс для управления турнирами и соревнованиями.

    Обеспечивает функционал создания турниров, регистрации игроков,
    ведения рейтинга и распределения призового фонда.

    Methods:
        create_schedule(start_date, end_date): Создание расписания турнира
        register_player(player_id, initial_rating): Регистрация участника
        calculate_prize_distribution(): Расчет призовых мест
        update_leaderboard(player_id, result): Обновление таблицы лидеров
        get_tournament_rules(): Получение правил турнира
        start_tournament(): Запуск турнира

    Attributes:
        players (list): Список участников турнира
        prize_pool (float): Призовой фонд
        status (str): Статус турнира
        min_players (int): Минимальное количество участников
        rating_points (dict): Рейтинговые очки игроков
        schedule (list): Расписание турнира
        rules (dict): Правила проведения
        leaderboard (dict): Таблица лидеров
    """

    def __init__(self):
        """
        Инициализация турнира с базовыми настройками.
        """
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
        """
        Создание расписания турнира.

        Args:
            start_date (str): Дата начала турнира
            end_date (str): Дата окончания турнира

        Returns:
            str: Подтверждение создания расписания
        """
        self.schedule.append({
            'start': start_date,
            'end': end_date,
            'rounds': self.generate_rounds()
        })
        return "Расписание турнира создано"

    def register_player(self, player_id, initial_rating=1000):
        """
        Регистрация нового участника турнира.

        Args:
            player_id (int): Идентификатор игрока
            initial_rating (int): Начальный рейтинг

        Returns:
            str: Подтверждение регистрации
        """
        self.players.append(player_id)
        self.rating_points[player_id] = initial_rating
        self.leaderboard[player_id] = {
            'wins': 0,
            'losses': 0,
            'points': 0
        }
        return f"Игрок {player_id} зарегистрирован"

    def calculate_prize_distribution(self):
        """
        Расчет распределения призового фонда.

        Returns:
            dict: Распределение призового фонда
        """
        return {
            '1st': self.prize_pool * 0.5,
            '2nd': self.prize_pool * 0.3,
            '3rd': self.prize_pool * 0.2
        }

    def update_leaderboard(self, player_id, result):
        """
        Обновление статистики игрока в таблице лидеров.

        Args:
            player_id (int): Идентификатор игрока
            result (str): Результат игры

        Returns:
            str: Подтверждение обновления
        """
        if result == 'win':
            self.leaderboard[player_id]['wins'] += 1
            self.leaderboard[player_id]['points'] += 3
        return "Таблица лидеров обновлена"

    def get_tournament_rules(self):
        """
        Получение правил турнира.

        Returns:
            dict: Правила турнира
        """
        return self.rules

    def start_tournament(self):
        """
        Запуск турнира при достаточном количестве участников.

        Returns:
            str: Статус запуска турнира
        """
        if len(self.players) >= self.min_players:
            self.status = 'active'
            return "Турнир начался!"
        return f"Нужно минимум {self.min_players} игроков"
