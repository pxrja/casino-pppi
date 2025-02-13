class UserInterface:
    """
    Класс для управления пользовательским интерфейсом игровой платформы.

    Обеспечивает настройку интерфейса, навигацию между играми,
    управление ставками и взаимодействие с игровыми столами.

    Methods:
        change_language(lang): Смена языка интерфейса
        change_theme(new_theme): Изменение темы оформления
        adapt_to_device(device_type): Адаптация под устройство
        navigate_games(game_type): Навигация между играми
        start_stream(table_id): Запуск трансляции стола
        toggle_hints(): Управление подсказками
        place_bet(amount): Размещение ставки
        join_table(table_id): Присоединение к столу
        init_chat(): Инициализация чата

    Attributes:
        language (str): Текущий язык интерфейса
        theme (str): Тема оформления
        device (str): Тип устройства
        current_game (str): Текущая игра
        bet_amount (float): Размер ставки
        active_tables (list): Активные столы
        hints_enabled (bool): Статус подсказок
    """

    def __init__(self):
        """
        Инициализация пользовательского интерфейса.
        """
        self.language = 'ru'
        self.theme = 'dark'
        self.device = 'desktop'
        self.current_game = None
        self.bet_amount = 0
        self.active_tables = []
        self.hints_enabled = True

    def change_language(self, lang):
        """
        Изменение языка интерфейса.

        Args:
            lang (str): Код языка

        Returns:
            str: Подтверждение смены языка
        """
        self.language = lang
        return f"Язык изменен на {lang}"

    def change_theme(self, new_theme):
        """
        Изменение темы оформления.

        Args:
            new_theme (str): Название темы

        Returns:
            str: Подтверждение смены темы
        """
        self.theme = new_theme
        return f"Тема изменена на {new_theme}"

    def adapt_to_device(self, device_type):
        """
        Адаптация интерфейса под устройство.

        Args:
            device_type (str): Тип устройства

        Returns:
            str: Подтверждение адаптации
        """
        self.device = device_type
        return f"Интерфейс адаптирован под {device_type}"

    def navigate_games(self, game_type):
        """
        Переключение между играми.

        Args:
            game_type (str): Тип игры

        Returns:
            str: Подтверждение перехода
        """
        self.current_game = game_type
        return f"Переход к игре {game_type}"

    def start_stream(self, table_id):
        """
        Запуск трансляции игрового стола.

        Args:
            table_id (int): Идентификатор стола

        Returns:
            str: Подтверждение запуска
        """
        return f"Трансляция стола {table_id} запущена"

    def toggle_hints(self):
        """
        Включение/отключение подсказок.

        Returns:
            str: Статус подсказок
        """
        self.hints_enabled = not self.hints_enabled
        return "Подсказки включены" if self.hints_enabled else "Подсказки отключены"

    def place_bet(self, amount):
        """
        Размещение ставки.

        Args:
            amount (float): Размер ставки

        Returns:
            str: Подтверждение ставки
        """
        self.bet_amount = amount
        return f"Ставка {amount} размещена"

    def join_table(self, table_id):
        """
        Присоединение к игровому столу.

        Args:
            table_id (int): Идентификатор стола

        Returns:
            str: Подтверждение присоединения
        """
        self.active_tables.append(table_id)
        return f"Присоединение к столу {table_id}"

    def init_chat(self):
        """
        Инициализация чата с дилером.

        Returns:
            str: Подтверждение инициализации
        """
        return "Чат с дилером инициализирован"
