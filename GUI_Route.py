"""
module chính, có tác dụng điều hướng tới các cửa sổ khác nhau
"""

from tkinter import *

class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("Maxwell Co. Ltd")
        self.root.state('zoomed')

        import Login



