import random
import os
# import tkinter as tk
from tkinter import *


# ===== tkinter START
root = Tk()

myLabel1 = Label(
    root, 
    text="Hello World!", 
    # bg="black", 
    # fg="white",
    width=20,
    height=10
    )

myLabel2 = Label(
    root, 
    text="Hello World Two!", 
    width=20,
    height=10
    )

# myLabel1.pack()
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

myButton = Button(
    root, 
    text="Click MEEE!",
    padx=20,
    pady=20
    )
myButton.grid(row=0, column=2)

root.mainloop()
# ===== tkinter END


# ===== main code START
if os.path.isfile("_my_code/last_name.txt") == False:
    with open("_my_code/last_name.txt", "w") as fix_file:
        fix_file.write("a\nb")

last_name = open("_my_code/last_name.txt", "r")


def studentProbability(data):
    probChanged = []

    for student in data:
        for _ in range(student[1]):
            probChanged.append(student[0])
    return probChanged


def lastNameCheck(data):
    names_lines = last_name.readlines()
    for i_elem in range(len(data)):
        if data[i_elem][0] in names_lines[0]:
            data[i_elem][1] = 0
        if data[i_elem][0] in names_lines[1]:
            data[i_elem][1] = 0
       
    return data, names_lines


students = [
    ["Pila Andrei", 1], 
    ["Craciun Rafael Alexandru", 1],
    ["Rau Ivona Maria", 1],
    ["Andrei Stoiceanu", 1],
    ["Ivan Cecilia", 1],
    ["Tibrigan Nicolae", 1],
    ["Nedelcu Alexandru", 1],
    ["Robu Bogdan", 1],
    ["Andrei Netoiu", 0]
    ]

alter_students, prev_name = lastNameCheck(students)

result = studentProbability(alter_students)

if len(result) > 1:
    chosen_one = result[random.randint(0, len(result)-1)]
else:
    chosen_one = result[0]

last_name.close()

with open("_my_code/last_name.txt", "w") as a_file:
    a_file.write(prev_name[1]+"\n"+chosen_one)

print(chosen_one)
# ===== main code END