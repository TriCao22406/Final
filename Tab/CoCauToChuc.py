import GUI_Route as GUI
import tkinter as tk
import csv

class CoCau:
    def __init__(self,x,y):
        canvas = tk.Canvas(bg="red")
        canvas.pack(fill="both", expand=1)

        #Top server
        fr1 = tk.Frame(canvas)
        fr1.pack(side=tk.TOP, )

        #top 2
        fr2 = tk.Frame(canvas)
        fr2.pack(side=tk.TOP)

        #top 3
        fr3 = tk.Frame(canvas)
        fr3.pack(side=tk.TOP)

        # Create node widgets
        level1 = node(fr1, 1)
        level2 = node(fr2, 2)
        level3 = node(fr3, 3)



#tạo nhiều nút hiển thị tên và chức vụ của các NV 1 cấp
class node:
    def __init__(self, master, cap):
        self.cap = cap
        self.phanloai = self.phanloai_cap()
        self.data = self.get_data()
        print(self.data)

        for i in range(len(self.data)):
            tk.Button(master, text=self.name_job(i)).grid(row=0, column=i, padx=10,pady=10)

    def name_job(self, i):
        return f"{self.data[i][1]}\n{self.data[i][3]}"

    def get_data(self):
        with open('D:/Final/Final/database/bangiamdoc.csv', newline="", mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=",", quoting=csv.QUOTE_NONE)
            data = list(reader)
            filtered_data = []
            if self.cap == 3:
                for row in data:
                    if row[3].startswith('trưởng phòng'):
                        filtered_data.append(row)
                return filtered_data
            elif self.cap == 2:
                for row in data:
                    if row[3].startswith('giám đốc'):
                        filtered_data.append(row)
                return filtered_data
            else:
                for row in data:
                    if row[3] == "ceo":
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
    def __init__(self):
        super().__init__()

    def draw_line(self):
