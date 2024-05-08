import tkinter as tk
from tkinter import messagebox

def click(event):
    current = display.get()
    text = event.widget.cget("text")
    
    try:
        if text=="=":
            result = eval(current)
            display.delete(0,tk.END)
            display.insert(tk.END,result)
        elif text=="C":
            display.delete(0,tk.END)
        else:
            display.insert(tk.END,text)
    except Exception as e:
        messagebox.showinfo("ERROR",e)
        display.delete(0,tk.END)

window = tk.Tk()
window.title("Calculator")
window.geometry("320x450")

display = tk.Entry(window,font=("Arial",25),justify="right")
display.pack(fill=tk.X,padx=10,pady=10,ipady=10)

btn_frame = tk.Frame(window)
btn_frame.pack()

btn_labels = [
    ["7","8","9","C"],
    ["4","5","6","+"],
    ["1","2","3","-"],
    ["*","0","/","."],
    ["="]
]


for i in range(0,4):
    for j in range(0,4):
        button = tk.Button(btn_frame,font=("Arial",16),padx=15,pady=10,text=btn_labels[i][j])
        button.grid(row=i,column=j, padx=10,pady=10)
        button.bind("<Button>",click)

button = tk.Button(btn_frame,font=("Arial",16),padx=100,pady=10,text=btn_labels[4][0])
button.grid(row=5,column=0, columnspan=4, rowspan = 1, padx=10,pady=10)
button.bind("<Button>",click)

window.mainloop()




























# class Calculator:
#     def __init__(self, master):
#         self.master = master
#         master.title("Calculator")

#         self.display = tk.Entry(master, width=30, borderwidth=5)
#         self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#         # Button layout
#         self.buttons = [
#             ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#             ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#             ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#             ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
#             ('C', 5, 0)
#         ]
#         # Create buttons
#         for (text, row, col) in self.buttons:
#             btn = tk.Button(master, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t))
#             btn.grid(row=row, column=col)
#     def on_button_click(self, value):
#         if value == '=':
#             try:
#                 result = eval(self.display.get())
#                 self.display.delete(0, tk.END)
#                 self.display.insert(tk.END, str(result))
#             except Exception as e:
#                 self.display.delete(0, tk.END)
#                 self.display.insert(tk.END, "Error")
#         elif value == 'C':
#             self.display.delete(0, tk.END)
#         else:
#             self.display.insert(tk.END, value)
# def main():
#     root = tk.Tk()
#     calculator = Calculator(root)
#     root.mainloop()
# if __name__ == "__main__":
#     main()

