"""Demonstrate Python statement-level control structures."""


def approval_label(score: int) -> str:
    """Return a label using guard-clause style branching."""
    if score < 0:
        return "invalid"
    if score < 75:
        return "needs improvement"
    return "approved"


def example_1_for_loop_range() -> None:
    """Show a for-loop iterating with range()."""
    # Python's for-loop iterates over any iterable, and range() is the common counter source.
    values = [index * index for index in range(4)]
    print("1. for loop with range:", values)


def example_2_while_loop() -> None:
    """Show a while-loop with a condition."""
    count = 0
    outputs: list[int] = []
    # While loops remain available for condition-driven repetition.
    while count < 3:
        outputs.append(count)
        count += 1
    print("2. while loop:", outputs)


def example_3_if_elif_else() -> None:
    """Show chained conditional branching."""
    value = 86
    # elif keeps mutually exclusive branches readable without nested indentation.
    if value >= 90:
        result = "excellent"
    elif value >= 75:
        result = "passing"
    else:
        result = "failing"
    print("3. if/elif/else:", result)


def example_4_match_statement() -> None:
    """Show Python's structural pattern matching."""
    command = ("archive", 2026)
    # match/case expresses branch selection with destructuring-friendly syntax.
    match command:
        case ("archive", year):
            result = f"archive request for {year}"
        case ("delete", _):
            result = "delete request"
        case _:
            result = "unknown request"
    print("4. match statement:", result)


def example_5_break_continue() -> None:
    """Show break and continue in one loop."""
    visited: list[int] = []
    for number in range(6):
        # continue skips odd values; break exits once a threshold is met.
        if number % 2 == 1:
            continue
        if number == 4:
            break
        visited.append(number)
    print("5. break and continue:", visited)


def example_6_nested_loops() -> None:
    """Show nested iteration over rows and columns."""
    pairs: list[tuple[int, int]] = []
    # Nested loops are explicit and indentation reveals the control hierarchy.
    for row in range(2):
        for column in range(3):
            pairs.append((row, column))
    print("6. nested loops:", pairs)


def example_7_guard_clauses() -> None:
    """Show early returns as guard clauses."""
    print("7. guard clauses:", approval_label(-1), approval_label(80))


def main() -> None:
    """Run all control-structure examples."""
    example_1_for_loop_range()
    example_2_while_loop()
    example_3_if_elif_else()
    example_4_match_statement()
    example_5_break_continue()
    example_6_nested_loops()
    example_7_guard_clauses()


if __name__ == "__main__":
    main()
