import tkinter as tk
from tkinter import messagebox

def submit_order():
    name = name_entry.get()
    address = address_entry.get()
    size = size_var.get()
    
    # Collect selected toppings
    selected_toppings = []
    if pepperoni_var.get(): selected_toppings.append("Pepperoni")
    if mushrooms_var.get(): selected_toppings.append("Mushrooms")
    if onions_var.get(): selected_toppings.append("Onions")
    
    if not name or not address:
        messagebox.showwarning("Error", "Please fill in your name and address!")
        return

    # Order Summary Message
    summary = f"Customer: {name}\nAddress: {address}\nSize: {size}\nToppings: {', '.join(selected_toppings) if selected_toppings else 'None'}"
    messagebox.showinfo("Order Placed", f"Thank you, {name}!\n\nOrder Summary:\n{summary}")

# Main Window Setup
root = tk.Tk()
root.title("Python Pizza Delivery")
root.geometry("400x500")

# --- Customer Info ---
tk.Label(root, text="Pizza Order Form", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Delivery Address:").pack()
address_entry = tk.Entry(root, width=30)
address_entry.pack()

# --- Pizza Size (Radio Buttons) ---
tk.Label(root, text="\nSelect Size:", font=("Arial", 10, "bold")).pack()
size_var = tk.StringVar(value="Medium")
tk.Radiobutton(root, text="Small", variable=size_var, value="Small").pack()
tk.Radiobutton(root, text="Medium", variable=size_var, value="Medium").pack()
tk.Radiobutton(root, text="Large", variable=size_var, value="Large").pack()

# --- Toppings (Checkboxes) ---
tk.Label(root, text="\nSelect Toppings:", font=("Arial", 10, "bold")).pack()
pepperoni_var = tk.BooleanVar()
mushrooms_var = tk.BooleanVar()
onions_var = tk.BooleanVar()

tk.Checkbutton(root, text="Pepperoni", variable=pepperoni_var).pack()
tk.Checkbutton(root, text="Mushrooms", variable=mushrooms_var).pack()
tk.Checkbutton(root, text="Onions", variable=onions_var).pack()

# --- Submit Button ---
tk.Label(root, text="").pack() # Spacer
submit_btn = tk.Button(root, text="Place Order", command=submit_order, bg="green", fg="white", font=("Arial", 12, "bold"))
submit_btn.pack(pady=20)

root.mainloop()