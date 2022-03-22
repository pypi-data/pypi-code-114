from rich.console import Console
import subprocess as sp
import time
import click


class App:
    def __init__(self,filepath : str,arguments : str,delay : int):
        self.filepath = filepath
        self.arguments = arguments
        self.delay = delay
        Console().rule('[#51D6FF]<FILEWATCH IS STARTING>[/#51D6FF]')
        label_msg = "[#97DBAE][FILEWATCH][/#97DBAE]"
        Console().log(f'{label_msg} [#39AEA9]Watching [#4C3F91]{self.filepath}[/#4C3F91][/#39AEA9]')
        while True:
            with open(self.filepath) as f:
                content = f.read()
                if content != f.read():
                    Console().log(f"[#C65D7B] {label_msg} Change Detected! Running Arguments[/#C65D7B]")
                    Console().log(f'{label_msg} [#39AEA9]Watching For File Changes..[/#39AEA9]')
                    time.sleep(self.delay)
                try:
                    sp.call(self.arguments,shell=True)

                except KeyboardInterrupt:
                    Console().rule('[#EE4266]<FILEWATCH IS STOPPING>[/#EE4266]',style="red")
                    exit()

@click.command()
@click.option('--path','-p',help='Path of file to watch')
@click.option('--arguments','-args',help='Arguments to run when file changes')
@click.option('--delay','-d',default=4,help='Delay in seconds')
def start(path,arguments,delay):
    '''FILEWATCH is a file watcher that allows you to watch files if something changes run arguments'''
    App(filepath=str(path),arguments=arguments,delay=delay)

if __name__ == '__main__':
    try:
        start()

    except FileNotFoundError:
        print("Use --help to see help information")