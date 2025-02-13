class Blackjack:
    """
    Класс для реализации игры в Блэкджек с поддержкой разных вариантов.

    Поддерживает американский и европейский варианты игры,
    включая различные правила раздачи карт и страховку.

    Methods:
        hit(): Добор дополнительной карты игроком
        stand(): Завершение хода игрока
        deal_initial_cards(): Начальная раздача карт
        deal_american(): Раздача по американским правилам
        deal_european(): Раздача по европейским правилам
        offer_insurance(): Предложение страховки
        check_blackjack(): Проверка на блэкджек

    Attributes:
        game_type (str): Вариант игры (American/European)
        player_hand (list): Карты игрока
        dealer_hand (list): Карты дилера
        deck (list): Игровая колода
        insurance (bool): Статус страховки
        bet_amount (float): Размер ставки
        insurance_amount (float): Размер страховки
    """

    def __init__(self, variant='American'):
        """
        Инициализация игры в Блэкджек.

        Args:
            variant (str): Вариант игры (по умолчанию 'American')
        """
        self.game_type = variant
        self.player_hand = []
        self.dealer_hand = []
        self.deck = []
        self.insurance = False
        self.bet_amount = 0
        self.insurance_amount = 0

    def hit(self):
        """
        Добор дополнительной карты игроком.

        Returns:
            str: Сообщение о выдаче карты
        """
        card = self.deck.pop()
        self.player_hand.append(card)
        return "Выдана дополнительная карта"

    def stand(self):
        """
        Завершение хода игрока.

        Returns:
            str: Сообщение о завершении хода
        """
        return "Игрок остановился"

    def deal_initial_cards(self):
        """
        Начальная раздача карт в зависимости от варианта игры.

        Returns:
            str: Сообщение о результате раздачи
        """
        if self.game_type == 'American':
            return self.deal_american()
        return self.deal_european()

    def deal_american(self):
        """
        Раздача карт по американским правилам.

        Returns:
            str: Сообщение о раздаче карт
        """
        return "Карты розданы по американским правилам"

    def deal_european(self):
        """
        Раздача карт по европейским правилам.

        Returns:
            str: Сообщение о раздаче карт
        """
        return "Карты розданы по европейским правилам"

    def offer_insurance(self):
        """
        Предложение страховки при тузе у дилера.

        Returns:
            str: Сообщение о доступности страховки
        """
        if self.dealer_hand[0].rank == 'A':
            self.insurance_amount = self.bet_amount / 2
            return "Предложена страховка"
        return "Страховка недоступна"

    def check_blackjack(self):
        """
        Проверка комбинации на блэкджек.

        Returns:
            bool: True если сумма карт равна 21
        """
        return sum([card.value for card in self.player_hand]) == 21
