import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Fibonacci clicker")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

Fib = [0, 1]

def command_1():
    global Fib
    Fib.append(Fib[-1] + Fib[-2])
    label.config(text=Fib[-1])

label = tk.Label(root,text="0", font=("Arial", 50))
label.grid(row=0, column=0, sticky="S")

label_1 = tk.Label(root,text="The Fibonacci clicker", font=("Arial", 16))
label_1.grid(row=0, column=0, sticky="N")

button = tk.Button(root, text="Click", command=command_1)
button.grid(row=1, column=0, sticky="N", pady=150)

root.mainloop()