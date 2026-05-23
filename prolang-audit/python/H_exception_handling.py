"""Demonstrate Python exception and event-handling techniques."""

from __future__ import annotations

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class AuditError(Exception):
    """Represent a domain-specific audit failure."""


class MissingReviewerError(AuditError):
    """Raised when a reviewer is missing."""


class TemporaryStorageError(AuditError):
    """Raised when storage is temporarily unavailable."""


class DemoResource:
    """A simple context manager used for cleanup demonstration."""

    def __enter__(self) -> DemoResource:
        """Acquire the resource."""
        print("6. context manager: enter")
        return self

    def __exit__(self, exc_type, exc, exc_tb) -> bool:
        """Release the resource and keep propagating exceptions."""
        print("6. context manager: exit")
        return False


def parse_count(raw_value: str) -> int:
    """Parse an integer count or raise a custom error."""
    try:
        return int(raw_value)
    except ValueError as exc:
        raise MissingReviewerError("count must be numeric") from exc


def read_config() -> None:
    """Raise a storage error for chaining examples."""
    raise TemporaryStorageError("config service unavailable")


def load_audit_settings() -> None:
    """Wrap a lower-level exception with additional context."""
    try:
        read_config()
    except TemporaryStorageError as exc:
        raise AuditError("unable to load audit settings") from exc


def validate_state(should_fail: bool) -> None:
    """Raise an exception to mimic a fatal validation problem."""
    if should_fail:
        raise AuditError("fatal validation mismatch")


def low_level_operation() -> None:
    """Raise an error deep in the call stack."""
    raise AuditError("database write failed")


def mid_level_operation() -> None:
    """Propagate the low-level error upward."""
    low_level_operation()


def example_1_try_except_finally() -> None:
    """Show try/except/finally behavior."""
    try:
        value = 10 / 2
        print("1. try/except/finally:", value)
    except ZeroDivisionError:
        print("1. try/except/finally: division failed")
    finally:
        # finally always runs, which mirrors deterministic cleanup logic.
        print("1. try/except/finally: cleanup executed")


def example_2_custom_exception_type() -> None:
    """Show a custom exception type."""
    try:
        parse_count("NaN")
    except MissingReviewerError as exc:
        # Custom exception classes encode domain meaning beyond generic ValueError.
        print("2. custom exception:", exc)


def example_3_chaining_and_unwrapping() -> None:
    """Show exception chaining via raise ... from ... ."""
    try:
        load_audit_settings()
    except AuditError as exc:
        # __cause__ preserves the lower-level exception for debugging.
        print("3. chaining:", exc, "cause:", type(exc.__cause__).__name__)


def example_4_raise_and_except() -> None:
    """Show raise/except as Python's explicit error transfer."""
    try:
        validate_state(True)
    except AuditError as exc:
        # Python surfaces exceptional control flow through raised exceptions.
        print("4. raise/except:", exc)


def example_5_multiple_exception_types() -> None:
    """Handle multiple exception classes in a single block."""
    for raw_value in ("5", "oops", "7"):
        try:
            print("5. parsed value:", parse_count(raw_value))
        except (MissingReviewerError, TemporaryStorageError) as exc:
            # A tuple in except consolidates related recovery logic.
            print("5. multiple exception types:", type(exc).__name__)


def example_6_context_manager() -> None:
    """Show context manager entry and exit hooks."""
    with DemoResource():
        # with delegates setup and teardown to __enter__ and __exit__.
        print("6. context manager: inside")


def example_7_propagation_vs_logging() -> None:
    """Show propagation to a caller instead of logging in place."""
    try:
        mid_level_operation()
    except AuditError as exc:
        # The top-level caller decides whether to log, re-raise, or recover.
        logging.info("7. propagation handled at top level: %s", exc)


def main() -> None:
    """Run all exception-handling examples."""
    example_1_try_except_finally()
    example_2_custom_exception_type()
    example_3_chaining_and_unwrapping()
    example_4_raise_and_except()
    example_5_multiple_exception_types()
    example_6_context_manager()
    example_7_propagation_vs_logging()


if __name__ == "__main__":
    main()
