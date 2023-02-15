import tkinter as tk

class Checkbox :

    def __init__(self,root,pos_x,pos_y,color):
        self.checkbox_value = tk.IntVar()
        self.color_val = color
        self.checkbox = tk.Checkbutton(root, variable=self.checkbox_value, height=5, width=10, bg=color, highlightthickness=0)
        self.checkbox.place(x=pos_x, y=pos_y)

    def check_checkbox(self):
        if self.checkbox_value.get() == 1:
            print("La case est cochée !")
        else:
            print("La case n'est pas cochée.")