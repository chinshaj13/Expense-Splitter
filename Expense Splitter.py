import tkinter as tk

root = tk.Tk()
root.title("Expense Splitter")
root.geometry("400x400")

frame = tk.Frame(root, bg="white", padx=20, pady=20, bd=1, relief="solid")
frame.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(
    frame, 
    text="Room Expense Splitter", 
    font=("Arial", 16, "bold"))
title.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(frame, text="Rent", font=("Arial", 12, "bold"), bg='white' , fg='black').grid(row=1, column=0, padx=10, pady=10)
rent_entry = tk.Entry(frame)
rent_entry.grid(row=1, column=1)

tk.Label(frame, text="Food", font=("Arial", 12, "bold"), bg='white' , fg='black').grid(row=2, column=0, padx=10, pady=10)
food_entry = tk.Entry(frame)
food_entry.grid(row=2, column=1)

tk.Label(frame, text="Electricity Units", font=("Arial", 12, "bold"), bg='white' , fg='black').grid(row=3, column=0, padx=10, pady=10)
units_entry = tk.Entry(frame)
units_entry.grid(row=3, column=1)

tk.Label(frame, text="Cost per Unit", font=("Arial", 12, "bold"), bg='white' , fg='black').grid(row=4, column=0, padx=10, pady=10)
cost_entry = tk.Entry(frame)
cost_entry.grid(row=4, column=1)

tk.Label(frame, text="Persons", font=("Arial", 12, "bold"), bg='white' , fg='black').grid(row=5, column=0, padx=10, pady=10)
persons_entry = tk.Entry(frame)
persons_entry.grid(row=5, column=1)

def calculate():
    try:
        rent = int(rent_entry.get())
        food = int(food_entry.get())
        units = int(units_entry.get())
        cost = int(cost_entry.get())
        persons = int(persons_entry.get())

        if persons <= 0:
            result_label.config(text="Persons must be > 0")
            return

        electricity = units * cost
        total = rent + food + electricity
        per_person = total / persons

        with open("expenses.txt", "a") as f:
            f.write(f"{rent},{food},{electricity},{per_person:.2f}\n")
        result_label.config(
            text=result_label.cget("text") + f"Rent: ₹{rent}\n"
                f"Food: ₹{food}\n"
                f"Electricity: ₹{electricity}\n\n"
                f"Per Person: ₹{per_person:.2f}")

    except ValueError:
        result_label.config(text="Please enter valid numbers")

def clear():
    rent_entry.delete(0, tk.END)
    food_entry.delete(0, tk.END)
    units_entry.delete(0, tk.END)
    cost_entry.delete(0, tk.END)
    persons_entry.delete(0, tk.END)
    result_label.config(text="")
tk.Button(frame, text="Calculate", command=calculate, bg="#4CAF50", fg="white", width=20).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Clear", command=clear, bg="sky blue", fg="white", width=20)\
    .grid(row=7, column=0, columnspan=2, pady=10)
result_label = tk.Label(frame, text="", font=("Arial", 12, "bold"), bg="white", fg="black", justify="left", anchor="w", wraplength=250)
result_label.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()