class Baccarat:
    """
    Класс для реализации игры в Баккара с поддержкой разных вариантов.

    Поддерживает два варианта игры: Punto Banco и Chemin de Fer,
    с различными правилами раздачи карт и подсчета очков.

    Methods:
        deal_cards(): Раздача карт в зависимости от варианта игры
        deal_punto_banco(): Раздача карт по правилам Punto Banco
        deal_chemin_de_fer(): Раздача карт по правилам Chemin de Fer
        assign_banker(): Назначение банкира для Chemin de Fer
        calculate_score(): Подсчет очков для обоих игроков
        calculate_hand(cards): Подсчет очков для одной руки

    Attributes:
        game_type (str): Вариант игры (Punto Banco/Chemin de Fer)
        current_hand (list): Текущая рука в игре
        banker_score (int): Очки банкира
        player_score (int): Очки игрока
        banker_cards (list): Карты банкира
        player_cards (list): Карты игрока
        current_banker (str): Текущий банкир для Chemin de Fer
    """

    def __init__(self, variant='Punto Banco'):
        """
        Инициализация игры в Баккара.

        Args:
            variant (str): Вариант игры (по умолчанию 'Punto Banco')
        """
        self.game_type = variant
        self.current_hand = []
        self.banker_score = 0
        self.player_score = 0
        self.banker_cards = []
        self.player_cards = []
        self.current_banker = None

    def deal_cards(self):
        """
        Раздача карт в соответствии с выбранным вариантом игры.

        Returns:
            str: Сообщение о результате раздачи
        """
        if self.game_type == 'Punto Banco':
            return self.deal_punto_banco()
        return self.deal_chemin_de_fer()

    def deal_punto_banco(self):
        """
        Раздача карт по правилам Punto Banco.

        Returns:
            str: Сообщение о раздаче карт
        """
        self.banker_cards = ['card1', 'card2']
        self.player_cards = ['card1', 'card2']
        return "Карты розданы в режиме Punto Banco"

    def deal_chemin_de_fer(self):
        """
        Раздача карт по правилам Chemin de Fer.

        Returns:
            str: Сообщение о раздаче карт
        """
        self.assign_banker()
        self.banker_cards = ['card1', 'card2']
        self.player_cards = ['card1', 'card2']
        return "Карты розданы в режиме Chemin de Fer"

    def assign_banker(self):
        """
        Назначение нового банкира для режима Chemin de Fer.

        Returns:
            str: Сообщение о назначении банкира
        """
        return "Назначен новый банкир"

    def calculate_score(self):
        """
        Подсчет очков для банкира и игрока.

        Returns:
            str: Строка с результатами подсчета очков
        """
        self.banker_score = self.calculate_hand(self.banker_cards)
        self.player_score = self.calculate_hand(self.player_cards)
        return f"Счет: Банкир {self.banker_score}, Игрок {self.player_score}"

    def calculate_hand(self, cards):
        """
        Подсчет очков для одной руки.

        Args:
            cards (list): Список карт в руке

        Returns:
            int: Сумма очков по модулю 10
        """
        return sum([card.value for card in cards]) % 10
