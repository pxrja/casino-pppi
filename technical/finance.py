class Finance:
    def __init__(self):
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
        return amount * self.bonus_system[bonus_type]

    def get_transaction_history(self, user_id, filter_type=None):
        if filter_type:
            return [t for t in self.transactions
                   if t['user_id'] == user_id and t['type'] == filter_type]
        return [t for t in self.transactions if t['user_id'] == user_id]

    def update_limits(self, limit_type, new_value):
        self.limits[limit_type] = new_value
        return f"Лимит {limit_type} обновлен"

    def add_payment_system(self, name, commission):
        self.payment_systems[name] = {
            'enabled': True,
            'commission': commission
        }
        return f"Добавлена платежная система {name}"
