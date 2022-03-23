# -*- coding: utf-8 -*-
"""
Copyright 2019-2022 Olexandr Balyk
This file is part of Timeslib.
Timeslib is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Timeslib is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with Timeslib. If not, see <https://www.gnu.org/licenses/>.
"""

import pathlib
import pandas as pd

def read_data_csv(file_path, tableInfo):

    if tableInfo is None:
        print(
            "No info found on how to process: {}. It will be skipped.".format(file_path)
        )
        return None
    tableName = pathlib.Path(file_path).name.removesuffix(".csv")

    if tableName not in tableInfo.keys():
        print(
            "No info found on how to process: {}. It will be skipped.".format(tableName)
        )
        return None
    if tableInfo[tableName]["keepDimensions"] is None:
        print(
            "No info found on how to process: {}. It will be skipped.".format(tableName)
        )
        return None
    df = pd.read_csv(file_path)

    df["tableName"] = tableName

    if "Units" not in df.columns:
        if tableInfo[tableName]["defaultUnit"] is not None:
            df["Units"] = tableInfo[tableName]["defaultUnit"]
        else:
            df["Units"] = "missing"
    renameDimsMap = {
        "Scenario": "scenario",
        "Period": "year",
        "Region": "region",
        "Pv": "total",
        "Units": "label",
        tableInfo[tableName]["keepDimensions"]: "serieName",
    }

    df.rename(columns=renameDimsMap, inplace=True)

    excludeColumns = (
        "UserName",
        "ModelName",
        "Studyname",
        "Attribute",
        "Commodity",
        "Commodityset",
        "Process",
        "Processset",
        "Vintage",
        "Timeslice",
        "Userconstraint",
    )

    # Remove columns in excludeColumns
    df = df[[i for i in df.columns if i not in excludeColumns]]

    df = df.groupby([i for i in df.columns if not i == "total"]).agg(
        tableInfo[tableName]["aggregation"]
    )

    if "reverseSign" in tableInfo[tableName].keys():
        if tableInfo[tableName]["reverseSign"] is True:
            df = -df
            
    return df.reset_index()
