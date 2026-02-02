#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


# base class abstract ABC
class DataStream(ABC):
    """Abstract base class for data streams."""

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        """Filter data based on given criteria."""
        if criteria is None:
            return data_batch
        return [data for data in data_batch if criteria in str(data)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Get statistics about the data stream."""
        return {"type": self.__class__.__name__, "data_count": 0}


class SensorStream(DataStream):
    """Concrete implementation for processing sensor data."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.data_count = 0

    def process_batch(self, data_batch: List[float]) -> str:
        self.data_count += len(data_batch)
        avg_value = sum(data_batch) / len(data_batch) if data_batch else 0
        return f"SensorStream {self.stream_id}: Processed {len(data_batch)} \
values, avg={avg_value:.2f}"

    def filter_data(self, data_batch, criteria=None):
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats.update({"stream_id": self.stream_id,
                     "data_count": self.data_count})
        return stats


class TransactionStream(DataStream):
    """Concrete implementation for processing transaction data."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.data_count = 0

    def process_batch(self, data_batch: List[Dict[str, Any]]) -> str:
        self.data_count += len(data_batch)
        total_amount = sum(item.get("amount", 0) for item in data_batch)
        return f"TransactionStream {self.stream_id}: \
Processed {len(data_batch)} transactions, total_amount={total_amount:.2f}"

    def filter_data(self, data_batch, criteria=None):
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats.update({"stream_id": self.stream_id,
                     "data_count": self.data_count})
        return stats


class EventStream(DataStream):
    """Concrete implementation for processing event data."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.data_count = 0

    def process_batch(self, data_batch: List[str]) -> str:
        self.data_count += len(data_batch)
        return f"EventStream {self.stream_id}: Processed {len(data_batch)} \
events"

    def filter_data(self, data_batch, criteria=None):
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats.update({"stream_id": self.stream_id,
                     "data_count": self.data_count})
        return stats


class StreamProcessor:
    def __init__(self, stream: DataStream) -> None:
        self.stream = stream

    def process(self, data_batch: List[Any]) -> str:
        filtered_data = self.stream.filter_data(data_batch)
        return self.stream.process_batch(filtered_data)

    def get_statistics(self) -> Dict[str, Union[str, int, float]]:
        return self.stream.get_stats()


# • Demonstrate batch processing of mixed stream types
# • Include stream filtering and transformation capabilities
# • Add comprehensive error handling for stream processing failures
def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    sensor_stream = SensorStream("sensor_001")
    transaction_stream = TransactionStream("trans_001")
    event_stream = EventStream("event_001")
    streams = [
        (sensor_stream, [23.5, 26.7, 22.1, 24.3]),
        (transaction_stream, [
            {"id": 1, "amount": 100.0},
            {"id": 2, "amount": 250.5},
            {"id": 3, "amount": 75.25}
        ]),
        (event_stream, [
            "User logged in",
            "File uploaded",
            "Error occurred"
        ])
    ]
    for stream, data_batch in streams:
        processor = StreamProcessor(stream)
        try:
            result = processor.process(data_batch)
            stats = processor.get_statistics()
            print(result)
            print(f"Stream Stats: {stats}")
        except Exception as e:
            print(f"Error processing stream {stream.__class__.__name__}: {e}")
        finally:
            print()
    print("=== END OF STREAM PROCESSING ===")
    log_data = ["Error: File not found", "Warning: Low disk space",
                "Info: System rebooted"]
    event_stream = EventStream("event_002")
    processor = StreamProcessor(event_stream)
    try:
        filtered_data = event_stream.filter_data(log_data, criteria="Error")
        result = processor.process(filtered_data)
        stats = processor.get_statistics()
        print("Filtered Event Stream Processing:")
        print(result)
        print(f"Stream Stats: {stats}")
    except Exception as e:
        print(f"Error processing filtered event stream: {e}")
    finally:
        print()


if __name__ == "__main__":
    main()
