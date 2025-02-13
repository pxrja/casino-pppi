class Finance:
    """
    Класс для управления финансовыми операциями и платежными системами.

    Обеспечивает полный цикл управления финансами: депозиты, выводы средств,
    бонусную систему, историю транзакций и настройку платежных систем.

    Methods:
        deposit(user_id, amount, system): Создание депозита с начислением бонуса
        withdraw(user_id, amount, system): Создание запроса на вывод средств
        calculate_bonus(amount, bonus_type): Расчет бонуса для операции
        get_transaction_history(user_id, filter_type): Получение истории транзакций
        update_limits(limit_type, new_value): Обновление лимитов операций
        add_payment_system(name, commission): Добавление новой платежной системы

    Attributes:
        payment_systems (dict): Словарь платежных систем с их настройками
        transactions (list): История всех финансовых операций
        limits (dict): Ограничения на финансовые операции
        bonus_system (dict): Настройки бонусной программы
    """
    def __init__(self):
        """
        Инициализация финансового модуля с расширенными настройками.
        """
        self.payment_systems = {
            'Visa': {'enabled': True, 'commission': 0.02},
            'MasterCard': {'enabled': True, 'commission': 0.02},
            'Crypto': {'enabled': True, 'commission': 0.01},
            'WebMoney': {'enabled': True, 'commission': 0.03}
        }
        self.transactions = []
        self.limits = {
            'min_deposit': 100,
            'max_deposit': 10000,
            'min_withdraw': 200,
            'daily_limit': 50000
        }
        self.bonus_system = {
            'welcome': 100,
            'deposit': 0.1,  # 10% от депозита
            'loyalty': 0.05  # 5% кэшбэк
        }

    def deposit(self, user_id, amount, system):
        """
        Создание депозита с начислением бонуса.

        Args:
            user_id (int): Идентификатор пользователя
            amount (float): Сумма депозита
            system (str): Используемая платежная система

        Returns:
            str: Сообщение о статусе операции и начисленном бонусе
        """
        if self.validate_deposit(amount, system):
            bonus = self.calculate_bonus(amount, 'deposit')
            transaction = {
                'type': 'deposit',
                'user_id': user_id,
                'amount': amount,
                'system': system,
                'bonus': bonus,
                'timestamp': 'current_time'
            }
            self.transactions.append(transaction)
            return f"Депозит выполнен. Начислен бонус: {bonus}"
        return "Ошибка депозита"

    def withdraw(self, user_id, amount, system):
        """
         Создание запроса на вывод средств.

         Args:
             user_id (int): Идентификатор пользователя
             amount (float): Сумма для вывода
             system (str): Платежная система для вывода

         Returns:
             str: Сообщение о статусе операции
        """
        if self.validate_withdrawal(user_id, amount):
            transaction = {
                'type': 'withdraw',
                'user_id': user_id,
                'amount': amount,
                'system': system,
                'timestamp': 'current_time'
            }
            self.transactions.append(transaction)
            return "Запрос на вывод создан"
        return "Ошибка вывода средств"

    def calculate_bonus(self, amount, bonus_type):
        """
        Расчет бонуса для указанной операции.

        Args:
            amount (float): Сумма операции
            bonus_type (str): Тип бонуса

        Returns:
            float: Сумма начисленного бонуса
        """
        return amount * self.bonus_system[bonus_type]

    def get_transaction_history(self, user_id, filter_type=None):
        """
        Получение истории транзакций пользователя.

        Args:
            user_id (int): Идентификатор пользователя
            filter_type (str, optional): Тип транзакций для фильтрации

        Returns:
            list: Список транзакций пользователя
        """
        if filter_type:
            return [t for t in self.transactions
                   if t['user_id'] == user_id and t['type'] == filter_type]
        return [t for t in self.transactions if t['user_id'] == user_id]

    def update_limits(self, limit_type, new_value):
        """
        Обновление лимитов операций.

        Args:
            limit_type (str): Тип лимита
            new_value (float): Новое значение лимита

        Returns:
            str: Сообщение об обновлении
        """
        self.limits[limit_type] = new_value
        return f"Лимит {limit_type} обновлен"

    def add_payment_system(self, name, commission):
        """
        Добавление новой платежной системы.

        Args:
            name (str): Название платежной системы
            commission (float): Комиссия системы

        Returns:
            str: Сообщение о добавлении системы
        """
        self.payment_systems[name] = {
            'enabled': True,
            'commission': commission
        }
        return f"Добавлена платежная система {name}"
