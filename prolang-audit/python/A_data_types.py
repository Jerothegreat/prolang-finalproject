"""Demonstrate Python data-type design decisions with seven examples."""


def example_1_primitive_types() -> None:
    """Show Python primitive scalar values."""
    integer_value = 42
    float_value = 3.14
    bool_value = True
    string_value = "Python"
    # Python binds names directly to runtime objects without declarations.
    print("1. primitive types:", integer_value, float_value, bool_value, string_value)


def example_2_reference_types() -> None:
    """Show Python reference semantics using a shared list."""
    original = ["audit", "report"]
    alias = original
    # Both names point at the same list object, similar to shared references.
    alias.append("complete")
    print("2. reference type aliasing:", original, "same object:", original is alias)


def example_3_dynamic_typing() -> None:
    """Show that one name can be rebound to values of different types."""
    flexible = 99
    # Python checks type compatibility at runtime instead of compile time.
    print("3. dynamic typing before:", flexible, type(flexible).__name__)
    flexible = "ninety-nine"
    print("3. dynamic typing after:", flexible, type(flexible).__name__)


def example_4_type_introspection() -> None:
    """Use type() to inspect the inferred runtime type of values."""
    inferred_count = 5
    inferred_label = "governance"
    # Python does not expose declaration-time inference; type() inspects objects.
    print("4. type introspection:", type(inferred_count), type(inferred_label))


def example_5_collections() -> None:
    """Show built-in list and dict collection types."""
    stages = ["plan", "implement", "verify"]
    scores = {"python": 9, "go": 8}
    # Python ships flexible, heterogeneous collections in the core language.
    print("5. collections:", stages, scores)


def example_6_null_handling() -> None:
    """Show Python's null sentinel, None."""
    reviewer_name = None
    # None is a first-class singleton used to express the absence of a value.
    fallback = "unassigned" if reviewer_name is None else reviewer_name
    print("6. null handling:", reviewer_name, "=>", fallback)


def example_7_explicit_conversion() -> None:
    """Show explicit casting between common scalar types."""
    text_number = "123"
    # Python requires explicit conversion when semantics are not lossless.
    as_int = int(text_number)
    as_float = float(as_int)
    as_string = str(as_float)
    print("7. explicit conversion:", as_int, as_float, as_string)


def main() -> None:
    """Run all data-type examples."""
    example_1_primitive_types()
    example_2_reference_types()
    example_3_dynamic_typing()
    example_4_type_introspection()
    example_5_collections()
    example_6_null_handling()
    example_7_explicit_conversion()


if __name__ == "__main__":
    main()
