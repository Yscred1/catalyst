import tkinter as tk
from tkinter import messagebox

def calculate_fe():
    try:
        z = float(entry_z.get())
        C_product = float(entry_C.get()) /100
        I_current = float(entry_I.get())
        V_flowrate = float(entry_V.get()) * 0.0000166667
        F = 96485  # Faraday constant in C/mol
        Vm = 22.4
        n_product = (V_flowrate * C_product)/Vm
        FE = (z * F * n_product / I_current) * 100
        result_label.config(text=f"Faradaic Efficiency: {FE:.2f}%")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create GUI window
root = tk.Tk()
root.title("Faradaic Efficiency Calculator for gases")

tk.Label(root, text="Number of electrons transferred (z):").pack()
entry_z = tk.Entry(root)
entry_z.pack()

tk.Label(root, text="Volumefraction of the product x detected by GC (%):").pack()
entry_C = tk.Entry(root)
entry_C.pack()

tk.Label(root, text="Current applied (A):").pack()
entry_I = tk.Entry(root)
entry_I.pack()

tk.Label(root, text="CO2 gas flow rate (mL/min) ").pack()
entry_V = tk.Entry(root)
entry_V.pack()

tk.Button(root, text="Calculate FE", command=calculate_fe).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
