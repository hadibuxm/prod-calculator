#!/usr/bin/env python3
"""Text-based arithmetic calculator that supports the four basic operations."""

from __future__ import annotations

from typing import Callable, Dict


Operation = Callable[[float, float], float]


OPERATIONS: Dict[str, Operation] = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def read_number(prompt: str) -> float:
    """Prompt the user until they supply a valid number."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return float(raw_value)
        except ValueError:
            print("Please enter a valid number (e.g., 3, -2, 4.5).")


def read_operation() -> str:
    """Prompt the user to select a valid operation symbol."""
    prompt = "Choose operation (+ for add, - for subtract, * for multiply, / for divide): "
    while True:
        symbol = input(prompt).strip()
        if symbol in OPERATIONS:
            return symbol
        print("Unknown operation. Please enter one of: +, -, *, /.")


def run_calculator() -> None:
    print("Simple Arithmetic Calculator")
    print("----------------------------")

    while True:
        first = read_number("Enter the first number: ")
        second = read_number("Enter the second number: ")
        operation = read_operation()

        try:
            result = OPERATIONS[operation](first, second)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {result}")

        again = input("Perform another calculation? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Calculator session ended.")
            break
        print()  # Blank line separates calculations and clears previous result context.


if __name__ == "__main__":
    run_calculator()
