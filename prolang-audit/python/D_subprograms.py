"""Demonstrate Python subprogram features."""

from functools import reduce


def example_1_first_class_functions() -> None:
    """Store a function inside a variable."""

    def greet(name: str) -> str:
        """Return a greeting."""
        return f"hello, {name}"

    greeter = greet
    # Functions are first-class objects and can be reassigned like any other value.
    print("1. first-class function:", greeter("Python"))


def example_2_closures() -> None:
    """Show a closure capturing outer scope state."""

    def make_multiplier(factor: int):
        """Return a closure that multiplies by factor."""

        def multiply(value: int) -> int:
            """Multiply the incoming value using a captured outer variable."""
            return value * factor

        return multiply

    times_three = make_multiplier(3)
    # The inner function keeps access to factor after the outer call returns.
    print("2. closure:", times_three(5))


def factorial(number: int) -> int:
    """Compute factorial recursively."""
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def example_3_recursion() -> None:
    """Show recursion with factorial."""
    # Python supports direct recursive calls, though depth is bounded by the runtime.
    print("3. recursion:", factorial(5))


def sum_all(*values: int) -> int:
    """Add any number of integer arguments."""
    return sum(values)


def example_4_variadic_parameters() -> None:
    """Show *args variadic parameters."""
    # *args collects positional arguments into a tuple at call time.
    print("4. variadic parameters:", sum_all(1, 2, 3, 4))


def quotient_and_remainder(dividend: int, divisor: int) -> tuple[int, int]:
    """Return two values as a tuple."""
    return dividend // divisor, dividend % divisor


def example_5_multiple_return_values() -> None:
    """Show multiple values returned as a tuple."""
    quotient, remainder = quotient_and_remainder(17, 5)
    # Python packages multiple returns into a tuple and unpacks them naturally.
    print("5. multiple return values:", quotient, remainder)


def example_6_higher_order_functions() -> None:
    """Show map, filter, and reduce as higher-order functions."""
    numbers = [1, 2, 3, 4]
    doubled = list(map(lambda value: value * 2, numbers))
    filtered = list(filter(lambda value: value % 2 == 0, numbers))
    total = reduce(lambda left, right: left + right, numbers)
    # Python passes functions as values into reusable library algorithms.
    print("6. higher-order functions:", doubled, filtered, total)


def example_7_anonymous_functions() -> None:
    """Show a lambda expression."""
    square = lambda value: value * value
    # Lambda provides a compact anonymous function for small expressions.
    print("7. anonymous function:", square(6))


def main() -> None:
    """Run all subprogram examples."""
    example_1_first_class_functions()
    example_2_closures()
    example_3_recursion()
    example_4_variadic_parameters()
    example_5_multiple_return_values()
    example_6_higher_order_functions()
    example_7_anonymous_functions()


if __name__ == "__main__":
    main()
