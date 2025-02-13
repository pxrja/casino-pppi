class Support:
    def __init__(self):
        self.tickets = []
        self.faq = {
            'deposit': 'Как внести депозит?',
            'withdraw': 'Как вывести средства?'
        }

    def create_ticket(self, user_id, message):
        ticket = {
            'id': len(self.tickets) + 1,
            'user_id': user_id,
            'message': message,
            'status': 'open'
        }
        self.tickets.append(ticket)
        return ticket['id']

    def get_faq(self):
        return self.faq
