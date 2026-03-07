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
        filtered_data: List[Any] = [data for data in data_batch
                                    if criteria.lower() in str(data).lower()]
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.__class__.__name__,
            "status": "active"
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        details: str = ", ".join([str(d) for d in data_batch])
        temps: List[float] = [float(d.split(':')[1])
                              for d in data_batch if 'temp' in str(d)]
        avg_temp: float = sum(temps) / len(temps) if temps else 0
        return (f"Processing sensor batch: [{details}]\n"
                f"Sensor analysis: {len(data_batch)} readings processed,"
                f"avg temp: {avg_temp}°C")

    def filter_data(self, data_batch: List[Any]) -> List[Any]:
        result: List[Any] = []
        criteria: List[str] = ["temp", "humidity", "pressure"]
        for find in criteria:
            result += super().filter_data(data_batch, find)
        return result


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
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
        result: List[Any] = []
        criteria: List[str] = ["buy", "sell"]
        for find in criteria:
            result += super().filter_data(data_batch, find)
        return result


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        details: str = ", ".join([str(d) for d in data_batch])
        error_count: int = sum(1 for d in data_batch
                               if 'error' in str(d).lower())
        return (f"Processing event batch: [{details}]\n"
                f"Event analysis: {len(data_batch)} events,"
                f"{error_count} error detected")

    def filter_data(self, data_batch: List[Any]) -> List[Any]:
        result: List[Any] = []
        criteria: List[str] = ["login", "error", "logout",
                               "Critical_error", "Large_transaction"]
        for find in criteria:
            result += super().filter_data(data_batch, find)
        return result


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_streams(self, streams: List[DataStream],
                        data_batch: List[Any]) -> List[str]:
        types: Dict[str, int] = {"SensorStream": 0,
                                 "TransactionStream": 0, "EventStream": 0}
        result: List[str] = []
        for stream in streams:
            try:
                result.append(stream.process_batch(
                    stream.filter_data(data_batch)))
                types[stream.__class__.__name__] += len(
                    stream.filter_data(data_batch))
            except Exception as e:
                print(f"Error processing stream {stream.stream_id}: {e}")
        print("Batch 1 Results:")
        print(f"- Sensor data: {types['SensorStream']} readings processed")
        print(
            f"- Transaction data:"
            f"{types['TransactionStream']} operations processed")
        print(f"- Event data: {types['EventStream']} events processed")
        return result


def data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    initial_streams: List[DataStream] = [
        SensorStream("SENSOR_00"),
        TransactionStream("TRANS_001"),
        EventStream("EVENT_001")]
    for stream in initial_streams:
        if stream.get_stats()["type"] == "SensorStream":
            print("Initializing Sensor Stream...")
            print(f"Stream ID: {stream.stream_id}, Type: Environmental Data")
            print(
                stream.process_batch(
                    ["temp:22.5",
                     "humidity:65",
                     "pressure:1013"]),)
        elif stream.get_stats()["type"] == "TransactionStream":
            print("Initializing Transaction Stream...")
            print(f"Stream ID: {stream.stream_id}, Type: Financial Data")
            print(stream.process_batch(
                    ["buy:100",
                     "sell:150",
                     "buy:75"]))
        elif stream.get_stats()["type"] == "EventStream":
            print("Initializing Event Stream...")
            print(f"Stream ID: {stream.stream_id}, Type: System Events")
            print(stream.process_batch(
                    ["login",
                     "error",
                     "logout"]))
        else:
            print("Type: Unknown")
            print("This object is not valid")
        print()
    print("=== Polymorphic Stream Processing ===")
    mixed_data: List[str] = ["temp:22.5", "humidity:65", "pressure:1013",
                             "buy:100", "sell:150", "buy:75", "sell:2",
                             "login", "error", "logout",
                             "Critical_error", "Large_transaction",
                             "Critical_error"]
    streams: List[DataStream] = [SensorStream("SENSOR_00"),
                                 TransactionStream("TRANS_001"),
                                 EventStream("EVENT_001")]
    streampro: StreamProcessor = StreamProcessor()
    for stream in streams:
        streampro.add_stream(stream)
    streampro.process_streams(streams, mixed_data)
    print("\nStream filtering active: High-priority data only")
    print(f"Filtered results: "
          f"{mixed_data.count('Critical_error')} "
          f"critical sensor alerts, "
          f"{mixed_data.count('Large_transaction')} "
          f"large transaction"
          )
    print("All streams processed successfully. "
          "Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
