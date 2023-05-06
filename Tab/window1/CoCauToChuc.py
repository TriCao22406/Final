import tkinter as tk
import csv

class CoCau(tk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.canvas = CanvasLine(self)
        self.canvas.pack(fill="both", expand=1)

        #Top server
        fr1 = tk.Frame(self.canvas)
        fr1.pack(side=tk.TOP,pady=20, padx=10)

        #top 2
        fr2 = tk.Frame(self.canvas)
        fr2.pack(side=tk.TOP,pady=20, padx=10)

        #top 3
        fr3 = tk.Frame(self.canvas)
        fr3.pack(side=tk.TOP, pady=20, padx=10)

        # Create node widgets
        level1 = node(fr1, 1)
        level2 = node(fr2, 2)
        level3 = node(fr3, 3)

    def draw_line_cond(self):
        self.canvas.draw_line()
        # canvas.bind("<Button-1>", canvas.print_coords)

#tạo nhiều nút hiển thị tên và chức vụ của các NV 1 cấp
class node:
    def __init__(self, master, cap):
        self.cap = cap
        self.phanloai = self.phanloai_cap()
        self.data = self.get_data()

        for i in range(len(self.data)):
            tk.Button(master, text=self.name_job(i)).grid(row=0, column=i,padx=10)

    def name_job(self, i):
        return f"{self.data[i][1]}\n{self.data[i][7]}"

    def get_data(self):
        with open(r"..\Final\database\employees.csv", newline="", mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=",", quoting=csv.QUOTE_NONE)
            data = list(reader)
            filtered_data = []
            if self.cap == 3:
                for row in data:
                    if row[7].endswith('Manager'):
                        filtered_data.append(row)
                return filtered_data
            elif self.cap == 2:
                for row in data:
                    if row[7].startswith('giám đốc'):
                        filtered_data.append(row)
                return filtered_data
            else:
                for row in data:
                    if row[7] == "CEO":
                        filtered_data.append(row)
                        return filtered_data

    def phanloai_cap(self):
        if self.cap == 1:
            return "ceo"
        elif self.cap == 2:
            return "ban giám đốc"
        else:
            return "trưởng phòng"

class CanvasLine(tk.Canvas):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

    def draw_line(self):
        i = 0
        children = self.winfo_children()
        for children1 in children:
            i += 1
            indx = 0
            sub_children = children1.winfo_children()
            for child in sub_children:
                indx += 1
                x = child.winfo_rootx() + child.winfo_width() / 2
                y = child.winfo_rooty() - 5
                if i == 1:
                    self.create_line(x, y - 10, x, y + 20)
                elif i == 2:
                    self.create_line(x, y + 20, x, y - child.winfo_height() - 20)
                    if indx == 1:
                        first = x
                    else:
                        self.create_line(first, y - child.winfo_height() - 20, x, y - child.winfo_height() - 20)
                else:
                    self.create_line(x, y + 20, x, y - child.winfo_height() - 20)
                    if indx == 1:
                        first = x
                    else:
                        self.create_line(first, y - child.winfo_height() - 20, x, y - child.winfo_height() - 20)

    @staticmethod
    def print_coords(event):
        x, y = event.x, event.y
        print(f"Mouse clicked at ({x}, {y})")
