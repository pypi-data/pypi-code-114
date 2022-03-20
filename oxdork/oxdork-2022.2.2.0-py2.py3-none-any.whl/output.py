def write(args,results,counter):
	with open(args.output, "a") as file:
		file.write(f"[{counter}] {results}\n")
		file.close()