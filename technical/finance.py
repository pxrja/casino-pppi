class Finance:
    def __init__(self):
        self.payment_systems = ['Visa', 'MasterCard', 'Crypto']
        self.transactions = []
        self.limits = {
            'min_deposit': 100,
            'max_deposit': 10000,
            'min_withdraw': 200
        }

    def deposit(self, user_id, amount, system):
        transaction = {
            'type': 'deposit',
            'user_id': user_id,
            'amount': amount,
            'system': system
        }
        self.transactions.append(transaction)
        return "Депозит успешно выполнен"

    def withdraw(self, user_id, amount):
        if amount > self.limits['min_withdraw']:
            return "Запрос на вывод средств создан"
        return "Сумма меньше минимальной"

    def calculate_commission(self, amount):
        if amount < 1000:
            return amount * 0.05  # 5% комиссия
        elif amount < 5000:
            return amount * 0.03  # 3% комиссия
        else:
            return amount * 0.02  # 2% комиссия