import json
from typing import Optional
from dataclasses import dataclass, field
import traceback

from igi_file_transformation_contract.exceptions import IGIAggregateException, IGIUserFriendlyException

IGI_SUPPORT_EMAIL = "support@igiltd.com"
FAO = "Chris Prosser"
PLEASE_SUBMIT_MSG = (
    f"Please consider submitting the file to IGI to request for "
    f"support to be added ({IGI_SUPPORT_EMAIL} - FAO: {FAO}).")


@dataclass
class Status:
    success: bool
    igi_exception: Optional[Exception] = field(default_factory=lambda: None)

    @property
    def failure_message(self) -> str:
        """User friendly message."""
        if self.igi_exception is None:
            return ""

        if isinstance(self.igi_exception, IGIUserFriendlyException):
            return str(self.igi_exception)
        return f"Unexpected error - {PLEASE_SUBMIT_MSG}"

    @property
    def stack_trace(self) -> str:        
        return traceback.format_exception(
            type(self.igi_exception),
            self.igi_exception,
            self.igi_exception.__traceback__,
        )
    
    def to_json(self) -> str:
        serialise = lambda o: o.__dict__ if hasattr(o, '__dict__') else str(o)
        return json.dumps(self, default=serialise, sort_keys=True, indent=4)


SuccessStatus = Status(success=True)


@dataclass
class TransformationResult:
    status: Status
    output_filepath: str = field(default="")

    @property
    def message(self) -> str:
        if self.status.success:
            return "Success"
        return self.status.failure_message


def create_aggregate_result(comb_path: str, *results: TransformationResult) -> TransformationResult:
    # note: wanted to set this to success if all (rather than any) passed,
    #       however, this does not work as it gets the failed status and 
    #       returns an erorr mesage rather than the file - we are contrained to
    #       either a file response (for the zip) - `send_file()` or a template
    #       response `render_transformer_template()`, but don't seem to be able to
    #       do both. This means that I can't return the zip and an error msg (
    #       which requires a re-render of the template with updated params).
    success = any(r.status.success for r in results)
    msgs = set([r.message for r in results if not r.status.success])
    
    # TODO: it would be better if we could map the error message to the files it
    #       relates to. Tried with result.output_filepath, but it's empty in errors.
    #       Could also consider cutting out repeat suffixes e.g. consider sumitting...
    if not msgs:
        return TransformationResult(status=Status(success), output_filepath=comb_path)
    msg = f"{len(msgs)} out of {len(results)} files failed: {', '.join(msgs)}"
    status = Status(success, igi_exception=IGIAggregateException(msg))
    return TransformationResult(status=status, output_filepath=comb_path)
    


