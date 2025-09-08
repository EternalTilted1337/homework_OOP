class Bank:
    def __init__(self):
        self.account = {}

    def new_score(self,name_client,start_balance=0):
        self.account[name_client] = start_balance

    def find_score(self,name_client):
        for client, balance in self.account.items():
            if client==name_client:
                return client,balance
        return None

    def transfer_money(self,from_client,to_client,value):
        from_score = self.find_score(from_client)
        to_score = self.find_score(to_client)

        if from_score is None:
            raise ValueError('Счет отправителя не существует')
        if to_score is None:
            raise ValueError("Счёт получателя не найден")
        if from_score[1] >= value:
            self.account[from_client] -= value
            self.account[to_client] += value
        else:
            raise ValueError('На вашем счету не достаточно ДЕНЕХ')

#Тесты прописаны, тесты прошел. Вроде все норм
class BankAccount:
    def __init__(self,account_id,owner,balance=0):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        if amount <=0:
            raise ValueError('Пополнение должны быть больше 0')

        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError ('Сумма снятия должна быть > 0')
        if amount > self.balance:
            raise ValueError ('Сумма снятия не должна превышать баланс')
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance



