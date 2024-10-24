class InsufficientFundsError(Exception):
    def __init__(self, balance: int) -> None:
        super().__init__(f"잔액이 부족합니다. 현재 잔고: {balance}원")

class NegativeAmountError(Exception):
    def __init__(self) -> None:
        super().__init__("음수 금액은 허용되지 않습니다.")

class UserNotFoundError(Exception):
    def __init__(self, username: str) -> None:
        super().__init__(f"사용자를 찾을 수 없습니다: {username}")