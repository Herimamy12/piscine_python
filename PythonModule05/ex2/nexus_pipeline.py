#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Protocol, Union


class ProcessingPipeline(ABC):
    def add_stage(self, stage: 'ProcessingStages') -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class ProcessingStages(Protocol):
    def process(self, data: Any) -> Any:
        ...


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStages] = []

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process(data)
        return data


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStages] = []

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process(data)
        return data


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStages] = []

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process(data)
        return data


class NexusManager:
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> List[Any]:
        results = []
        for pipeline in self.pipelines:
            result = pipeline.process(data)
            results.append(result)
        return results


class InputStage:
    def process(self, data: Any) -> Dict[str, Any]:
        # Simulate data ingestion
        return {"raw_data": data}


class TransformStage:
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # Simulate data transformation
        transformed_data = {k: str(v).upper() for k, v in data.items()}
        return transformed_data


class OutputStage:
    def process(self, data: Dict[str, Any]) -> str:
        # Simulate data output
        output = ", ".join(f"{k}: {v}" for k, v in data.items())
        return output


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print()

    nexus_manager = NexusManager()
    json_pipeline = JSONAdapter("json_pipeline_01")
    csv_pipeline = CSVAdapter("csv_pipeline_01")
    stream_pipeline = StreamAdapter("stream_pipeline_01")
    nexus_manager.add_pipeline(json_pipeline)
    nexus_manager.add_pipeline(csv_pipeline)
    nexus_manager.add_pipeline(stream_pipeline)
    for pipeline in nexus_manager.pipelines:
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())
    sample_data = {"name": "Alice", "age": 30, "city": "New York"}
    results = nexus_manager.process_data(sample_data)
    for i, result in enumerate(results, start=1):
        print(f"Pipeline {i} Output: {result}")


if __name__ == "__main__":
    main()
