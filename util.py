#!/usr/bin/env python3
"""Various Utility functions for the PH306 assignment template.
"""

# --- Functions --- #
def assert_expr(expr: bool, msg: str) -> None:
    """Assert that an expression is True, otherwise raise an AssertionError with a message.

    Args:
        expr (bool): The expression to evaluate.
        msg (str): The message to display if the assertion fails.

    Raises:
        AssertionError: If the expression is False.
    """
    if __debug__ and not expr:
        raise AssertionError(msg)
