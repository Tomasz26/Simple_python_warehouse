
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
import pandas as pd
from tkinter import messagebox


plik_excel = "dane.xlsx"
#plik_excel = r"C:\Users\Tomasz\Kurs Kodilla\dane.xlsx"

try:
    df = pd.read_excel(plik_excel, sheet_name="Sheet1")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Name", "Quantity", "Unit", "Unit Price ($)"])
    df.to_excel(plik_excel, index=False)
    print("Plik nie znaleziony. Utworzono nowy plik.")

revenue = df.at[0, "Revenue"]
#print(revenue)
cost = df.at[0, "Cost"]
#print(cost)
income = df.at[0, "Income"]
#print(income)

def odswiez_tabele():
    for wiersz in tree.get_children():
        tree.delete(wiersz)
    for index, rekord in df.iterrows():
        tree.insert("", "end", values=(rekord["Name"], rekord["Quantity"], rekord["Unit"], rekord["Unit Price ($)"]))

def add_item():
    #func tht adds items to excel database and sums cost and revenue

    global df, cost, revenue

    name = entry_1.get()
    quantity = entry_3.get()
    unit = entry_6.get()
    price = entry_7.get()

    if name and quantity and unit and price:

        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            messagebox.showerror("Invalid input", "Quantity must be an integer and price must be a number.")
            return

        nowy_wiersz = {"Name": name, "Quantity": quantity, "Unit": unit, "Unit Price ($)": price}
        df = pd.concat([df, pd.DataFrame([nowy_wiersz])], ignore_index=True)

        current_cost = round(quantity * price, 2)
        cost += current_cost
        revenue = round(revenue - (current_cost), 2)

        df.at[0, "Cost"] = cost 
        df.at[0, "Revenue"] = revenue

        canvas.itemconfig(tagOrId=cost_text, text=f"${cost}")
        canvas.itemconfig(tagOrId=revenue_text, text=f"${revenue}")

        entry_1.delete(0, "end")
        entry_3.delete(0, "end")
        entry_6.delete(0, "end")
        entry_7.delete(0, "end")
        messagebox.showinfo("Success", f"Add {quantity} of {name} for {quantity * price}.")
        
    print(f"Name: {name}, Quantity: {quantity}, Unit: {unit}, Price: {price}, Added {quantity * price} $ cost")
    odswiez_tabele()
    df.to_excel(plik_excel, index=False)


def sell_item():
    #this is a func tht sells item if they are present in database

    global df, revenue, income
    
    name = entry_2.get()
    quantity = entry_4.get()
    selling_price = entry_5.get()

    try:
        quantity = int(quantity)
        selling_price = float(selling_price)
    except ValueError:
        messagebox.showerror("Invalid input")
        return

    if name in df["Name"].values:
        index = df.index[df["Name"] == name].tolist()[0]
        actual_quantity = df.at[index, "Quantity"]

        if actual_quantity >= quantity:
            df.at[index, "Quantity"] = actual_quantity - quantity
            income += quantity * selling_price
            revenue += quantity * selling_price

            if df.at[index, "Quantity"] == 0:
                df.drop(index, inplace=True) 

            df.to_excel(plik_excel, index=False)
            
            df.at[0, "Income"] = income
            df.at[0, "Revenue"] = revenue
            canvas.itemconfig(tagOrId=income_text, text=f"${income}")
            canvas.itemconfig(tagOrId=revenue_text, text=f"${revenue}")

            entry_2.delete(0, "end")
            entry_4.delete(0, "end")
            entry_5.delete(0, "end")
            messagebox.showinfo("Success", f"Sold {quantity} of {name} for {quantity * selling_price}.")
            
        else:
            messagebox.showwarning("Insufficient quantity", f"Not enough {name} in stock.\nAvailable: {actual_quantity}.")
    else:
        messagebox.showerror("Item not found", f"{name} is not in the stock.")

    print(f"Name: {name}, Quantity: {quantity}, Selling price: {selling_price}, Added {quantity * selling_price} $ income")
    odswiez_tabele()
    df.to_excel(plik_excel, index=False)

    

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Python warehouse")

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    82.0,
    fill="#ADB6AF",
    outline="")

canvas.create_text(
    19.0,
    21.0,
    anchor="nw",
    text="Python Warehouse App",
    fill="#000000",
    font=("Inter SemiBold", 32 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    230.0,
    145.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    630.0,
    145.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1030.0,
    145.0,
    image=image_image_3
)

canvas.create_text(
    61.0,
    113.0,
    anchor="nw",
    text="Income",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    26.0,
    231.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    26.0,
    307.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    266.0,
    231.0,
    anchor="nw",
    text="Quantity",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    266.0,
    307.0,
    anchor="nw",
    text="Quantity",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    507.0,
    307.0,
    anchor="nw",
    text="Selling Price ($)",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    507.0,
    231.0,
    anchor="nw",
    text="Unit (kg, l)",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    747.0,
    231.0,
    anchor="nw",
    text="Unit Price ($)",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    461.0,
    113.0,
    anchor="nw",
    text="Costs",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    861.0,
    113.0,
    anchor="nw",
    text="Revenue",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

income_text = canvas.create_text(
    62.0,
    138.0,
    anchor="nw",
    text=income,
    fill="#000000",
    font=("Inter SemiBold", 32 * -1)
)

cost_text = canvas.create_text(
    462.0,
    138.0,
    anchor="nw",
    text=cost,
    fill="#000000",
    font=("Inter SemiBold", 32 * -1)
)

revenue_text = canvas.create_text(
    862.0,
    138.0,
    anchor="nw",
    text=revenue,
    fill="#000000",
    font=("Inter SemiBold", 32 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1100.0,
    570.0,
    image=image_image_4
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    133.5,
    278.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=35.0,
    y=256.0,
    width=197.0,
    height=42.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    133.5,
    354.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=35.0,
    y=332.0,
    width=197.0,
    height=42.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    373.5,
    278.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=275.0,
    y=256.0,
    width=197.0,
    height=42.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    373.5,
    354.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=275.0,
    y=332.0,
    width=197.0,
    height=42.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    614.5,
    354.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=516.0,
    y=332.0,
    width=197.0,
    height=42.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    614.5,
    278.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=516.0,
    y=256.0,
    width=197.0,
    height=42.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    854.5,
    278.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=756.0,
    y=256.0,
    width=197.0,
    height=42.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    text = "Add item",
    compound = "center",
    font=("Inter SemiBold", 24 * -1),
    borderwidth=0,
    highlightthickness=0,
    command = add_item,
    relief="flat"
)
button_1.place(
    x=995.0,
    y=256.0,
    width=264.0,
    height=44.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    text = "Sell item",
    compound = "center",
    font=("Inter SemiBold", 24 * -1),
    highlightthickness=0,
    command=sell_item,
    relief="flat"
)
button_2.place(
    x=995.0,
    y=332.0,
    width=264.0,
    height=44.0
)

canvas.create_text(
    1019.0,
    267.0,
    anchor="nw",
    text="Add unit to warehouse",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    1087.0,
    341.0,
    anchor="nw",
    text="Sell unit",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

kolumny = ["Name", "Quantity", "Unit", "Unit Price (PLN)"]
tree = ttk.Treeview(window, columns=kolumny, show="headings")
for kolumna in kolumny:
    tree.heading(kolumna, text=kolumna)
    tree.column(kolumna, width=150)

tree.place(x=30, y=450, width=800, height=200)

window.resizable(False, False)

odswiez_tabele()

window.mainloop()
