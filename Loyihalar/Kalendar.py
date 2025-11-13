import tkinter as tk
from tkcalendar import Calendar

# tkcalendar ni o'rnatish uchun terminalda: pip install tkcalendar

def tanlangan_sana():
    sana = cal.get_date()
    lbl.config(text=f"Tanlangan sana: {sana}")

root = tk.Tk()
root.title("Oddiy Kalendar Ilovasi")

cal = Calendar(root, selectmode='day', year=2025, month=9, day=15)
cal.pack(pady=20)

btn = tk.Button(root, text="Sanani tanlash", command=tanlangan_sana)
btn.pack(pady=10)

lbl = tk.Label(root, text="")
lbl.pack(pady=10)

root.mainloop()