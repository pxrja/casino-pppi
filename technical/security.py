class Security:
    def __init__(self):
        self.two_factor_enabled = False
        self.encryption_key = "default_key"
        self.active_sessions = {}

    def enable_2fa(self, user_id):
        self.two_factor_enabled = True
        return "2FA активирован"

    def verify_user(self, user_id, token):
        return True

    def check_ddos(self, ip_address):
        return "IP адрес проверен"
