from banking_system.models.user import User
from banking_system.utils.exceptions import UserNotFoundError

class BankingService:
    def __init__(self) -> None:
        self.users = []

    def add_user(self, username: str) -> None:
        self.users.append(User(username))

    def find_user(self, username: str) -> User:
        for user in self.users:
            if user.username == username:
                return user
        raise UserNotFoundError(username)

    def user_menu(self, username: str) -> None:
        user = self.find_user(username)

        while True:
            try:
                choice = input("원하는 작업을 선택하세요 (1: 입금, 2: 출금, 3: 잔고 확인, 4: 거래 내역, 5: 종료): ")
                if choice == '1':
                    amount = int(input("입금할 금액을 입력하세요: "))
                    user.account.deposit(amount)
                elif choice == '2':
                    amount = int(input("출금할 금액을 입력하세요: "))
                    user.account.withdraw(amount)
                elif choice == '3':
                    print(f"현재 잔고는 {user.account.get_balance()}원 입니다.")
                elif choice == '4':
                    for transaction in user.account.get_transactions():
                        print(transaction)
                elif choice == '5':
                    break
                else:
                    print("잘못된 입력입니다. 다시 시도하세요.")
            except ValueError as e:
                print(f"잘못된 입력입니다: {e}")
            except InsufficientFundsError as e:
                print(f"오류: {e}")
            except NegativeAmountError as e:
                print(f"오류: {e}")
            except UserNotFoundError as e:
                print(f"오류: {e}")
