from tkinter import *
from main import *
class GUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.wm_title("Comparison")
        self.geometry("300x300")
        self.B1 = Button(self,bg = "blue", text = "Automatic", command = automatic)
        self.B1.place(x = 60, y = 140)
        self.B2 = Button(self, text = "Manual", bg = "blue", command = self.helper)
        self.B2.place(x = 180, y = 140)
    def helper(self):
        self.top2 = Tk()
        self.top2.geometry("250x250")
        self.top2.wm_title("Manual")
        self.L1 = Label(self.top2, fg = "white" , bd = 5, bg = "black", text= "Size    ")
        self.L1.place(x = 50, y = 90)
        self.E1 = Entry(self.top2, bd = 5)
        self.E1.place(x = 110, y = 90)
        self.L2 = Label(self.top2, fg = "white", bd = 5, bg = "black", text = "Inputs")
        self.L2.place(x = 50, y = 125)
        self.E2 = Entry(self.top2, bd = 5)
        self.E2.place(x = 110, y = 125)
        self.B3 = Button(self.top2, text = "Compare", bg = "blue", command = self.manual)
        self.B3.place(x = 110, y = 160)
        self.L3 = Entry(self.top2, bd = 5)
        self.L3.place(x = 75, y = 190)
        self.top2.mainloop()
    def manual(self):
        self.siz = int(self.E1.get())
        self.str_nums = self.E2.get()
        self.tmp = self.str_nums.split()
        self.linked_list = Linkedlist()
        self.list = []
        self.list1 = []
        for i in range(0, self.siz):
            self.list.append(int(self.tmp[i]))
            self.list1.append(int(self.tmp[i]))
            self.linked_list.add(int(self.tmp[i]))
        self.list = Selection_Sort_Array(self.list)
        self.show = ""
        for i in range(len(self.list)):
            self.show += str(self.list[i]) + " "
        self.L3.insert(0, self.show)
        #help_manual(self.linked_list, self.list1, self.siz)


"""def manual():"""
"""
top = Tk()
top.wm_title("Comparison")
top.geometry("300x300")
B1 = Button(top,bg = "blue", text = "Automatic", command = automatic)
B1.place(x = 60, y = 140)
B2 = Button(top, text = "Manual", bg = "blue", command = helper)
B2.place(x = 180, y = 140)
top.mainloop()
"""
gui = GUI()
gui.mainloop()
