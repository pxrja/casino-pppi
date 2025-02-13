class UserInterface:
    def __init__(self):
        self.language = 'ru'
        self.theme = 'dark'
        self.device = 'desktop'

    def change_language(self, lang):
        self.language = lang
        return f"Язык изменен на {lang}"

    def change_theme(self, new_theme):
        self.theme = new_theme
        return f"Тема изменена на {new_theme}"

    def init_chat(self):
        return "Чат с дилером инициализирован"
