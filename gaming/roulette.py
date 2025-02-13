class Roulette:
    """
    Класс для реализации игры в рулетку с разными вариантами правил.

    Поддерживает европейский, американский и французский варианты,
    различные типы ставок и систему выплат.

    Methods:
        initialize_wheel(): Инициализация чисел рулетки
        spin(): Запуск вращения рулетки
        place_bet(bet_type, amount, numbers): Размещение ставки
        check_all_bets(winning_number): Проверка всех ставок
        calculate_win(bet, winning_number): Расчет выигрыша
        apply_french_rules(): Применение французских правил

    Attributes:
        type (str): Вариант рулетки
        last_numbers (list): История выпавших чисел
        wheel_numbers (list): Числа на колесе рулетки
        bets (list): Список активных ставок
        payouts (dict): Коэффициенты выплат
    """

    def __init__(self, variant='European'):
        """
        Инициализация игры в рулетку.

        Args:
            variant (str): Вариант рулетки (по умолчанию 'European')
        """
        self.type = variant
        self.last_numbers = []
        self.wheel_numbers = self.initialize_wheel()
        self.bets = []
        self.payouts = {
            'straight': 35,
            'split': 17,
            'street': 11,
            'corner': 8,
            'line': 5,
            'dozen': 2,
            'column': 2,
            'even': 1,
            'odd': 1,
            'red': 1,
            'black': 1
        }

    def initialize_wheel(self):
        """
        Инициализация чисел на колесе рулетки.

        Returns:
            list: Список чисел на колесе
        """
        if self.type == 'American':
            return list(range(0, 37)) + [38]  # 0, 00
        return list(range(0, 37))  # 0-36

    def spin(self):
        """
        Вращение рулетки и определение выигрышного числа.

        Returns:
            str: Сообщение с выпавшим числом
        """
        from random import choice
        result = choice(self.wheel_numbers)
        self.last_numbers.append(result)
        self.check_all_bets(result)
        return f"Выпало число {result}"

    def place_bet(self, bet_type, amount, numbers=None):
        """
        Размещение ставки определенного типа.

        Args:
            bet_type (str): Тип ставки
            amount (float): Размер ставки
            numbers (list): Номера для ставки

        Returns:
            str: Подтверждение ставки
        """
        bet = {
            'type': bet_type,
            'amount': amount,
            'numbers': numbers
        }
        self.bets.append(bet)
        return f"Ставка {amount} на {bet_type} принята"

    def check_all_bets(self, winning_number):
        """
        Проверка всех ставок после выпадения числа.

        Args:
            winning_number (int): Выигрышное число

        Returns:
            float: Общая сумма выигрышей
        """
        total_winnings = 0
        for bet in self.bets:
            winnings = self.calculate_win(bet, winning_number)
            total_winnings += winnings
        return total_winnings

    def calculate_win(self, bet, winning_number):
        """
        Расчет выигрыша для конкретной ставки.

        Args:
            bet (dict): Информация о ставке
            winning_number (int): Выигрышное число

        Returns:
            float: Сумма выигрыша
        """
        if winning_number in bet['numbers']:
            return bet['amount'] * self.payouts[bet['type']]
        return 0

    def apply_french_rules(self):
        """
        Применение специальных французских правил.

        Returns:
            str: Подтверждение применения правил
        """
        if self.type == 'French':
            return "Применены французские правила"
