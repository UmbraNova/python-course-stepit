from tkinter import *


credit = 0

def main():
    root = Tk()
    root.geometry("480x360")
    Label(root, text="Enter coins.[Press Buttons]").grid(row=1, column=1)
    # =====================================================================================


    display = Label(root, text=credit, bg="red") # we need this Label as a variable!
    display.grid(row=2, column=1)

    def add(amount):
        global credit
        credit += amount
        display.configure(text="%.2f" % credit)
    def sub(amount):
        global credit
        credit -= amount
        display.configure(text="%.2f" % credit)

    Button(root, text="10p", command=lambda: add(.1)).grid(row=3, column=1)
    Button(root, text="20p", command=lambda: sub(.2)).grid(row=4, column=1)
    Button(root, text="50p", command=lambda: sub(.5)).grid(row=5, column=1)
    Button(root, text="P1",  command=lambda: add(1.)).grid(row=6, column=1)


    # =====================================================================================
    root.mainloop()
main()