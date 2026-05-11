from re import I
import tkinter as tk

DAY_CAL=2500
DAY_PRO=120
DAY_FAT=80
DAY_CARB=400

ate_cal=0
ate_pro=0
ate_fat=0
ate_carb=0

def update_remainders():
    """Update labels to show how many calories/macros remain."""
    remain_cal=DAY_CAL-ate_cal
    remain_protein=DAY_PRO-ate_pro
    remain_fat=DAY_FAT-ate_fat
    remain_carb=DAY_CARB-ate_carb

    label_cur_cal.config(text=f"Current Calories: {ate_cal}")
    label_cur_protein.config(text=f"Current Protein: {ate_pro}g")
    label_cur_fat.config(text=f"Current Fat: {ate_fat}g")
    label_cur_carbs.config(text=f"Current Carbs: {ate_carb}g")

    label_rem_cal.config(text=f"Remaining Calories: {remain_cal}")
    label_rem_protein.config(text=f"Remaining Protein: {remain_protein}g")
    label_rem_fat.config(text=f"Remaining Fat: {remain_fat}g")
    label_rem_carbs.config(text=f"Remaining Carbs: {remain_carb}g")
 # if negative change to red so user can see they went over their goal for the day
    if remain_cal < 0:
        label_rem_cal.config(fg="red")
    if remain_protein < 0:
        label_rem_protein.config(fg="red")
    if remain_fat < 0:
        label_rem_fat.config(fg="red")
    if remain_carb < 0:
        label_rem_carbs.config(fg="red")

def add_meal():
    if not all([entry_meal_cal.get(),entry_meal_protein.get(),entry_meal_fat.get(),entry_meal_carbs.get()]):
        return
    try:
        cal=float(entry_meal_cal.get())
        pro=float(entry_meal_protein.get())
        fat=float(entry_meal_fat.get())
        carb=float(entry_meal_carbs.get())
        if cal < 0 or pro < 0 or fat < 0 or carb < 0:
            return
        global ate_cal,ate_pro,ate_fat,ate_carb
        ate_cal+=cal
        ate_pro+=pro
        ate_fat+=fat
        ate_carb+=carb
        entry_meal_cal.delete(0,tk.END)
        entry_meal_protein.delete(0,tk.END)
        entry_meal_fat.delete(0,tk.END)
        entry_meal_carbs.delete(0,tk.END)
        update_remainders()
    except ValueError:
        pass

def reset_day():
    global ate_cal,ate_pro,ate_fat,ate_carb
    ate_cal=0
    ate_pro=0
    ate_fat=0
    ate_carb=0
    update_remainders()

# Create the main window
root=tk.Tk()
root.title("Simple Macro Tracker")

# Frame for meal entries
frame_meal=tk.Frame(root)
frame_meal.grid(row=0,column=0,padx=10,pady=10)

# Labels and entries for meal macros
label_meal_cal=tk.Label(frame_meal,text="Calories:")
label_meal_cal.grid(row=0,column=0,sticky="e")

entry_meal_cal=tk.Entry(frame_meal,width=10)
entry_meal_cal.grid(row=0,column=1,padx=5)

label_meal_protein=tk.Label(frame_meal,text="Protein (g):")
label_meal_protein.grid(row=1,column=0,sticky="e")

entry_meal_protein=tk.Entry(frame_meal,width=10)
entry_meal_protein.grid(row=1,column=1,padx=5)

label_meal_fat=tk.Label(frame_meal,text="Fat (g):")
label_meal_fat.grid(row=2,column=0,sticky="e")

entry_meal_fat=tk.Entry(frame_meal,width=10)
entry_meal_fat.grid(row=2,column=1,padx=5)

label_meal_carbs=tk.Label(frame_meal,text="Carbs (g):")
label_meal_carbs.grid(row=3,column=0,sticky="e")

entry_meal_carbs=tk.Entry(frame_meal,width=10)
entry_meal_carbs.grid(row=3,column=1,padx=5)

button_add_meal=tk.Button(frame_meal,text="Add Meal",command=add_meal)
button_add_meal.grid(row=4,column=0,columnspan=2,pady=5)

# Frame for current eaten
frame_current=tk.Frame(root)
frame_current.grid(row=1,column=0,padx=10,pady=10)

label_cur_cal=tk.Label(frame_current,text="Current Calories:")
label_cur_cal.grid(row=0,column=0,sticky="w")

label_cur_protein=tk.Label(frame_current,text="Current Protein:")
label_cur_protein.grid(row=1,column=0,sticky="w")

label_cur_fat=tk.Label(frame_current,text="Current Fat:")
label_cur_fat.grid(row=2,column=0,sticky="w")

label_cur_carbs=tk.Label(frame_current,text="Current Carbs:")
label_cur_carbs.grid(row=3,column=0,sticky="w")

# Frame for remainders
legend_rem=tk.Label(root,text="Red text indicates you have gone over your goal for the day.")
legend_rem.grid(row=5,column=0,padx=10,pady=10)

frame_remainder=tk.Frame(root)
frame_remainder.grid(row=2,column=0,padx=10,pady=10)

label_rem_cal=tk.Label(frame_remainder,text="Remaining Calories:")
label_rem_cal.grid(row=1,column=0,sticky="w")

label_rem_protein=tk.Label(frame_remainder,text="Remaining Protein:")
label_rem_protein.grid(row=2,column=0,sticky="w")

label_rem_fat=tk.Label(frame_remainder,text="Remaining Fat:")
label_rem_fat.grid(row=3,column=0,sticky="w")

label_rem_carbs=tk.Label(frame_remainder,text="Remaining Carbs:")
label_rem_carbs.grid(row=4,column=0,sticky="w")

# Reset button
button_reset_day=tk.Button(frame_remainder,text="Reset Daily Values",command=reset_day)
button_reset_day.grid(row=5,column=0,pady=5)


update_remainders()

root.mainloop()