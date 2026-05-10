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
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Concrete implementation for processing numeric data."""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")
        processed_value = f"Processed {len(data)} values, \
sum={sum(data)}, avg={sum(data)/len(data):.2f}"
        return str(processed_value)

    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(i, int) for i in data)


class TextProcessor(DataProcessor):
    """Concrete implementation for processing text data."""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")
        processed_value = f"Processed {len(''.join(data))} characters, \
{len(data)} words"
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
    print("Initializing Numeric Processor...")
    print("Processing data: [1, 2, 3, 4, 5]")
    data = [1, 2, 3, 4, 5]
    processor = NumericProcessor()
    try:
        result = processor.process(data)
        formatted_result = processor.format_output(result)
        print(formatted_result)
    except ValueError as e:
        print(f"Error processing numeric data: {e}")
    finally:
        print()

    print("Initializing Text Processor...")
    print('Processing data: ["Hello", "Nexus", "World"]')
    text_data = ["Hello", "Nexus", "World"]
    text_processor = TextProcessor()
    try:
        text_result = text_processor.process(text_data)
        formatted_text_result = text_processor.format_output(text_result)
        print(formatted_text_result)
    except ValueError as e:
        print(f"Error processing text data: {e}")
    finally:
        print()

    print("Initializing Log Processor...")
    print("Processing data: ['Error: File not found']")
    log_data = ["Error: File not found"]
    log_processor = LogProcessor()
    try:
        log_result = log_processor.process(log_data)
        formatted_log_result = log_processor.format_output(log_result)
        print(formatted_log_result)
    except ValueError as e:
        print(f"Error processing log data: {e}")
    finally:
        print()

    print("=== Polymorphic Processing Demo ===")
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    sample_data = [
        [10, 20, 30],
        ["polymorphism", "in", "python"],
        ["Info: System started"]
    ]
    for proc, data in zip(processors, sample_data):
        try:
            result = proc.process(data)
            formatted_result = proc.format_output(result)
            print(formatted_result)
        except ValueError as e:
            print(f"Error processing data with {proc.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()
