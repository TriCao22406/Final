from tkinter import *
# from GUI_Route import *
#
# class CoCau():
#     def __init__(self):
#         mainframe = MainFrame()

import tkinter as tk
from tkinter import ttk


class TreeGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Tree View Example")

        self.tree = ttk.Treeview(self.win)
        self.tree.pack(side='left', fill='both', expand=True)

        # Inserting parent items
        parent1 = self.tree.insert("", "end", text="Parent 1")
        parent2 = self.tree.insert("", "end", text="Parent 2")

        # Inserting child items
        child1 = self.tree.insert(parent1, "end", text="Child 1")
        child2 = self.tree.insert(parent1, "end", text="Child 2")
        child3 = self.tree.insert(parent2, "end", text="Child 3")
        child4 = self.tree.insert(parent2, "end", text="Child 4")

        # Binding click event to the tree view
        self.tree.bind("<ButtonRelease-1>", self.tree_click)

    def tree_click(self, event):
        # Getting selected item
        item = self.tree.focus()
        print(self.tree.item(item)["text"])


tree_gui = TreeGUI()
tree_gui.win.mainloop()




