import csv

import customtkinter as ctk

from tkinter import filedialog, messagebox, simpledialog

import pyperclip

# --------------------------------------------------

# Main Function

# --------------------------------------------------

def edit_column_d():

    # Select CSV file

    filepath = filedialog.askopenfilename(

        title="Select ClubSpot CSV",

        initialdir="C:/Users/paul/Downloads",

        filetypes=[("CSV Files", "*.csv")]

    )

    if not filepath:

        messagebox.showinfo(

            "No File Selected",

            "You didn't choose a CSV file."

        )

        return

    # Ask Auto Renew question

    auto_renew = messagebox.askyesno(

        "Auto Renew Filter",

        "Auto Renew Draw only?\n\n"

        "YES = Only names with 'Enabled' in Column H\n\n"

        "NO = Include all names and add offline entries."

    )

    column_d_values = []

    # Read CSV

    with open(filepath, mode="r", newline="", encoding="utf-8") as f:

        reader = csv.reader(f)

        for row in reader:

            col_d = row[3] if len(row) >= 4 else ""

            if auto_renew:

                col_h = row[7] if len(row) >= 8 else ""

                if col_h.strip().lower() == "enabled":

                    column_d_values.append(col_d)

            else:

                column_d_values.append(col_d)

    # Offline entries

    if not auto_renew:

        num_offline = simpledialog.askinteger(

            "Offline Entries",

            "How many offline entries do you want to add?"

        )

        if num_offline is None or num_offline < 1:

            messagebox.showinfo(

                "No Entries Added",

                "You didn't enter a valid number."

            )

            return

        for i in range(1, num_offline + 1):

            column_d_values.append(f"offline entry {i}")

        filter_msg = f"Added {num_offline} offline entries."

    else:

        filter_msg = (

            "Auto Renew enabled.\n"

            "Only names marked as 'Enabled' were included."

        )

    # Copy to clipboard

    pyperclip.copy("\n".join(column_d_values))

    # Update status label

    status_label.configure(

        text="✅ Completed - Data copied to clipboard",

        text_color="#00C853"

    )

    # Success popup

    messagebox.showinfo(

        "Success",

        f"{filter_msg}\n\n"

        "The updated Column D list has been copied to your clipboard."

    )

# --------------------------------------------------

# CustomTkinter Setup

# --------------------------------------------------

ctk.set_appearance_mode("dark")     # dark / light / system

ctk.set_default_color_theme("blue")

root = ctk.CTk()

root.title("50/50 Draw Manager")

root.geometry("600x350")

root.resizable(False, False)

# --------------------------------------------------

# Header

# --------------------------------------------------

title_label = ctk.CTkLabel(

    root,

    text="50/50 Draw Manager",

    font=("Segoe UI", 28, "bold")

)

title_label.pack(pady=(30, 10))

subtitle_label = ctk.CTkLabel(

    root,

    text="Load a ClubSpot CSV and generate the updated draw list",

    font=("Segoe UI", 14)

)

subtitle_label.pack()

# --------------------------------------------------

# Main Button

# --------------------------------------------------

select_button = ctk.CTkButton(

    root,

    text="📂 Select CSV File",

    command=edit_column_d,

    width=250,

    height=45,

    font=("Segoe UI", 14, "bold")

)

select_button.pack(pady=40)

# --------------------------------------------------

# Status

# --------------------------------------------------

status_label = ctk.CTkLabel(

    root,

    text="Ready",

    font=("Segoe UI", 12),

    text_color="lightgray"

)

status_label.pack(side="bottom", pady=20)

# --------------------------------------------------

# Run App

# --------------------------------------------------

root.mainloop()

 
