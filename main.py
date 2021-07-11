from tkinter import *
from tkinter.messagebox import *
font = ('verdana', 22, 'bold')



# creating a window
root = Tk()
root.title("SAMPLE CALCULATOR")
root.geometry("400x500")

# textfield
e = Entry(root, font=font, justify=CENTER, borderwidth= 10, )
e.pack(side=TOP, pady=10, fill=X, padx=10)


# frame for buttons
BtnFrame = Frame(root, bg="black")
BtnFrame.pack(side=TOP)

# functions for program
def all_clear():
    e.delete(0,END)

def clear():
    exp = e.get()
    exp = exp[0:len(exp)-1]
    e.delete(0,END)
    e.insert(0,exp)

def click_function(event):
    print('clicked')
    a = event.widget
    text=a['text']
    print(text)

    if text=='÷':
        e.insert(END,"/")
        return

    if text=='X':
        e.insert(END,"*")
        return

    if text=='=':
        try:
            exp=e.get()
            answer=eval(exp)
            e.delete(0,END)
            e.insert(0,answer)
        except Exception as d:
            print("Error....",d)
            showerror("error",d)
        return

    e.insert(END, text)



# adding buttons
num=1
for i in range(0,3):
    for j in range(0,3):
        btn = Button(BtnFrame, text=num, font=font, width=3, relief="raised", borderwidth=5)
        btn.grid(row=i, column=j, padx=5, pady=5)
        num += 1
        btn.bind('<Button-1>',click_function)

btnAllclear= Button(BtnFrame, text='AC', font=font, width=3, relief="raised", borderwidth=5, command=all_clear)
btnAllclear.grid(row=0, column=4, padx=5, pady=5)

btnAdd= Button(BtnFrame, text='+', font=font, width=3, relief="raised", borderwidth=5)
btnAdd.grid(row=1, column=4, padx=5, pady=5)

btnMultply= Button(BtnFrame, text='X', font=font, width=3, relief="raised", borderwidth=5)
btnMultply.grid(row=2, column=4, padx=5, pady=5)

btnZero =  Button(BtnFrame, text='0', font=font, width=3, relief="raised", borderwidth=5)
btnZero.grid(row=4, column=0, padx=5, pady=5)

btnDot =  Button(BtnFrame, text='.', font=font, width=3, relief="raised", borderwidth=5)
btnDot.grid(row=4, column=1, padx=5, pady=5)

btnSubtract =  Button(BtnFrame, text='-', font=font, width=3, relief="raised", borderwidth=5)
btnSubtract.grid(row=4, column=2, padx=5, pady=5)

btnDivide= Button(BtnFrame, text='÷', font=font, width=3, relief="raised", borderwidth=5)
btnDivide.grid(row=4, column=4, padx=5, pady=5)

btnClear= Button(BtnFrame, text='Clear', font=font, width=3, relief="raised", borderwidth=5, command=clear)
btnClear.grid(row=5, column=0, padx=5, pady=5, columnspan=2, ipadx=40)

btnEqual =  Button(BtnFrame, text='=', font=font, width=3, relief="raised", borderwidth=5)
btnEqual.grid(row=5, column=2, padx=5, pady=5, columnspan=3, ipadx=40)

#binding buttons

btnEqual.bind('<Button-1>', click_function)
btnDot.bind('<Button-1>',click_function)
btnDivide.bind('<Button-1>', click_function)
btnMultply.bind('<Button-1>',click_function)
btnSubtract.bind('<Button-1>', click_function)
btnAdd.bind('<Button-1>', click_function)
btnZero.bind('<Button-1>',click_function)

root.mainloop()