import pytest
from Bank_Class_for_Managing_Custome_Accounts_and_Transactions import BankAccount, Bank

def test_initial_balance_default():
    acc = BankAccount(1, 'Misha')
    assert acc.get_balance() == 0

def test_deposit_increases_balance_and_returns_new():
    acc = BankAccount(1, 'Misha')
    assert acc.deposit(1000) == 1000
    assert acc.get_balance() == 1000

@pytest.mark.parametrize("amount", [0, -1, -100])
def test_deposit_invalid_amount_raises(amount):
    acc = BankAccount(1, 'Misha')
    with pytest.raises(ValueError):
        acc.deposit(amount)

def test_withdraw_ok():
    acc = BankAccount(1, 'Misha', balance=1000)
    assert acc.withdraw(600) == 400
    assert acc.get_balance() == 400

def test_withdraw_all_to_zero():
    acc = BankAccount(1, 'Misha', balance=1000)
    assert acc.withdraw(1000) == 0
    assert acc.get_balance() == 0

def test_withdraw_insufficient_raises_and_keeps_balance():
    acc = BankAccount(1, 'Misha', balance=1000)
    with pytest.raises(ValueError):
        acc.withdraw(1001)
    assert acc.get_balance() == 1000








@pytest.fixture
def bank():
    return Bank()


def test_new_score_creates_account_with_default_zero(bank):
    bank.new_score("Misha")
    assert "Misha" in bank.account
    assert bank.account["Misha"] == 0
    assert bank.find_score("Misha") == ("Misha", 0)


def test_new_score_creates_account_with_initial_balance(bank):
    bank.new_score("Alice", 500)
    assert bank.account["Alice"] == 500
    assert bank.find_score("Alice") == ("Alice", 500)


def test_find_score_returns_none_if_not_found(bank):
    assert bank.find_score("Ghost") is None


def test_transfer_success_updates_both_balances(bank):
    bank.new_score("Alice", 500)
    bank.new_score("Bob", 200)

    bank.transfer_money("Alice", "Bob", 300)

    assert bank.account["Alice"] == 200
    assert bank.account["Bob"] == 500


def test_transfer_sender_missing_raises_and_no_change(bank):
    bank.new_score("Bob", 200)

    with pytest.raises(ValueError) as exc:
        bank.transfer_money("Ghost", "Bob", 100)

    # сообщение может отличаться по "е/ё", проверяем по ключевому слову
    assert "отправителя" in str(exc.value)
    assert bank.account["Bob"] == 200  # баланс не изменился


def test_transfer_receiver_missing_raises_and_no_change(bank):
    bank.new_score("Alice", 500)

    with pytest.raises(ValueError) as exc:
        bank.transfer_money("Alice", "Ghost", 100)

    assert "получателя" in str(exc.value)
    assert bank.account["Alice"] == 500  # баланс не изменился


def test_transfer_insufficient_funds_raises_and_no_change(bank):
    bank.new_score("Alice", 100)
    bank.new_score("Bob", 200)

    with pytest.raises(ValueError) as exc:
        bank.transfer_money("Alice", "Bob", 150)

    assert "не достаточно" in str(exc.value) or "недостаточно" in str(exc.value).lower()
    assert bank.account["Alice"] == 100
    assert bank.account["Bob"] == 200