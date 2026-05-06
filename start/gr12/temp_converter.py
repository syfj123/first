import tkinter as tk

def calculate():
    try:
        if choice.get() == 1:  # Celsius input
            cel = float(cel_entr.get())
            far = cel * 1.8 + 32
            kel = cel + 273.15
            far_entr.delete(0, tk.END)
            far_entr.insert(0, f"{far:.2f}")
            kel_entr.delete(0, tk.END)
            kel_entr.insert(0, f"{kel:.2f}")
            result.config(text="Converted from Celsius")
        elif choice.get() == 2:  # Kelvin input
            kel = float(kel_entr.get())
            cel = kel - 273.15
            far = cel * 1.8 + 32
            cel_entr.delete(0, tk.END)
            cel_entr.insert(0, f"{cel:.2f}")
            far_entr.delete(0, tk.END)
            far_entr.insert(0, f"{far:.2f}")
            result.config(text="Converted from Kelvin")
        elif choice.get() == 3:  # Fahrenheit input
            far = float(far_entr.get())
            cel = (far - 32) / 1.8
            kel = cel + 273.15
            cel_entr.delete(0, tk.END)
            cel_entr.insert(0, f"{cel:.2f}")
            kel_entr.delete(0, tk.END)
            kel_entr.insert(0, f"{kel:.2f}")
            result.config(text="Converted from Fahrenheit")
        else:
            result.config(text="Select a unit")
    except ValueError:
        result.config(text="Invalid input")
    
root = tk.Tk()
root.geometry("600x400")
choice=tk.IntVar()
choice.set(1)
far_lab = tk.Label(text="Fahrenheit")
far_lab.grid(row=0, column=0, padx=10, pady=10)

far_entr = tk.Entry()
far_entr.grid(row=0, column=1, padx=10, pady=10)

rb1 = tk.Radiobutton(text="C",value=1,variable=choice)
rb1.grid(row=3, column=0, padx=10, pady=10)

rb2 = tk.Radiobutton(text="K",value=2,variable=choice)
rb2.grid(row=3, column=1, padx=10, pady=10)

rb3 = tk.Radiobutton(text="F",value=3,variable=choice)
rb3.grid(row=3, column=2, padx=10, pady=10)

cel_lab = tk.Label(text="Celsius")
cel_lab.grid(row=1, column=0, padx=10, pady=10)

cel_entr = tk.Entry()
cel_entr.grid(row=1, column=1, padx=10, pady=10)

kel_lab = tk.Label(text="Kelvin")
kel_lab.grid(row=2, column=0, padx=10, pady=10)

kel_entr = tk.Entry()
kel_entr.grid(row=2, column=1, padx=10, pady=10)

butt = tk.Button(text="Convert", command=calculate)
butt.grid(row=6, column=0, columnspan=2)

result = tk.Label(text="Result")
result.grid(row=7, column=0, columnspan=2)

root.mainloop()