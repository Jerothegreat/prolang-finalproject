"""Demonstrate Python object-oriented programming features."""


class Report:
    """A class with methods and encapsulated state."""

    def __init__(self, title: str) -> None:
        """Initialize a report with a title."""
        self.title = title
        self._status = "draft"

    def publish(self) -> None:
        """Update the report status."""
        self._status = "published"

    def describe(self) -> str:
        """Return a user-facing description."""
        return f"{self.title} [{self._status}]"


class Vehicle:
    """Base class for inheritance examples."""

    def move(self) -> str:
        """Describe generic movement."""
        return "vehicle moves"


class Car(Vehicle):
    """Derived class overriding a base method."""

    def move(self) -> str:
        """Describe car-specific movement."""
        return "car drives"


class EmailSender:
    """A class used for duck-typed behavior."""

    def send(self) -> str:
        """Return a channel-specific message."""
        return "email sent"


class SmsSender:
    """Another class used for duck-typed behavior."""

    def send(self) -> str:
        """Return a channel-specific message."""
        return "sms sent"


class TimeStampedMixin:
    """Provide timestamp behavior for multiple inheritance."""

    def stamp(self) -> str:
        """Return a timestamp label."""
        return "2026-05-23"


class AuditMixin:
    """Provide audit behavior for multiple inheritance."""

    def record(self) -> str:
        """Return an audit label."""
        return "audit recorded"


class AuditReport(TimeStampedMixin, AuditMixin, Report):
    """Combine behaviors through Python's MRO."""


class ComparableReport:
    """Implement dunder methods for object protocols."""

    def __init__(self, title: str, pages: int) -> None:
        """Initialize the comparable report."""
        self.title = title
        self.pages = pages

    def __str__(self) -> str:
        """Return a readable string form."""
        return f"{self.title} ({self.pages} pages)"

    def __eq__(self, other: object) -> bool:
        """Compare two report objects by value."""
        if not isinstance(other, ComparableReport):
            return NotImplemented
        return (self.title, self.pages) == (other.title, other.pages)


class SecureReport:
    """Demonstrate encapsulation within an object."""

    def __init__(self, title: str, access_code: str) -> None:
        """Initialize protected report data."""
        self.title = title
        self._access_code = access_code

    def can_open(self, provided_code: str) -> bool:
        """Compare the caller's code with encapsulated state."""
        return provided_code == self._access_code


def notify(sender) -> str:
    """Use duck typing by calling a shared method name."""
    return sender.send()


def example_1_class_with_methods() -> None:
    """Show a class definition with methods."""
    report = Report("Language Audit")
    report.publish()
    # Methods bind behavior to objects while keeping state on self.
    print("1. class with methods:", report.describe())


def example_2_inheritance() -> None:
    """Show class inheritance."""
    car = Car()
    # Python inheritance reuses base-class contracts through subclassing.
    print("2. inheritance:", car.move(), isinstance(car, Vehicle))


def example_3_method_overriding() -> None:
    """Show a subclass overriding a parent method."""
    base = Vehicle()
    derived = Car()
    # Dynamic dispatch selects the subclass implementation at runtime.
    print("3. method overriding:", base.move(), "vs", derived.move())


def example_4_polymorphism() -> None:
    """Show duck-typed polymorphism."""
    # Python cares about the presence of send(), not a declared interface type.
    print("4. polymorphism:", notify(EmailSender()), notify(SmsSender()))


def example_5_multiple_inheritance() -> None:
    """Show multiple inheritance and MRO."""
    audit_report = AuditReport("Composite Report")
    # Multiple inheritance composes behavior, and MRO resolves method lookup order.
    print("5. multiple inheritance:", audit_report.stamp(), audit_report.record())


def example_6_dunder_methods() -> None:
    """Show special methods such as __str__ and __eq__."""
    left = ComparableReport("Status", 10)
    right = ComparableReport("Status", 10)
    # Dunder methods integrate objects with Python's core protocols.
    print("6. dunder methods:", str(left), left == right)


def example_7_encapsulation() -> None:
    """Show object-level encapsulation."""
    report = SecureReport("Restricted", "1234")
    # Methods expose controlled access while keeping internals behind an API.
    print("7. encapsulation:", report.can_open("0000"), report.can_open("1234"))


def main() -> None:
    """Run all OOP examples."""
    example_1_class_with_methods()
    example_2_inheritance()
    example_3_method_overriding()
    example_4_polymorphism()
    example_5_multiple_inheritance()
    example_6_dunder_methods()
    example_7_encapsulation()


if __name__ == "__main__":
    main()
