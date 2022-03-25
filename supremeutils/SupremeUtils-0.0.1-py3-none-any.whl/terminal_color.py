from rich import print


class Color():
    """
    Functions:
        error(msg, color=red)
            print a formatted message
    """

    def __init__(self, text_color='white'):
        self.text_color = text_color

    def error(self, msg, color='red'):
        print(f'[[{color}]X[/{color}]] [{self.text_color}]{msg}[/{self.text_color}]')

    def warning(self, msg, color='yellow'):
        print(f'[[{color}]![/{color}]] [{self.text_color}]{msg}[/{self.text_color}]')

    def add(self, msg, color='green'):
        print(f'[[{color}]+[/{color}]] [{self.text_color}]{msg}[/{self.text_color}]')

    def minus(self, msg, color='red'):
        print(f'[[{color}]-[/{color}]] [{self.text_color}]{msg}[/{self.text_color}]')

    def info(self, msg, color='white'):
        print(f'[[{color}]i[/{color}]] [{self.text_color}]{msg}[/{self.text_color}]')
