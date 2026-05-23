"""Demonstrate Python expressions and assignment statements."""


def side_effect_check(label: str, result: bool) -> bool:
    """Print when a boolean helper is evaluated."""
    print(f"   evaluating {label}")
    return result


def compute_pair() -> tuple[int, int]:
    """Return two numbers for destructuring."""
    return 7, 11


def example_1_arithmetic_precedence() -> None:
    """Show arithmetic operators with precedence rules."""
    value = 2 + 3 * 4
    grouped = (2 + 3) * 4
    # Multiplication binds tighter than addition unless parentheses override it.
    print("1. arithmetic precedence:", value, grouped)


def example_2_boolean_short_circuit() -> None:
    """Show Python short-circuiting boolean expressions."""
    # The second helper is skipped because the first operand is already False.
    result = side_effect_check("left", False) and side_effect_check("right", True)
    print("2. short circuit result:", result)


def example_3_ternary_expression() -> None:
    """Show Python's inline conditional expression."""
    score = 85
    # Python offers a built-in expression form: X if condition else Y.
    remark = "pass" if score >= 75 else "fail"
    print("3. ternary expression:", remark)


def example_4_augmented_assignment() -> None:
    """Show augmented assignment operators."""
    total = 10
    # Augmented assignment updates the bound object reference succinctly.
    total += 5
    total *= 2
    total -= 4
    print("4. augmented assignment:", total)


def example_5_multiple_assignment() -> None:
    """Show tuple unpacking and swap semantics."""
    first, second = compute_pair()
    # Tuple unpacking makes multi-value assignment a core language feature.
    first, second = second, first
    print("5. multiple assignment:", first, second)


def example_6_bitwise_operations() -> None:
    """Show bitwise expression support."""
    left_shift = 3 << 2
    mask = 14 & 7
    # Python integers support bitwise operators directly on arbitrary precision ints.
    print("6. bitwise operations:", left_shift, mask, 5 ^ 3)


def example_7_string_interpolation() -> None:
    """Show Python f-string interpolation."""
    language = "Python"
    examples = 7
    # F-strings embed expressions inline with readable formatting syntax.
    message = f"7. string interpolation: {language} shows {examples} examples"
    print(message)


def main() -> None:
    """Run all expression examples."""
    example_1_arithmetic_precedence()
    example_2_boolean_short_circuit()
    example_3_ternary_expression()
    example_4_augmented_assignment()
    example_5_multiple_assignment()
    example_6_bitwise_operations()
    example_7_string_interpolation()


if __name__ == "__main__":
    main()
