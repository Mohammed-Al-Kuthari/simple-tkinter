from cProfile import label
from tkinter import TclError, ttk
import tkinter as tk
from patient import Patient

# Patients Store
patients = [Patient("ahmed", "21", "2022-2-21")]

root = tk.Tk()
root.resizable(400, 600)
root.title("Simple Patient App")
try:
    # windows only (remove the minimize/maximize button)
    root.attributes('-toolwindow', True)
except TclError:
    print('Not supported on your platform')

# layout on the root window
root.columnconfigure(0, weight=4)
root.rowconfigure(0, weight=3)


def create_input_frame(container, patients=patients):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Name
    ttk.Label(frame, text='Enter name:').grid(column=0, row=0, sticky=tk.W)
    name = ttk.Entry(frame, width=30)
    name.focus()
    name.grid(column=1, row=0, sticky=tk.W)

    # Age
    ttk.Label(frame, text='Enter age:').grid(column=0, row=1, sticky=tk.W)
    age = ttk.Entry(frame, width=30)
    age.grid(column=1, row=1, sticky=tk.W)

    # Date
    ttk.Label(frame, text='Enter date:').grid(column=0, row=2, sticky=tk.W)
    date = ttk.Entry(frame, width=30)
    date.grid(column=1, row=2, sticky=tk.W)

    def add_patient():
        new_patient = Patient(name.get(), age.get(), date.get())
        save_patient(new_patient, rebuild)

    # Add Button
    ttk.Button(frame, text="Add Patient", command=add_patient).grid(
        column=0, row=3, columnspan=2)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_show_frame(container, patients=patients):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Label(frame, text='Name', width=20).grid(column=0, row=0, sticky=tk.W)
    ttk.Label(frame, text='Age', width=20).grid(column=1, row=0, sticky=tk.W)
    ttk.Label(frame, text='Date', width=20).grid(column=2, row=0, sticky=tk.W)

    i = 1
    for patient in patients:
        ttk.Label(frame, text=patient.name, width=20).grid(
            column=0, row=i, sticky=tk.W)
        ttk.Label(frame, text=patient.age, width=20).grid(
            column=1, row=i, sticky=tk.W)
        ttk.Label(frame, text=patient.date, width=20).grid(
            column=2, row=i, sticky=tk.W)
        i += 1

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def save_patient(new_patient, rebuilder):
    patients.append(new_patient)
    rebuilder()


def rebuild():
    show_frame = create_show_frame(root)
    show_frame.grid(column=0, row=2)


input_frame = create_input_frame(root)
input_frame.grid(column=0, row=0)

rebuild()

root.mainloop()
