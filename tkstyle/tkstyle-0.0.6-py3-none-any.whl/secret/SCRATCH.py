import tkinter as tk
from cyberpunk_theme import Cyberpunk
from cyberpunk_theme.widget.button import get_button_style_4


root = tk.Tk()
# apply the Cyberpunk theme to the GUI
cyberpunk_theme = Cyberpunk()
cyberpunk_theme.target(root)

# write your awesome code here
# ...
# ...

button = tk.Button(root, text="Button")
button.pack()

# do you need to set dynamically a specific style to a button ?
# there are 10 styles for buttons ! from the black to the red style !
button_style_4 = get_button_style_4()
button_style_4.target(button)

# mainloop
root.mainloop()






exit()
import tkinter as tk
import tkstyle
from megawidget.table import Table


def get_button_style():
    style = tkstyle.Button()
    style.background = "red"
    return style


def get_listbox_style():
    style = tkstyle.Listbox()
    style.background = "green"
    return style


def get_table_style():
    style = tkstyle.Frame()
    style.highlightThickness = 7
    style.highlightBackground = "red"
    style.add(get_listbox_style())
    return style

theme = tkstyle.Theme()
theme.add(get_table_style(), pattern="*kaka")

root = tk.Tk()
theme.target(root)

button = tk.Button(root, text="Hello")
button.pack()

#button_style = get_button_style()
#button_style.target(button)

data = [["Jack", 20, "A"], ["Jolinda", 22, "B"],
        ["Marc", 25, "C"], ["Joe", 27, "D"], ["Jack", 30, "E"]]
table = Table(root, titles=["Name", "Age", "Location"], data=data,
              cnfs={"body": {"name": "kaka"}})
table.pack()

#table_style = get_table_style()
#table_style.target(table)

root.mainloop()
