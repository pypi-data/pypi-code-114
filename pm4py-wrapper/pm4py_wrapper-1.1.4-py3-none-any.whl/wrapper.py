from pathlib import Path

import pandas as pd
import pm4py
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.objects.log.util import interval_lifecycle
from pm4py.objects.log.exporter.xes import exporter as xes_exporter


def convert_xes_to_csv(xes_path: Path, output_path: Path):
    log = pm4py.read_xes(str(xes_path))
    log_interval = interval_lifecycle.to_interval(log)
    df = log_converter.apply(log_interval, variant=log_converter.Variants.TO_DATA_FRAME)
    df.to_csv(output_path, index=False)


def convert_csv_to_xes(csv_path: Path, output_path: Path):
    df = pd.read_csv(csv_path)
    log = log_converter.apply(df, variant=log_converter.Variants.TO_EVENT_LOG)
    log_lifecycle = interval_lifecycle.to_lifecycle(log)
    xes_exporter.apply(log_lifecycle, str(output_path))
