class UserInterface:
    def __init__(self):
        self.language = 'ru'
        self.theme = 'dark'
        self.device = 'desktop'
        self.current_game = None
        self.bet_amount = 0
        self.active_tables = []
        self.hints_enabled = True

    def change_language(self, lang):
        self.language = lang
        return f"Язык изменен на {lang}"

    def change_theme(self, new_theme):
        self.theme = new_theme
        return f"Тема изменена на {new_theme}"

    def adapt_to_device(self, device_type):
        self.device = device_type
        return f"Интерфейс адаптирован под {device_type}"

    def navigate_games(self, game_type):
        self.current_game = game_type
        return f"Переход к игре {game_type}"

    def start_stream(self, table_id):
        return f"Трансляция стола {table_id} запущена"

    def toggle_hints(self):
        self.hints_enabled = not self.hints_enabled
        return "Подсказки включены" if self.hints_enabled else "Подсказки отключены"

    def place_bet(self, amount):
        self.bet_amount = amount
        return f"Ставка {amount} размещена"

    def join_table(self, table_id):
        self.active_tables.append(table_id)
        return f"Присоединение к столу {table_id}"

    def init_chat(self):
        return "Чат с дилером инициализирован"
