# Copyright 2022 NEC Laboratories Europe
# Author: Nicolas Weber <nicolas.weber@neclab.eu>

__all__ = ['run']

import argparse
import illyrian

def run():
	parser = argparse.ArgumentParser(description="Illyrian")
	parser.add_argument("args", nargs='*')
	parser.add_argument("--version", action='store_true')
	args, unknown = parser.parse_known_args()

	print("#### Illyrian v{} ####".format(illyrian.__version__))
	print()

	if args.version:
		exit(0)
	
	if args.args is None or len(args.args) == 0:
		raise Exception('usage: illyrian config.json or illyrian cmake ...')

	if len(args.args) == 1:	illyrian.wheel	(args.args[0])
	else:					illyrian.env	(args.args)