from pydantic.dataclasses import dataclass


@dataclass
class ParallelAnsysConfig:
    run_dir: str
    n_parallel_runners: int
    n_proc: int
    root_dir: str
    exec_file: str
    master_input_file: str
    template_to_input_file: dict
    additional_upload_files: list