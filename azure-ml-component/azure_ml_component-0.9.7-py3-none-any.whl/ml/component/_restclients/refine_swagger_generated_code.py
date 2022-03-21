#!/usr/bin/env python

from pathlib import Path
import fileinput
import sys


if __name__ == "__main__":
    cur_file_path = Path(__file__).absolute()
    parent_cur_dir = Path(cur_file_path).parent
    target_dir = parent_cur_dir / "designer" / "operations"

    # stream=True
    old_str = "pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)"
    new_str = (
        "pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)"
    )
    files_stream_true = {
        "_data_sets_operations.py": [
            "template_url=self.get_dataset_visualization_data.metadata['url'],",
            "template_url=self.get_dataset_schema.metadata['url'],",
            "template_url=self.get_global_dataset_visualization_data.metadata['url'],",
            "template_url=self.get_global_dataset_schema.metadata['url'],",
            "template_url=self.get_global_dataset_visualization_data_with_name.metadata['url'],",
            "template_url=self.get_global_dataset_schema_with_name.metadata['url'],",
            "template_url=self.get_saved_dataset_schema.metadata['url'],",
            "template_url=self.get_saved_dataset_visualization_data.metadata['url'],",
        ],
        "_data_sets_v2_operations.py": [
            "template_url=self.get_dataset_visualization_data.metadata['url'],",
            "template_url=self.get_dataset_schema.metadata['url'],",
            "template_url=self.get_global_dataset_visualization_data.metadata['url'],",
            "template_url=self.get_global_dataset_schema.metadata['url'],",
            "template_url=self.get_global_dataset_visualization_data_with_name.metadata['url'],",
            "template_url=self.get_global_dataset_schema_with_name.metadata['url'],",
            "template_url=self.get_saved_dataset_schema.metadata['url'],",
            "template_url=self.get_saved_dataset_visualization_data.metadata['url'],",
        ],
        "_pipeline_drafts_operations.py": [
            "template_url=self.get_module_visualization_data.metadata['url'],",
            "template_url=self.get_module_output_schema.metadata['url'],",
            "template_url=self.get_module_visualization_data_from_data_path.metadata['url'],",
            "template_url=self.get_module_output_schema_from_data_path.metadata['url'],",
            "template_url=self.get_pipeline_draft_sdk_code.metadata['url'],",
        ],
        "_pipeline_drafts_v2_operations.py": [
            "template_url=self.get_module_visualization_data.metadata['url'],",
            "template_url=self.get_module_output_schema.metadata['url'],",
            "template_url=self.get_module_visualization_data_from_data_path.metadata['url'],",
            "template_url=self.get_module_output_schema_from_data_path.metadata['url'],",
            "template_url=self.get_pipeline_draft_sdk_code.metadata['url'],",
        ],
        "_pipeline_endpoints_operations.py": [
            "template_url=self.get_pipeline_endpoint_sdk_code.metadata['url'],"
        ],
        "_pipeline_endpoints_v2_operations.py": [
            "template_url=self.get_pipeline_endpoint_sdk_code.metadata['url'],"
        ],
        "_pipeline_runs_operations.py": [
            "template_url=self.get_preview_for_path.metadata['url'],",
            "template_url=self.get_pipeline_run_sdk_code.metadata['url'],",
        ],
        "_pipeline_runs_v2_operations.py": [
            "template_url=self.get_preview_for_path.metadata['url'],",
            "template_url=self.get_pipeline_run_sdk_code.metadata['url'],",
        ],
        "_published_pipelines_operations.py": [
            "template_url=self.get_published_pipeline_sdk_code.metadata['url'],"
        ],
        "_published_pipelines_v2_operations.py": [
            "template_url=self.get_published_pipeline_sdk_code.metadata['url'],"
        ],
    }

    flag = False
    for file_name, values in files_stream_true.items():
        path = target_dir / file_name
        for line in fileinput.input(files=path, inplace=True):
            if flag and line.strip().replace("\r\n", "") == old_str:
                sys.stdout.write(line.replace(old_str, new_str))
                flag = False
                continue
            if line.strip().replace("\r\n", "") in values:
                flag = True
            sys.stdout.write(line)
