import os


def transfo_name(theLines):
    # Fix submodules title
    hasSubmodules = False
    for i, line in enumerate(theLines):
        if line == "Submodules\n":
            theLines.remove(line)
            theLines.remove(theLines[i])
            hasSubmodules = True
            break

    # Fix first line
    splitted = theLines[0].rstrip().replace('`', '').split(sep=".")
    newstr = '``' + splitted[-1] + '``'
    if hasSubmodules:
        newstr = newstr.replace('``', '**')
    theLines[0] = newstr + '\n'

    for k, line in enumerate(theLines):
        theLines[k] = line.replace(":maxdepth: 3", ":maxdepth: 8")
    return theLines


folder_to_change = "source/API/"

for root, dirs, files in os.walk(folder_to_change):

    for file in files:
        if file.endswith(".rst"):
            filename = root + "/" + file
            with open(filename, "r") as f:
                lines = f.readlines()
                newlines = transfo_name(lines)
            with open(filename, "w") as f:
                f.writelines(newlines)
