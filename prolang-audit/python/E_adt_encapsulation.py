"""Demonstrate Python ADTs and encapsulation techniques."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

_MODULE_TAX_RATE = 0.12


def _apply_tax(amount: float) -> float:
    """Apply the module-level tax rate to an amount."""
    return amount * (1 + _MODULE_TAX_RATE)


class BankAccount:
    """A simple custom ADT implemented as a Python class."""

    def __init__(self, owner: str, balance: float) -> None:
        """Initialize the account state."""
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: float) -> None:
        """Add funds to the account."""
        self._balance += amount

    @property
    def balance(self) -> float:
        """Return the private balance value."""
        return self._balance

    @balance.setter
    def balance(self, new_balance: float) -> None:
        """Validate balance updates through a property setter."""
        if new_balance < 0:
            raise ValueError("balance cannot be negative")
        self._balance = new_balance


class Processor(ABC):
    """Define an interface-like contract using an abstract base class."""

    @abstractmethod
    def process(self, amount: float) -> str:
        """Process a payment amount."""


class CardProcessor(Processor):
    """Implement the processor contract."""

    def process(self, amount: float) -> str:
        """Return a simple payment status."""
        return f"processed {amount:.2f}"


def make_account(owner: str, opening_balance: float) -> BankAccount:
    """Create an account using a constructor helper."""
    return BankAccount(owner, opening_balance)


@dataclass(frozen=True)
class ImmutablePoint:
    """Represent an immutable value object."""

    x: int
    y: int


def example_1_custom_adt() -> None:
    """Show a class acting as a custom ADT."""
    account = BankAccount("Ari", 1000.0)
    account.deposit(250.0)
    # A class groups data and related behavior into one reusable abstraction.
    print("1. custom ADT:", account.owner, account.balance)


def example_2_private_fields() -> None:
    """Show the underscore convention for private state."""
    account = BankAccount("Bea", 500.0)
    # Python privacy is conventional; _balance signals non-public intent.
    print("2. private field convention:", hasattr(account, "_balance"))


def example_3_getters_setters() -> None:
    """Show @property getter and setter behavior."""
    account = BankAccount("Cal", 300.0)
    account.balance = 450.0
    # @property keeps attribute syntax while routing access through methods.
    print("3. property access:", account.balance)


def example_4_module_level_encapsulation() -> None:
    """Show module-level hidden helpers."""
    taxed = _apply_tax(100.0)
    # Leading underscores also document module-level implementation details.
    print("4. module encapsulation:", round(taxed, 2))


def example_5_interface_contract() -> None:
    """Show an abstract base class contract."""
    processor = CardProcessor()
    # ABCs model required behavior without enforcing a single concrete class.
    print("5. interface contract:", processor.process(199.99))


def example_6_constructor_pattern() -> None:
    """Show a constructor helper wrapping class initialization."""
    account = make_account("Dia", 725.0)
    # Factory helpers can centralize initialization rules around __init__.
    print("6. constructor pattern:", account.owner, account.balance)


def example_7_immutability() -> None:
    """Show a frozen dataclass as an immutable object."""
    point = ImmutablePoint(4, 9)
    # frozen=True prevents attribute reassignment after construction.
    print("7. immutability:", point)


def main() -> None:
    """Run all ADT and encapsulation examples."""
    example_1_custom_adt()
    example_2_private_fields()
    example_3_getters_setters()
    example_4_module_level_encapsulation()
    example_5_interface_contract()
    example_6_constructor_pattern()
    example_7_immutability()


if __name__ == "__main__":
    main()
