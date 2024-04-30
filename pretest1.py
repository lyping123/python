# import tkinter
# from tkinter import *


# root = tkinter.Tk()
# name = Label(root, text='name')
# age = Label(root, text='age')
# gender= Label(root, text='gender')
# email= Label(root, text='email')
# Entry(root).pack()
# address= Label(root, text='address')

# name.pack()
# Entry(root).pack()
# age.pack()
# Entry(root).pack()
# gender.pack()
# Entry(root).pack()
# email.pack()
# Entry(root).pack()
# address.pack()
# Entry(root).pack()

# voting1 = Label(root, text="What do you think of my service?")
# voting1.grid(row=0, column=0, sticky=W)
# v1 = IntVar()
# for i in range(1, 6):
#     Radiobutton(root, text=str(i), variable=v1, value=i).grid(row=0, column=i, sticky=W)

# # Question 2
# voting2 = Label(root, text="How do you think of my performance?")
# voting2.grid(row=1, column=0, sticky=W)
# v2 = IntVar()
# for i in range(1, 6):
#     Radiobutton(root, text=str(i), variable=v2, value=i).grid(row=1, column=i, sticky=W)

# # Question 3
# voting3 = Label(root, text="How do you think of my product?")
# voting3.grid(row=2, column=0, sticky=W)
# v3 = IntVar()
# for i in range(1, 6):
#     Radiobutton(root, text=str(i), variable=v3, value=i).grid(row=2, column=i, sticky=W)

# # Question 4
# voting4 = Label(root, text="Did the product quality meet your expectations?")
# voting4.grid(row=3, column=0, sticky=W)
# v4 = IntVar()
# for i in range(1, 6):
#     Radiobutton(root, text=str(i), variable=v4, value=i).grid(row=3, column=i, sticky=W)

# # Question 5
# voting5 = Label(root, text="Rate us!")
# voting5.grid(row=4, column=0, sticky=W)
# v5 = IntVar()
# for i in range(1, 6):
#     Radiobutton(root, text=str(i), variable=v5, value=i).grid(row=4, column=i, sticky=W)


# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
# mylist = Listbox(root, yscrollcommand=scrollbar.set)

# states=["Penang","Kedah","Perlis","Johor","Kelantan","Malacca","Negeri Sembilan","Pahang","Perak","Sabah","	Sarawak","Selangor","Terengganu"]

# for state in states:
#     mylist.insert(END,  str(state))
    
# mylist.pack(side=LEFT, fill=BOTH)
# scrollbar.config(command=mylist.yview)
# menu = Menu(root)
# root.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='Open...')
# filemenu.add_command(label='Save')
# filemenu.add_command(label='Save as')
# filemenu.add_command(label='Setting')
# filemenu.add_command(label='option')
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=root.quit)
# helpmenu = Menu(menu)
# menu.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='About')
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Combobox Example")
def on_select(event):
    ourMessage = combo_box.get()
    messageVar = tk.Message(root, text=ourMessage)
    messageVar.config(bg='lightgreen')
    messageVar.pack()


# Create a label
label = tk.Label(root, text="Please choose hobby")

combo_box = ttk.Combobox(root, values=["football", "basketball", "badminton","tenis","pin pon"])
combo_box.pack(pady=5)
combo_box.set("football")


combo_box.bind("<<ComboboxSelected>>", on_select)


root.mainloop()


