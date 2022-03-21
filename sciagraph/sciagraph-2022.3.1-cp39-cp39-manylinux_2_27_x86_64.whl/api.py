"""Public API for interacting with Sciagraph."""

from datetime import datetime, timezone
from typing import Optional
import logging
from dataclasses import dataclass, asdict

__all__ = ["ReportResult"]

_LOGGER = logging.getLogger("sciagraph")

_DOWNLOAD_INSTRUCTIONS = """\
Successfully uploaded the Sciagraph profiling report.

Job start time: {job_time}
Job ID: {job_id}

To see the resulting profiling report, run the following on
Linux/Windows/macOS, Python 3.7+.

If you're inside a virtualenv:

    pip install --upgrade sciagraph-report

Otherwise:

    pip install --user --upgrade sciagraph-report

Then:

    python -m sciagraph_report download {download_key} {decryption_key}

If you have trouble installing sciagraph-report, please read the documentation:

https://pythonspeed.com/sciagraph/docs/howto/report-viewer.html
"""


@dataclass
class ReportResult:
    """
    Information about how to download uploaded profiling report.

    This will get logged by Sciagraph when profiling is finished.
    """

    job_time: str
    job_id: str
    download_key: str
    decryption_key: str

    def __str__(self):
        return _DOWNLOAD_INSTRUCTIONS.format(**asdict(self))


_UNKNOWN_JOB_ID = "Unknown, see docs to learn how to set this"


def _log_result(
    job_secs_since_epoch: int,
    job_id: Optional[str],
    download_key: str,
    decryption_key: str,
):
    """Log a ``ReportResult``."""
    if job_id is None:
        job_id = _UNKNOWN_JOB_ID
    job_time = datetime.fromtimestamp(job_secs_since_epoch, timezone.utc).isoformat()
    report = ReportResult(
        job_time=job_time,
        job_id=job_id,
        download_key=download_key,
        decryption_key=decryption_key,
    )
    _LOGGER.warning(report)
