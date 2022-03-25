import argparse
from io import StringIO
import os
import sys
import ntpath
import importlib
from traceback import format_exc
from .IExecuteScripts import IExecuteScripts

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
        
def TryAddImportPath(path):
    if path not in sys.path:
        sys.path.append(path)
    return
    
def main():
    # Initialize command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inputfile", help = "Path for the input file.", required=True)
    parser.add_argument("-o", "--outputfile", help = "Path for output file", required=True)
    parser.add_argument("-m", "--modulepath", help="The file name for the module that contains the script executor.", required=True)
 
    # Read arguments from command line
    args = parser.parse_args()
    
    # print("input file = {input}".format(input=args.inputfile))
    # print("output file = {output}".format(output=args.outputfile))
    # print("module file = {module}".format(module=args.modulepath))

    # add the module to the import path.
    TryAddImportPath(os.path.dirname(os.path.realpath(args.modulepath)))
    
    fileName = ntpath.basename(args.modulepath)
    # print(fileName)
    moduleName = os.path.splitext(fileName)[0]
    # print(moduleName)
    importlib.invalidate_caches()
    module=importlib.import_module(moduleName, package=None)
    # print(module)
    
    # check for MODULE level executors.
    # this gets around issues on having static/global variables - when you import
    # the users module, you just won't find what you're looking for. 
    if not hasattr(module, '_EXECUTOR'):
        raise Exception("No script executor registered in module. Decorate your implementation of IExecuteScripts with @Register()")
    
    executor=getattr(module, module._EXECUTOR['class'])
    instance:IExecuteScripts = executor()

    # could provide some introspect mechanism that provided some metadata about
    # the actual script itself, including if it required a connection or not.
    print("Attempting to run script.\n\tExecutor: '{exe}'\n\tExpected Content Type: {produces}\n\tRequires Connection: {requiresConnection}".format(exe=module._EXECUTOR['class'],produces=module._EXECUTOR['content-type'],requiresConnection=module._EXECUTOR['requiresConnection']))
    outputSize=0
    with Capturing() as lines:
        with open(args.inputfile, 'rb') as input:
            with open(args.outputfile, 'wb') as output:
                instance.execute(context={}, inputStream=input, outputStream=output)
                outputSize=output.tell()

    print("Wrote '{length}' bytes to {file}".format(length=outputSize, file=args.outputfile))
    print("Script stdout:")
    for x in range(len(lines)):
        print("***{line}".format(line=lines[x]))
    


if __name__ == '__main__':
    main()

    
    