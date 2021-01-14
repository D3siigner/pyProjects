from tkinter import *
import tkinter.font as tkFont
import math

root = Tk()
    
class Application:
    memory = []
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets()
        root.mainloop()
        
    def tela(self):
        self.root.geometry("321x502+500+100")
        self.root.title("Calculadora")
        self.root.configure(background="#e3e3e3")
        self.root.resizable(False, False)
    
    def widgets(self):
        self.ajuste = StringVar()
        self.otherview = StringVar()
        self.otherview_Lb = Label(self.root, textvariable=self.otherview, font=("Franklin Gothic", 9), justify="right", bd=0, bg="#e3e3e3", fg="#757575")
        self.otherview_Lb.place(relx=0.02, rely=0.1, relwidth=0.96)

        self.fontstyle = tkFont.Font(family="Franklin Gothic", size=33, weight="bold")
        self.viewer = StringVar()
        self.viewer.trace("w", self.on_write)
        self.viewer_Lb = Label(self.root, textvariable=self.viewer, font=self.fontstyle, justify="right", bd=0)
        self.viewer_Lb.place(relx=0.02, rely=0.14, relheight=0.11, relwidth=0.96)
        self.viewer.set("0")

        ### Grade de Botões - 1
        self.mc_Btn = Button(self.root, command=self.mc_function, text="MC", font=("Franklin Gothic", 9, "bold"), justify="center", state="disabled", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#e3e3e3")
        self.mc_Btn.place(relx=0.013, rely=0.283, relwidth=0.15, relheight=0.06)

        self.mr_Btn = Button(self.root, command=self.mr_function, text="MR", font=("Franklin Gothic", 9, "bold"), justify="center", state="disabled", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#e3e3e3")
        self.mr_Btn.place(relx=0.175, rely=0.283, relwidth=0.15, relheight=0.06)

        self.mplus_Btn = Button(self.root, command=self.mplus_function, text="M+", font=("Franklin Gothic", 9, "bold"), justify="center", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#e3e3e3")
        self.mplus_Btn.place(relx=0.338, rely=0.283, relwidth=0.15, relheight=0.06)

        self.mminus_Btn = Button(self.root, command=self.mminus_function, text="M-", font=("Franklin Gothic", 9, "bold"), justify="center", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#e3e3e3")
        self.mminus_Btn.place(relx=0.501, rely=0.283, relwidth=0.15, relheight=0.06)

        self.ms_Btn = Button(self.root, command=self.ms_function, text="MS", font=("Franklin Gothic", 9, "bold"), justify="center", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#e3e3e3")
        self.ms_Btn.place(relx=0.664, rely=0.283, relwidth=0.15, relheight=0.06)
        
        self.maba_Btn = Button(self.root, command=self.maba_function, text="M>", font=("Franklin Gothic", 9, "bold"), justify="center", state="disabled", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#e3e3e3")
        self.maba_Btn.place(relx=0.827, rely=0.283, relwidth=0.15, relheight=0.06)

        ### Grade de Botões - 2

        self.percent_Btn = Button(self.root, command=self.percent_function, text="%", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#d9dada")
        self.percent_Btn.place(relx=0.013, rely=0.35, relwidth=0.233, relheight=0.1)

        self.ce_Btn = Button(self.root, command=self.ce_function, text="CE", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#d9dada")
        self.ce_Btn.place(relx=0.259, rely=0.35, relwidth=0.233, relheight=0.1)

        self.c_Btn = Button(self.root, command=self.c_function, text="C", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#d9dada")
        self.c_Btn.place(relx=0.505, rely=0.35, relwidth=0.233, relheight=0.1)
        
        self.erase_Btn = Button(self.root, command=self.erase_function, text="X", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#d9dada")
        self.erase_Btn.place(relx=0.751, rely=0.35, relwidth=0.233, relheight=0.1)

        ### Grade de Botôes - 3

        self.onediv_Btn = Button(self.root, command=self.onediv_function, text="1/x", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#d9dada")
        self.onediv_Btn.place(relx=0.013, rely=0.46, relwidth=0.233, relheight=0.1)

        self.square_Btn = Button(self.root, command=self.square_function, text="x²", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#d9dada")
        self.square_Btn.place(relx=0.259, rely=0.46, relwidth=0.233, relheight=0.1)

        self.sqrt_Btn = Button(self.root, command=self.sqrt_function, text="²√x", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#d9dada")
        self.sqrt_Btn.place(relx=0.505, rely=0.46, relwidth=0.233, relheight=0.1)
        
        self.div_Btn = Button(self.root, command=self.div_function, text="/", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#d9dada")
        self.div_Btn.place(relx=0.751, rely=0.46, relwidth=0.233, relheight=0.1)
    
        ### Grade de Botôes - 4

        self.seven_Btn = Button(self.root, command=self.seven_function, text="7", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.seven_Btn.place(relx=0.013, rely=0.57, relwidth=0.233, relheight=0.1)

        self.eight_Btn = Button(self.root, command=self.eight_function, text="8", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.eight_Btn.place(relx=0.259, rely=0.57, relwidth=0.233, relheight=0.1)

        self.nine_Btn = Button(self.root, command=self.nine_function, text="9", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.nine_Btn.place(relx=0.505, rely=0.57, relwidth=0.233, relheight=0.1)
        
        self.multip_Btn = Button(self.root, command=self.multip_function, text="*", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#d9dada")
        self.multip_Btn.place(relx=0.751, rely=0.57, relwidth=0.233, relheight=0.1)

        ### Grade de Botôes - 5

        self.four_Btn = Button(self.root, command=self.four_function, text="4", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.four_Btn.place(relx=0.013, rely=0.68, relwidth=0.233, relheight=0.1)

        self.five_Btn = Button(self.root, command=self.five_function, text="5", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.five_Btn.place(relx=0.259, rely=0.68, relwidth=0.233, relheight=0.1)

        self.six_Btn = Button(self.root, command=self.six_function, text="6", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.six_Btn.place(relx=0.505, rely=0.68, relwidth=0.233, relheight=0.1)
        
        self.minus_Btn = Button(self.root, command=self.minus_function, text="-", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#d9dada")
        self.minus_Btn.place(relx=0.751, rely=0.68, relwidth=0.233, relheight=0.1)

        ### Grade de Botôes - 6

        self.one_Btn = Button(self.root, command=self.one_function, text="1", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.one_Btn.place(relx=0.013, rely=0.79, relwidth=0.233, relheight=0.1)

        self.two_Btn = Button(self.root, command=self.two_function, text="2", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.two_Btn.place(relx=0.259, rely=0.79, relwidth=0.233, relheight=0.1)

        self.three_Btn = Button(self.root, command=self.three_function, text="3", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.three_Btn.place(relx=0.505, rely=0.79, relwidth=0.233, relheight=0.1)
        
        self.plus_Btn = Button(self.root, command=self.plus_function, text="+", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#d9dada")
        self.plus_Btn.place(relx=0.751, rely=0.79, relwidth=0.233, relheight=0.1)

        ### Grade de Botôes - 7

        self.polarity_Btn = Button(self.root, text="+/-", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.polarity_Btn.place(relx=0.013, rely=0.895, relwidth=0.233, relheight=0.1)

        self.zero_Btn = Button(self.root, text="0", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.zero_Btn.place(relx=0.259, rely=0.895, relwidth=0.233, relheight=0.1)

        self.comma_Btn = Button(self.root, text=",", font=("Franklin Gothic", 9, "bold"), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#c9c9c9", highlightcolor="#4d4d4d", relief="sunken", bg="#f2f3f3")
        self.comma_Btn.place(relx=0.505, rely=0.895, relwidth=0.233, relheight=0.1)
        
        self.equal_Btn = Button(self.root, command=self.equal_function, text="=", font=("Franklin Gothic", 12), justify="center", state="normal", highlightbackground="#adadad", highlightthickness=10, bd=0, activebackground="#9a4aa4", highlightcolor="#4d4d4d", relief="sunken", bg="#aa7eb2")
        self.equal_Btn.place(relx=0.751, rely=0.895, relwidth=0.233, relheight=0.1)
    
    ### Funções

    def on_write(self, *args):
        print(self.viewer.get())
        s = self.viewer.get()
        fontsize = self.fontstyle['size']
        if s == "":
            self.viewer.set("0")
        #if len(s) > 3:
        #    a = str(format(int(s),",d").replace(",","."))
        #    print(a)
        #    self.viewer.set("")
        if len(s) > 1:
            if not s[-1].isdigit(): # retirar ultimo caracter caso nao seja digito
                self.viewer.set(s[:-1])
            else: # aproveitar apenas os primeiros 5 chars
                self.viewer.set(s[:21])
        
        if len(s) > 14:
            self.fontstyle["size"] -= 5
            if len(s) == 21:
                return 0

    def mc_function(self):
        if self.mc_Btn["state"] == "normal":
            self.memory = []
            self.mc_Btn["state"] = "disabled"
            self.mr_Btn["state"] = "disabled"
            self.maba_Btn["state"] = "disabled"
    def mr_function(self):
        if self.mr_Btn["state"] == "disabled":
            self.viewer.set(float(self.memory[-1]))

    def mplus_function(self):
        self.memory[-1] += float(self.viewer.get())
        if self.mc_Btn["state"] == "disabled":
            self.mc_Btn["state"] = "normal"
            self.mr_Btn["state"] = "normal"
            self.maba_Btn["state"] = "normal"

    def mminus_function(self):
        self.memory[-1] -= float(self.viewer.get())
        if self.mc_Btn["state"] == "disabled":
            self.mc_Btn["state"] = "normal"
            self.mr_Btn["state"] = "normal"
            self.maba_Btn["state"] = "normal"
    
    def ms_function(self):
        self.memory.append(float(self.viewer.get()))
        if self.mc_Btn["state"] == "disabled":
            self.mc_Btn["state"] = "normal"
            self.mr_Btn["state"] = "normal"
            self.maba_Btn["state"] = "normal"

    def maba_function(self):
        print(self.memory)
    
    def percent_function(self):
        self.viewer.set(float(self.viewer.get() / 100))

    def ce_function(self):
        self.viewer.set("0")
    
    def c_function(self):
        self.viewer.set("0")
        self.otherview.set("")
    
    def erase_function(self):
        if len(self.viewer.get()) == 1:
            self.viewer.set("0")
            return 0
        self.viewer.set(self.viewer.get()[0:-1])
    
    def onediv_function(self):
        self.otherview.set("1/({})".format(self.viewer.get()))
        self.viewer.set(1/float(self.viewer.get()))
    
    def square_function(self):
        self.otherview.set("sqr({})".format(self.viewer.get()))
        self.viewer.set(float(self.viewer.get()) ** 2)

    def sqrt_function(self):
        self.otherview.set("√({})".format(self.viewer.get()))
        self.viewer.set(float(self.viewer.get()) ** 0.5)
    
    def div_function(self):
        self.otherview.set("{} /".format(self.viewer.get()))
        self.ajuste = "0"
    
    def multip_function(self):
        self.otherview.set("{} *".format(self.viewer.get()))
        self.ajuste = "0"
    
    def minus_function(self):
        self.otherview.set("{} -".format(self.viewer.get()))
        self.ajuste = "0"

    def plus_function(self):
        self.otherview.set("{} +".format(self.viewer.get()))
        self.ajuste = "0"
    
    def equal_function(self):
        self.otherview.set(self.otherview.get() + str(self.viewer.get()))
        self.viewer.set(float(self.otherview.get()))
        self.ajuste = "0"

    def seven_function(self):
        if self.viewer.get() == "0":
            self.viewer.set(7)
            return 0
        
        if self.ajuste == "0":
            self.viewer.set(7)
            self.ajuste = "1"
            return 0

        self.viewer.set(str(self.viewer.get()) + str(7))
    
    def eight_function(self):
        if self.viewer.get() == "0":
            self.viewer.set(8)
            return 0
        
        if self.ajuste == "0":
            self.viewer.set(8)
            self.ajuste = "1"
            return 0

        self.viewer.set(str(self.viewer.get()) + str(8))
    
    def nine_function(self):
        if self.viewer.get() == "0":
            self.viewer.set("9")
            return 0
        
        if self.ajuste == "0":
            self.viewer.set("9")
            self.ajuste = "1"
            return 0

        self.viewer.set(str(self.viewer.get()) + str("9"))
    

    def four_function(self):
        if self.viewer.get() == "0":
            self.viewer.set("4")
            return 0
        
        if self.ajuste == "0":
            self.viewer.set("4")
            self.ajuste = "1"
            return 0

        self.viewer.set(str(self.viewer.get()) + str("4"))
    
    def five_function(self):
        if self.viewer.get() == "0":
            self.viewer.set("5")
            return 0
        
        if self.ajuste == "0":
            self.viewer.set("5")
            self.ajuste = "1"
            return 0

        self.viewer.set(str(self.viewer.get()) + str("5"))
    
    def six_function(self):
        if self.viewer.get() == "0":
            self.viewer.set("6")
            return 0
        
        if self.ajuste == "0":
            self.viewer.set("6")
            self.ajuste = "1"
            return 0

        self.viewer.set(str(self.viewer.get()) + str("6"))
    
    def one_function(self):
        if self.viewer.get() == "0":
            self.viewer.set("1")
            return 0
        
        if self.ajuste == "0":
            self.viewer.set("1")
            self.ajuste = "1"
            return 0

        self.viewer.set(str(self.viewer.get()) + str("1"))
    
    def two_function(self):
        if self.viewer.get() == "0":
            self.viewer.set("2")
            return 0
        
        if self.ajuste == "0":
            self.viewer.set("2")
            self.ajuste = "1"
            return 0

        self.viewer.set(str(self.viewer.get()) + str("2"))
    
    def three_function(self):
        if self.viewer.get() == "0":
            self.viewer.set("3")
            return 0
        
        if self.ajuste == "0":
            self.viewer.set("3")
            self.ajuste = "1"
            return 0

        self.viewer.set(str(self.viewer.get()) + str("3"))
    
    


Application()