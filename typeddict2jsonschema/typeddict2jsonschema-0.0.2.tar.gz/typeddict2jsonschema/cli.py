import sys
import argparse
import json
from typing import Dict, Any
from .jsonschemagenerator import analyze
from .utils import configure_logging




def main(raw_args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--input-type", dest="input_type", default="file", choices=["file", "string"], help="Input Type")
    parser.add_argument("--log-level", dest="log_level", default="info", choices=["debug", "info", "warning", "error"], help="Log Level")
    parser.add_argument("--log-file", dest="log_file", default="stdout", help="Log files, stdout and stderr are special values")
    parser.add_argument("--output", dest="output_class", default="__all__", help="Which class to output")
    parser.add_argument("input")
    args = parser.parse_args(raw_args)

    configure_logging("typeddict2jsonschema", args.log_file, args.log_level)
    program = args.input
    if args.input_type == "file":
        with open(args.input, 'r') as fd:
            program = fd.read() 
    json_schema_dict: Dict[str, Any] = analyze(program)
    if args.output_class == "__all__":
        output = json_schema_dict
    else:
        output = json_schema_dict[args.output_class]
    print(json.dumps(output))