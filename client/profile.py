class Profile:
    """
    Класс для управления профилем пользователя игровой платформы.

    Обеспечивает функционал регистрации, настройки профиля,
    отслеживания активности и статистики игрока.

    Methods:
        register(username, email, password): Регистрация нового пользователя
        update_settings(setting_name, value): Обновление настроек профиля
        add_activity(activity): Добавление записи активности
        upgrade_vip_status(new_status): Повышение VIP статуса
        update_tournament_rating(points): Обновление турнирного рейтинга
        get_stats(): Получение статистики игрока
        calculate_win_rate(): Расчет процента побед

    Attributes:
        username (str): Имя пользователя
        vip_status (str): VIP статус игрока
        balance (float): Баланс счета
        history (list): История активности
        settings (dict): Настройки профиля
        tournament_rating (int): Турнирный рейтинг
        achievements (list): Достижения игрока
    """

    def __init__(self):
        """
        Инициализация профиля пользователя.
        """
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
        """
        Регистрация нового пользователя.

        Args:
            username (str): Имя пользователя
            email (str): Email пользователя
            password (str): Пароль

        Returns:
            str: Подтверждение регистрации
        """
        self.username = username
        return f"Пользователь {username} зарегистрирован"

    def update_settings(self, setting_name, value):
        """
        Обновление настроек профиля.

        Args:
            setting_name (str): Название настройки
            value (any): Новое значение

        Returns:
            str: Подтверждение обновления
        """
        self.settings[setting_name] = value
        return f"Настройка {setting_name} обновлена"

    def add_activity(self, activity):
        """
        Добавление новой записи активности.

        Args:
            activity (dict): Данные об активности

        Returns:
            str: Подтверждение добавления
        """
        self.history.append(activity)
        return "Активность записана"

    def upgrade_vip_status(self, new_status):
        """
        Повышение VIP статуса пользователя.

        Args:
            new_status (str): Новый VIP статус

        Returns:
            str: Подтверждение повышения
        """
        self.vip_status = new_status
        return f"VIP статус повышен до {new_status}"

    def update_tournament_rating(self, points):
        """
        Обновление турнирного рейтинга.

        Args:
            points (int): Изменение рейтинга

        Returns:
            str: Новое значение рейтинга
        """
        self.tournament_rating += points
        return f"Рейтинг обновлен: {self.tournament_rating}"

    def get_stats(self):
        """
        Получение статистики игрока.

        Returns:
            dict: Статистика игрока
        """
        return {
            'games_played': len(self.history),
            'balance': self.balance,
            'status': self.vip_status,
            'tournament_rating': self.tournament_rating,
            'win_rate': self.calculate_win_rate(),
            'achievements': self.achievements
        }

    def calculate_win_rate(self):
        """
        Расчет процента побед игрока.

        Returns:
            float: Процент побед
        """
        wins = sum(1 for game in self.history if game['result'] == 'win')
        return wins / len(self.history) if self.history else 0
