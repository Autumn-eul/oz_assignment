from banking_system.models.account import Account

class User:
    def __init__(self, username: str) -> None:
        self.username = username
        self.account = Account()