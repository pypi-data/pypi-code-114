import tkinter as tk
from megawidget.scrollbox import Scrollbox
from megawidget.tree import Tree, ExampleHook
from megawidget.table import Table
from cyberpunk_theme.widget import button as button_style
from cyberpunk_theme import Cyberpunk
from tkutil import center_window
import suggestion


def _populate_example(tree):
    #
    hub_id = tree.insert(title="ecosystem")
    tree.expand(hub_id)
    africa_id = tree.insert(title="Pyrustic", parent=hub_id)
    america_id = tree.insert(title="Dresscode", parent=hub_id)
    america_id = tree.insert(title="Hubstore", parent=hub_id)
    asia_id = tree.insert(title="Suggestion", parent=hub_id)
    europe_id = tree.insert(title="Shared", parent=hub_id)
    europe_id = tree.insert(title="Probed", parent=hub_id)
    europe_id = tree.insert(title="...", parent=hub_id)
    #


def get_frame_1(master):
    frame = tk.Frame(master)
    # tree
    tree = Tree(frame)
    tree.pack(side=tk.LEFT, anchor="nw")
    tree.hook = lambda: ExampleHook()
    _populate_example(tree)
    # Text
    text = tk.Text(frame, width=57, height=14)
    text.pack(side=tk.LEFT, anchor="n", padx=10)
    text.insert("1.0", "Join the Pyrustic Open Ecosystem !\n")
    text.insert("2.0", "https://pyrustic.github.io")
    suggestion.Suggestion(text, dataset="/home/alex/words_alpha.txt")
    # column of check button
    intvar = tk.IntVar()
    cbnames = ("Python", "Desktop", "Frontend", "Backend", "Distribution",
               "Megawidgets", "Multithreading", "Theme|Style",
               "Autocomplete", "Productivity", "Bullshit", "More...")
    cbframe = tk.Frame(frame)
    cbframe.pack(side=tk.RIGHT, anchor="n")
    for name in cbnames:
        tk.Checkbutton(cbframe, text=name).pack(anchor="nw")
    return frame


def get_frame_2(master):
    frame = tk.Frame(master)
    left_frame = tk.Frame(frame)
    left_frame.pack(side=tk.LEFT, anchor="s")
    # table
    data = [["Everest", "8,848", "Earth"],
            ["Skil Brum", "7,410", "Mars"],
            ["Abi Gamin", "7,355", "Venus"],
            ["Mana Peak", "7,272", "Krypton"],
            ["Karjiang", "7,221", "Tao-Hung"]]
    table = Table(left_frame,
                  titles=["Mountain", "Height", "Planet"], data=data,
                  orient=None,
                  cnfs={"body": {"name": "kaka"},
                        "listboxes_columns":
                            {"width": 13,
                             "height": 5}})
    table.pack()
    rb_frame = tk.Frame(left_frame)
    rb_frame.pack()
    val_items = ["red", "green", "blue"]
    for i in range(3):
        b = tk.Radiobutton(rb_frame, variable=strvar, text=val_items[i], value=i)
        b.pack(side=tk.LEFT)
    # image
    #with open("/home/alex/theme_scorpio.png", "r")
    tk.Label(frame, image=img, width=212, height=124).pack(side=tk.LEFT)
    # form
    form_frame = tk.Frame(frame)
    form_frame.pack(side=tk.RIGHT, anchor="n")
    form_frame.columnconfigure(0, pad=5)
    form_frame.columnconfigure(1, pad=5)
    #form_frame.rowconfigure(1, pad=10)
    #form_frame.rowconfigure(3, pad=10)
    label_1 = tk.Label(form_frame, text="Username")
    label_1.grid(column=0, row=0, sticky="nw")
    label_2 = tk.Label(form_frame, text="Password")
    label_2.grid(column=1, row=0, sticky="nw")
    label_3 = tk.Label(form_frame, text="Duration")
    label_3.grid(column=0, row=2, sticky="nw")
    label_4 = tk.Label(form_frame, text="")
    label_4.grid(column=1, row=2, sticky="nw")
    entry_1 = tk.Entry(form_frame, width=15)
    entry_1.grid(column=0, row=1, pady=(0, 10), sticky="w")
    entry_2 = tk.Entry(form_frame, show="*", width=15)
    entry_2.grid(column=1, row=1, pady=(0, 10), sticky="w")
    entry_3 = tk.Spinbox(form_frame, width=13)
    entry_3.grid(column=0, row=3, sticky="w")
    entry_4 = tk.Checkbutton(form_frame, text="HODL")
    entry_4.grid(column=1, row=3, sticky="w")
    entry_3.insert(0, "3.141592653")
    # bframe
    bframe = tk.Frame(form_frame)
    bframe.grid(column=0, row=4, columnspan=2,
                sticky="w", pady=(10, 0))
    bcancel = tk.Button(bframe, text="Cancel")
    bcancel.pack(side=tk.LEFT, padx=(0, 5))
    button_style.get_button_red_style().target(bcancel)
    bsubmit = tk.Button(bframe, text="Connect")
    bsubmit.pack(side=tk.LEFT)
    button_style.get_button_green_filled_style().target(bsubmit)
    return frame


def get_frame_3(master):
    frame = tk.Frame(master)
    var = tk.DoubleVar()
    scale = tk.Scale(scrollbox.box, variable=var, orient=tk.HORIZONTAL)
    scale.pack(anchor=tk.CENTER, fill=tk.X, padx=10, pady=(0, 3))
    # footer
    footer = tk.Frame(frame)
    styles = (button_style.get_button_dark_style(),
              button_style.get_button_dark_filled_style(),
              button_style.get_button_blue_style(),
              button_style.get_button_blue_filled_style(),
              button_style.get_button_green_style(),
              button_style.get_button_green_filled_style(),
              button_style.get_button_yellow_style(),
              button_style.get_button_yellow_filled_style(),
              button_style.get_button_red_style(),
              button_style.get_button_red_filled_style())
    for xxx in styles:
        b1 = tk.Button(frame, text="Submit")
        b1.pack(side=tk.LEFT, padx=(0, 5), pady=13)
        xxx.target(b1)
    return frame


root = tk.Tk()
cyberpunk_theme = Cyberpunk()
cyberpunk_theme.target(root)
root.geometry("956x537")
root.config(bg="#121519")
root.title("Pyrustic Cyberpunk Theme")
center_window(root)
img = tk.PhotoImage(file="/home/alex/theme_scorpio.png")

# menu bar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")
menubar.add_cascade(label="Desktop", menu=filemenu, command=lambda: print("hii"))
menubar.add_cascade(label="Application", command=lambda: print("hii"))
menubar.add_cascade(label="About", command=lambda: print("hii"))
root.config(menu=menubar)

strvar = tk.StringVar(value=1)

# scrollbox
scrollbox = Scrollbox(root)
scrollbox.pack(expand=1, fill=tk.BOTH)

# frame 1
frame_1 = get_frame_1(scrollbox.box)
frame_1.pack(fill=tk.X, padx=5, pady=5)

# frame 2
frame_2 = get_frame_2(scrollbox.box)
frame_2.pack(fill=tk.X, padx=5, pady=(10, 5))

# frame 2
frame_3 = get_frame_3(scrollbox.box)
frame_3.pack(fill=tk.X, padx=5, pady=(0, 400))



root.mainloop()

