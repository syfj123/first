import tkinter as tk
from turtle import update
root=tk.Tk()
root.title("Click counter")

timer=tk.Label(root,text="Timer: 10s",font=1000)
timer.place(x=50,y=70)


counter=tk.Label(root,text="Clicks: 0",font=1000)
counter.place(x=50,y=30)

time=10
clicks=0
started=False

def tick():
    global time
    if time>0:
        time-=1
        timer.config(text=f"Timer: {time}s")
        root.after(1000,tick)
    else:
        B1.config(state="disabled",text="Time's up!")

def click():
    global clicks, started
    if not started:
        started=True
        tick()
    clicks+=1   
    counter.config(text=f"Clicks: {clicks}")
    update_cps()

B1=tk.Button(root,text="Click Me!",font=1000,width=15,height=6,command=click)
B1.place(x=200,y=20)

CPS=tk.Label(root,text="CPS: 0",font=1000)
CPS.place(x=50,y=110)
def update_cps():
    if time>0:
        cps=clicks/(10-time)
        CPS.config(text=f"CPS: {cps:.2f}")
        root.after(1000,update_cps)
root.geometry("400x200")
root.mainloop()