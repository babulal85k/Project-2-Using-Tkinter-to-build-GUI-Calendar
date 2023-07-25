import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def get_date():
    date = cal.get_date()
    selected_date_label.config(text="Selected Date: " + date)

# Step 1: Create the Tkinter window and configure its properties
root = tk.Tk()
root.title("Calendar Date Picker")
root.geometry("300x300")

# Step 2: Create the Calendar widget
cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
cal.pack(pady=20)

# Step 3: Create a button to trigger date selection and link it to the get_date() function
select_date_button = ttk.Button(root, text="Select Date", command=get_date)
select_date_button.pack()

# Step 4: Create a label to display the selected date
selected_date_label = ttk.Label(root, text="Selected Date: ")
selected_date_label.pack(pady=10)

# Step 7: Run the Tkinter event loop
root.mainloop()

#cap01_001