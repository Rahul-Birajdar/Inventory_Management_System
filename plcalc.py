from tkinter import *

#from profit_loss import calculateProfit, calculateLoss
class MyWindow:
    def __init__(self, win):
        global sp, cp
        self.lbl1=Label(win, text='SELLING PRICE')
        self.lbl2=Label(win, text='COST PRICE')
        self.lbl3=Label(win, text='RESUlT')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='PROFIT')
        self.btn2=Button(win, text='LOSS')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='PROFIT', command=self.calculateProfit)
        self.b2=Button(win, text='LOSS',command=self.calculateLoss)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    def calculateProfit(self):
        self.t3.delete(0, 'end')
        sp=int(self.t1.get())
        cp=int(self.t2.get())
        resultProfit=(sp-cp)
        self.t3.insert(END, str(resultProfit))
        return resultProfit
    def calculateLoss(self):
        self.t3.delete(0, 'end')
        sp=int(self.t1.get())
        cp=int(self.t2.get())
        resultLoss=(sp-cp)
        self.t3.insert(END, str(resultLoss))
        return resultLoss

    #if sp == cp:
    #    print("Neither profit nor Loss")

    #elif sp > cp:
    #    print("The Profit is", calculateProfit(sp,cp))

    #else:
    #    print("The Loss is", calculateLoss(sp,cp))

window=Tk()
mywin=MyWindow(window)
window.title('Application')
window.geometry("500x300+10+10")
window.configure(bg='yellow')
window.mainloop()

