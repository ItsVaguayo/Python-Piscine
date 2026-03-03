from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        filtered_data = [data for data in data_batch
                         if criteria.lower() in str(data).lower()]
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.__class__.__name__,
            "status": "active"
        }


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        details = ", ".join([str(d) for d in data_batch])
        temps = [float(d.split(':')[1])
                 for d in data_batch if 'temp' in str(d)]
        avg_temp = sum(temps) / len(temps) if temps else 0
        return (f"Processing sensor batch: [{details}]\n"
                f"Sensor analysis: {len(data_batch)} readings processed,"
                f"avg temp: {avg_temp}°C")

    def filter_data(self, data_batch: List[Any]) -> List[Any]:
        result = []
        criteria = ["temp", "humidity", "pressure"]
        for find in criteria:
            result += super().filter_data(data_batch, find)
        return result


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        details: str = ", ".join([str(d) for d in data_batch])
        units: List[float] = [-float(d.split(':')[1])
                              if 'sell' in str(d) else float(d.split(':')[1])
                              for d in data_batch]
        return (f"Processing transaction batch: [{details}]\n"
                f"Transaction analysis: {len(data_batch)} operations,"
                f"net flow: {sum(units):+} units")

    def filter_data(self, data_batch: List[Any]) -> List[Any]:
        result = []
        criteria = ["buy", "sell"]
        for find in criteria:
            result += super().filter_data(data_batch, find)
        return result


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        details: list = ", ".join([str(d) for d in data_batch])
        error_count: int = sum(1 for d in data_batch
                               if 'error' in str(d).lower())
        return (f"Processing event batch: [{details}]\n"
                f"Event analysis: {len(data_batch)} events,"
                f"{error_count} error detected")

    def filter_data(self, data_batch: List[Any]) -> List[Any]:
        result = []
        criteria = ["login", "error", "logout"]
        for find in criteria:
            result += super().filter_data(data_batch, find)
        return result


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_streams(self, streams: List[DataStream],
                        data_batch: List[Any]) -> None:
        for stream in streams:
            try:
                result = stream.process_batch(stream.filter_data(data_batch))
                print(result)
            except Exception as e:
                print(f"Error processing stream {stream.stream_id}: {e}")

def data_stream() -> None:
    """Entry point for data_stream module."""
    pass


if __name__ == "__main__":
    data_stream()


