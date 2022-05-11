import pytest

from app.calculations import add, multiply, divide, BankAccount, InsufficientFunds

# decorator for creating fixtures that can be reused
@pytest.fixture
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account_10():
    return BankAccount(10)


@pytest.fixture
def bank_account_100():
    return BankAccount(100)


@pytest.fixture
def bank_account_1000():
    return BankAccount(1000)


# decorator from pytest library
@pytest.mark.parametrize(
    "num1, num2, result",
    [
        (3, 2, 5),
        (7, 4, 11),
        (5, 7, 12),
    ],
)
def test_add(num1, num2, result):
    print("testing add function")
    assert add(num1, num2) == result


def test_multiply():
    print("testing mutliply function")
    assert multiply(5, 8) == 40


def test_divide():
    print("testing divide function")
    assert divide(5, 8) < 1


@pytest.mark.parametrize(
    "account, starting_balance, opening_balance",
    [("acc #1", 100, 100), ("acct #2", 1000, 1000), ("acct #3", 140, 140)],
)
def test_bankstartingbalance(account: str, starting_balance: int, opening_balance: int):
    print("testing bank starting balance")
    account = BankAccount(starting_balance)
    assert account.balance == opening_balance


@pytest.mark.parametrize(
    "account, starting_balance, withdrawal_amount, post_withdrawal_balance",
    [("acc #1", 100, 10, 90), ("acct #2", 100, 20, 80), ("acct #3", 500, 25, 475)],
)
def test_withdraw(
    account, starting_balance, withdrawal_amount, post_withdrawal_balance
):
    print("testing withdraw function")
    account = BankAccount(starting_balance)
    account.withdraw(withdrawal_amount)
    assert account.balance == post_withdrawal_balance


@pytest.mark.parametrize(
    "account, starting_balance, deposit_amount, post_deposit_balance",
    [("acct #1", 10, 10, 20), ("acct #2", 15, 20, 35)],
)
def test_deposit(
    account: str, starting_balance: int, deposit_amount: int, post_deposit_balance: int
):
    print("testing deposit function")
    account = BankAccount(starting_balance)
    account.deposit(deposit_amount)
    assert account.balance == post_deposit_balance


@pytest.mark.parametrize(
    "account, starting_balance, ending_balance",
    [("acct #1", 10, 11), ("acct #2", 100, 110)],
)
def test_collect_interest(account, starting_balance, ending_balance):
    print("testing collect interest")
    account = BankAccount(starting_balance)
    account.collect_interest()
    assert round(account.balance) == ending_balance


def test_zero_bank_account(zero_bank_account):
    assert zero_bank_account.balance == 0


def test_bank_account_10(bank_account_10):
    assert bank_account_10.balance == 10


def test_bank_account_100(bank_account_100):
    assert bank_account_100.balance == 100


def test_bank_account_1000(bank_account_1000):
    assert bank_account_1000.balance == 1000


@pytest.mark.parametrize(
    "starting_balance, deposit_amount, withdrawal_amount, post_withdrawal_balance",
    [(0, 100, 50, 50), (0, 2, 1, 1), (0, 500, 300, 200)],
)
def test_bank_transaction(
    zero_bank_account,
    starting_balance,
    deposit_amount,
    withdrawal_amount,
    post_withdrawal_balance,
):
    assert zero_bank_account.balance == starting_balance
    zero_bank_account.deposit(deposit_amount)
    zero_bank_account.withdraw(withdrawal_amount)
    assert zero_bank_account.balance == post_withdrawal_balance


def test_insufficient_funds(bank_account_1000):
    with pytest.raises(InsufficientFunds):
        bank_account_1000.withdraw(1001)
