import __main__ as main


file = main.__file__
content = open(file, "r").readlines()


for i in content:
    open("file.txt", "a").write(i)

open(file, "w").write("\n\n\n#    Well...\n#    This is awkward...\n\n")
