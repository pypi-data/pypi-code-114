import tkinter as tk
from suggestion import Suggestion
from cyberpunk_theme import Cyberpunk


# the dataset
DATASET = "/home/alex/words_alpha.txt"

# root
root = tk.Tk()
root.title("Suggestion demo | built with Pyrustic")

# set the theme
Cyberpunk().target(root)

# text field (it works with tk.Entry too!)
text_field = tk.Text(root)
text_field.pack()

# Suggestion
suggestion = Suggestion(text_field, dataset=DATASET)

# lift off !
root.mainloop()














exit()
import tkinter as tk
import tkutil
from suggestion import Suggestion
from jayson import Jayson
from cyberpunk_theme import Cyberpunk


def bigdata():
    dictionary = "/home/alex/Desktop/words_dictionary.json"
    jayson = Jayson(dictionary)
    return tuple(jayson.data)


DATASET = ["la", "maison", "au", "bord", "du", "lac"]
DATASET = "/home/alex/Desktop/words_alpha.txt"

root = tk.Tk()
Cyberpunk().target(root)

# text widget
text = tk.Text(root)
text.pack()
text.focus_set()
Suggestion(text, dataset=DATASET)

# entry widget
entry = tk.Entry(root, width=70)
entry.pack(fill=tk.X)
#entry.focus_set()
Suggestion(entry, dataset=DATASET)

# loop
tkutil.center_window(root)
root.mainloop()
