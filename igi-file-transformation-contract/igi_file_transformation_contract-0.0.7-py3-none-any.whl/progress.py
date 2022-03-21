from dataclasses import dataclass, field


@dataclass
class ProgressRecord:
    started: bool = field(default=False)
    finished: bool = field(default=False)
    success_text: str = field(default="")
    warning_text: str = field(default="")
    failure_text: str = field(default="")

    @property
    def status(self) -> str:
        return "finished" if self.finished else "started" if self.started else "ready"