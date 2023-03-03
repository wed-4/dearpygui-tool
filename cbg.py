import configparser
import json
import tkinter as tk
from tkinter import ttk
from tkcode import CodeEditor


def codeeditoropen():
    root = tk.Tk()
    root.title("json editor")
    root.option_add("*tearOff", 0)

    menubar = tk.Menu(root)

    file_menu = tk.Menu(menubar)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save as")
    file_menu.add_separator()
    file_menu.add_command(label="Exit")

    help_menu = tk.Menu(menubar)
    help_menu.add_command(label="Help")
    help_menu.add_command(label="About")

    menubar.add_cascade(menu=file_menu, label="File")
    menubar.add_cascade(menu=help_menu, label="Help")

    root.config(menu=menubar)

    notebook = ttk.Notebook(root)
    tab_1 = ttk.Frame(notebook)
    notebook.add(tab_1, text="a.json")
    notebook.pack(fill="both", expand=True)

    code_editor = CodeEditor(
        tab_1,
        width=40,
        height=10,
        language="json",
        highlighter="dracula",
        autofocus=True,
        blockcursor=True,
        insertofftime=0,
        padx=10,
        pady=10,
    )

    code_editor.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()


def jsonread():
    configj = configparser.ConfigParser()
    configj.read('image.ini')
    with open(configj['JSON']['JSONPATH']) as f:
        di = json.load(f)
    return json.dumps(di)

