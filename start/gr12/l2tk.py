import tkinter as tk
root=tk.Tk()
root.title("Click counter")

counter=tk.Label(root,text="Clicks: 0",font=1000)
counter.place(x=50,y=40)

clicks=0
def click():
    global clicks
    clicks+=1   
    counter.config(text=f"Clicks: {clicks}")

B1=tk.Button(root,text="Click Me!",font=1000,width=15,height=6,command=click)
B1.place(x=200,y=20)

root.geometry("400x200")
root.mainloop()