from typing import Any, List, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: Any) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> Optional[List[int]]:
        if data is None:
            return None
        try:
            data_processed = [int(num) for num in data]
        except ValueError:
            return None
        return data_processed    

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        if not isinstance(data, list):
            return False
        for num in data:
            if type(num) is not int:
                return False
        return True

    def format_output(self, result: List[int]) -> str:
        return (f"Output: Processed {len(result)},"
                f"sum={sum(result)}, avg={sum(result) / len(result)}")


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> Optional[str]:
        if data is None:
            return None
        if isinstance(data, list):
            data = " ".join(data)
        return data

    def validate(self, data: Any) -> bool:
        if data is None or not isinstance(data, str):
            return False
        return True

    def format_output(self, result: str) -> str:
        char_count = len(result)
        word_count = len(result.split())
        return (f"Output: Processed text: {char_count} characters, "
                f"{word_count} words")


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> Optional[str]:
        if data is None:
            return None
        return data

    def validate(self, data: Any) -> bool:
        if data is None or not isinstance(data, str):
            return False
        return True

    def format_output(self, result: str) -> str:
        if ": " in result:
            level, message = result.split(": ", 1)
            return f"Output: [ALERT] {level} level detected: {message}"
        return f"Output: {result}"


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    numeric_proc: NumericProcessor = NumericProcessor()
    data: list[int] = numeric_proc.process([1, 2, 3, 4, 5])
    print("Processing data:", data)
    if numeric_proc.validate(data):
        print("Validation: Numeric data verified")
        print(numeric_proc.format_output(data))

    print("\nInitializing Text Processor...")
    text_proc: TextProcessor = TextProcessor()
    data: str = text_proc.process(["Hello", "Nexus", "World"])
    print(f'Processing data: "{data}"')
    if text_proc.validate(data):
        print("Validation: Text data verified")
        print(text_proc.format_output(data))

    print("\nInitializing Log Processor...")
    log_proc: LogProcessor = LogProcessor()
    data: str = log_proc.process("ERROR: Connection timeout")
    print(f'Processing data: "{data}"')
    if log_proc.validate(data):
        print("Validation: Log entry verified")
        print(log_proc.format_output(data))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface..")
    data1 = numeric_proc.process([1, 2, 3])
    if numeric_proc.validate(data1):
        print("Result 1:", numeric_proc.format_output(data1))
    data2 = text_proc.process("Hello world")
    if text_proc.validate(data2):
        print("Result 2:", text_proc.format_output(data2))
    data3 = log_proc.process("Info: System ready")
    if log_proc.validate(data3):
        print("Result 3:", log_proc.format_output(data3))


if __name__ == "__main__":
    stream_processor()
