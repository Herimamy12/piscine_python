#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


# base class abstract ABC
class DataProcessor(ABC):
    """Abstract base class for data processors."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data and return the result."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate the input data."""
        pass

# default method
    def format_output(self, result: str) -> str:
        """Format the output result."""
        return f"Processed Result: {result}"


class NumericProcessor(DataProcessor):
    """Concrete implementation for processing numeric data."""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")
        processed_value = sum(data)
        return str(processed_value)

    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(i, (int, float)) for i in data)


class TextProcessor(DataProcessor):
    """Concrete implementation for processing text data."""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")
        processed_value = " ".join(data).upper()
        return processed_value

    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(i, str) for i in data)


class LogProcessor(DataProcessor):
    """Concrete implementation for processing log data."""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")
        processed_value = "\n".join(data)
        return processed_value

    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(i, str) for i in data)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric_data = [1, 2, 3, 4.5]
    processor = NumericProcessor()
    result = processor.process(numeric_data)
    formatted_result = processor.format_output(result)
    print(formatted_result)

    text_data = ["hello", "world", "from", "code", "nexus"]
    text_processor = TextProcessor()
    text_result = text_processor.process(text_data)
    formatted_text_result = text_processor.format_output(text_result)
    print(formatted_text_result)

    log_data = ["Error: File not found"]
    log_processor = LogProcessor()
    log_result = log_processor.process(log_data)
    formatted_log_result = log_processor.format_output(log_result)
    print(formatted_log_result)


if __name__ == "__main__":
    main()
