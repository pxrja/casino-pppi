class Support:
    def __init__(self):
        self.tickets = []
        self.chat_history = {}
        self.knowledge_base = {
            'games': 'Правила всех игр',
            'security': 'Безопасность аккаунта',
            'payments': 'Финансовые операции'
        }
        self.faq = {
            'deposit': 'Как внести депозит?',
            'withdraw': 'Как вывести средства?',
            'verification': 'Как пройти верификацию?',
            'bonus': 'Как получить бонус?'
        }

    def create_ticket(self, user_id, message, priority='normal'):
        ticket = {
            'id': len(self.tickets) + 1,
            'user_id': user_id,
            'message': message,
            'status': 'open',
            'priority': priority,
            'created_at': 'timestamp'
        }
        self.tickets.append(ticket)
        return ticket['id']

    def send_chat_message(self, user_id, message):
        if user_id not in self.chat_history:
            self.chat_history[user_id] = []
        self.chat_history[user_id].append(message)
        return "Сообщение отправлено"

    def get_chat_history(self, user_id):
        return self.chat_history.get(user_id, [])

    def update_ticket_status(self, ticket_id, new_status):
        for ticket in self.tickets:
            if ticket['id'] == ticket_id:
                ticket['status'] = new_status
                return f"Тикет {ticket_id} обновлен"

    def search_knowledge_base(self, query):
        return [topic for topic, content in self.knowledge_base.items()
                if query.lower() in content.lower()]

    def get_faq(self, category=None):
        if category:
            return {k: v for k, v in self.faq.items() if k.startswith(category)}
        return self.faq
