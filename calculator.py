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
