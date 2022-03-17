import cmd, sys
import os 
from pathlib import Path
import spleeter
from importlib.metadata import version
from importlib.resources import is_resource

__version__ = version('audiostems')

class Shell(cmd.Cmd):
    intro = 'Welcome to the command line.   Type help or ? to list commands.'
    prompt = '> '
    outputdir = str(Path('~/music/stems').expanduser().resolve())
    downloaddir = str(Path('~/music/sampledl').expanduser().resolve())
    nstems = 4
    _meta = {
        'outputdir': {'aliases': ['outdir'], 'fromstr': lambda string: str(Path(string).expanduser().resolve())},
        'downloaddir': {'aliases': ['downdir'], 'fromstr': lambda string: str(Path(string).expanduser().resolve())},
        'nstems': {'aliases': ['stems'], 'fromstr': lambda string: int(string)},
    }

    def do_info(self, arg):
        'Print some information about the program'
        if arg == 'debug':
            print(f'Version: {__version__}')
        print(f'Output Directory: {self.outputdir}')
        print(f'Output Stems: {self.nstems}')
        print(f'Download Directory: {self.downloaddir}')

    def do_set(self, arg):
        'Set variable value:    SET outdir ~/music/stems'
        args = arg.split(' ')
        if len(args) > 1:
            for k, v in self._meta.items(): 
                if args[0] in [k] + v['aliases']:
                    setattr(self, k, v['fromstr'](args[1]))
                    break
        else:
            return self.do_help('set')

    def do_separate(self, arg):
        'Separate audio into stems:   SEPARATE file.mp3 outputdirectory/'
        args = arg.strip().split(' ')
        files = []
        if args[0] == '':
            return self.do_help('separate')
        if len(args) >= 1: 
            filename = Path(args[0]).expanduser().resolve()
            # print(filename)
            if filename.is_dir(): 
                files = filename.glob('*')
            elif not filename.is_file(): 
                return print(f'Audio file {filename} does not exist')
            else:
                files = [filename]
        if len(args) >= 3:
            outputdir = Path(args[1]).expanduser().resolve()
            if outputdir.is_file():
                return print(f'At there is a file at {outputdir}, can\'t write there')
            if not outputdir.is_dir():
                if (input(f'Do you want to create the directory {outputdir}? [default=Y]') | 'Y') != 'N': return
                outputdir.mkdir()
                outputdir = outputdir.resolve()
            self.outputdir = str(outputdir)
        print(f'Using output directory: {self.outputdir}')
        print(f'Producing: {self.nstems} stems')
        for filename in files: 
            os.system(f'spleeter separate -p spleeter:{self.nstems}stems -o {self.outputdir} {str(filename)}')
    
    def do_download(self, arg):
        'Download a youtube video:    DOWNLOAD https://youtube.com/watch?v=blahblah'
        args = arg.strip().split(' ')
        if args[0] == '':
            return self.do_help('download')
        if len(args) >= 1: 
            return os.system(f'youtube-dl -x --audio-format wav --audio-quality 0 -o "{self.downloaddir}/%(title)s.%(ext)s" --restrict-filenames {args[0]}')

    # def do_ls(self, arg):
    #     'List files in directory:    LS path/to/dir'
    #     print('  '.join([x.name for x in Path(arg.strip().split(' ')[0]).expanduser().resolve().glob('*')]))

    def precmd(self, line):
        cmd = line.split(' ')
        if cmd[0] == 'd':
            cmd[0] == 'download'
        elif cmd[0] == 's':
            cmd[0] = 'separate'
        return ' '.join(cmd)

    def complete_info(self, text, line, begidx, endidx):
        return [x for x in ['debug'] if x.startswith(text) and x != text]

    def complete_set(self, text, line, begidx, endidx):
        args = line.split(' ')
        if len(args) < 3:
            _complete = []
            for k, v in self._meta.items():
                if k.startswith(text):
                    _complete.append(k)
                _complete += [x for x in v['aliases'] if x.startswith(text)]
            return _complete
        
    def complete_s(self, text, line, begidx, endidx):
        return self.complete_separate(text, line, begidx, endidx)

    def complete_separate(self, text, line, begidx, endidx): 
        return self._complete_ls(text, line, begidx, endidx)
    
    def complete_ls(self, text, line, begidx, endidx):
        return self._complete_ls(text, line, begidx, endidx)

    def _complete_ls(self, text, line, begidx, endidx):
        path = Path(line.split(' ')[-1]).expanduser().resolve()
        if path.is_file(): 
            return []
        if path.is_dir():
            return list(map(lambda x: f'{x.name}/' if x.is_dir() else x.name, path.glob('*')))
        return list(map(lambda x: f'{x.name}/' if x.is_dir() else x.name, path.parent.glob(f'{path.name}*'))) 


    def do_exit(self, arg):
        'Exit.'
        quit()

    def preloop(self):
        self.do_info('debug')



def main():
    Shell().cmdloop()


if __name__ == '__main__':
    main()