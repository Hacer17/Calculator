import tkinter as tk
def on_click(btn_text):
    if btn_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "ERROR")
    elif btn_text == "C":
         entry.delete(0, tk.END)
# ana bölüm
root = tk.Tk()
root.title("Calculator")
root.config(bg="lime")
root.geometry("330x550")
entry = tk.Entry(root, width=15, font=("Arial",30))
entry.grid(row=0, column=0, columnspan=8, pady=10)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'BG', 'BTN', 'R'
]
satir = 1
sutun = 0
for btn_text in buttons:
    b = tk.Button(root, text=btn_text, width=10, height=5, command = lambda btn=btn_text: on_click(btn))
    b.grid(row=satir, column=sutun)
    sutun += 1
    if sutun == 4:
        sutun = 0
        satir += 1
root.mainloop()








