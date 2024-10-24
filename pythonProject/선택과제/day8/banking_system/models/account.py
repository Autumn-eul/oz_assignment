from banking_system.models.transaction import Transaction
from banking_system.utils.decorators import validate_transaction
from banking_system.utils.exceptions import InsufficientFundsError, NegativeAmountError


class Account:
    bank_name = "MyBank"  # 클래스 변수

    def __init__(self) -> None:
        self.__balance = 1000
        self.transactions = []

    @validate_transaction
    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        self.__balance += amount
        self.transactions.append(Transaction("입금", amount, self.__balance))

    @validate_transaction
    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        if amount > self.__balance:
            raise InsufficientFundsError(self.__balance)
        self.__balance -= amount
        self.transactions.append(Transaction("출금", amount, self.__balance))

    def get_balance(self) -> int:
        return self.__balance

    def get_transactions(self) -> list:
        return self.transactions

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name

    @classmethod
    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name
