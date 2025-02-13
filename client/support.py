class Support:
    """
    Класс для управления службой поддержки пользователей.

    Обеспечивает работу с тикетами, чатом поддержки,
    базой знаний и часто задаваемыми вопросами.

    Methods:
        create_ticket(user_id, message, priority): Создание тикета поддержки
        send_chat_message(user_id, message): Отправка сообщения в чат
        get_chat_history(user_id): Получение истории чата
        update_ticket_status(ticket_id, new_status): Обновление статуса тикета
        search_knowledge_base(query): Поиск по базе знаний
        get_faq(category): Получение FAQ по категории

    Attributes:
        tickets (list): Список тикетов поддержки
        chat_history (dict): История чатов пользователей
        knowledge_base (dict): База знаний
        faq (dict): Часто задаваемые вопросы
    """

    def __init__(self):
        """
        Инициализация системы поддержки.
        """
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
        """
        Создание нового тикета поддержки.

        Args:
            user_id (int): Идентификатор пользователя
            message (str): Сообщение пользователя
            priority (str): Приоритет тикета

        Returns:
            int: Идентификатор созданного тикета
        """
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
        """
        Отправка сообщения в чат поддержки.

        Args:
            user_id (int): Идентификатор пользователя
            message (str): Текст сообщения

        Returns:
            str: Подтверждение отправки
        """
        if user_id not in self.chat_history:
            self.chat_history[user_id] = []
        self.chat_history[user_id].append(message)
        return "Сообщение отправлено"

    def get_chat_history(self, user_id):
        """
        Получение истории чата пользователя.

        Args:
            user_id (int): Идентификатор пользователя

        Returns:
            list: История сообщений
        """
        return self.chat_history.get(user_id, [])

    def update_ticket_status(self, ticket_id, new_status):
        """
        Обновление статуса тикета.

        Args:
            ticket_id (int): Идентификатор тикета
            new_status (str): Новый статус

        Returns:
            str: Подтверждение обновления
        """
        for ticket in self.tickets:
            if ticket['id'] == ticket_id:
                ticket['status'] = new_status
                return f"Тикет {ticket_id} обновлен"

    def search_knowledge_base(self, query):
        """
        Поиск информации в базе знаний.

        Args:
            query (str): Поисковый запрос

        Returns:
            list: Найденные темы
        """
        return [topic for topic, content in self.knowledge_base.items()
                if query.lower() in content.lower()]

    def get_faq(self, category=None):
        """
        Получение списка FAQ.

        Args:
            category (str, optional): Категория вопросов

        Returns:
            dict: Список вопросов и ответов
        """
        if category:
            return {k: v for k, v in self.faq.items() if k.startswith(category)}
        return self.faq
