from tkinter import *
import tkinter.font as tkFont
import os
root = Tk()
arch = open("CreatorTkinter/novo_projeto.py", "a+")

if os.stat("CreatorTkinter/novo_projeto.py").st_size == 0:
    arch.write("from tkinter import *\n\n")
    arch.write("root = Tk()\n\n")
    arch.write("class Application:\n")
    arch.write("    def __init__(self):\n")
    arch.write("        self.root = root\n")
    arch.write("        self.tela()\n")
    arch.write("        self.widgets()\n")    
    arch.write("        root.mainloop()\n\n")

class Application:
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets()
        root.mainloop()
    
    def tela(self):
        self.root.title("Criador de Aplicativo Tkinter")
        self.root.geometry("330x500")
        self.root.configure(background="#3b5e4f")
        self.root.resizable(False, False)
    
    def widgets(self):
        self.fontstyle = tkFont.Font(family="Franklin Gothic", size=12, weight="bold")

        self.label_Btn = Button(self.root, text="Criar >>Label<<", font=self.fontstyle, bg="#73ba9c", fg="#0c1f17", relief="groove", activebackground="#5d967e")
        self.label_Btn.place(relx=0.3, rely=0.035, relheight=0.05)

        self.entry_Btn = Button(self.root, text="Criar >>Entry<<", font=self.fontstyle, bg="#73ba9c", fg="#0c1f17", relief="groove", activebackground="#5d967e")
        self.entry_Btn.place(relx=0.3, rely=0.135, relheight=0.05)

        self.button_Btn = Button(self.root, text="Criar >>Button<<", font=self.fontstyle, bg="#73ba9c", fg="#0c1f17", relief="groove", activebackground="#5d967e")
        self.button_Btn.place(relx=0.285, rely=0.235, relheight=0.05)

        self.combobox_Btn = Button(self.root, text="Criar >>Combobox<<", font=self.fontstyle, bg="#73ba9c", fg="#0c1f17", relief="groove", activebackground="#5d967e")
        self.combobox_Btn.place(relx=0.24, rely=0.335, relheight=0.05)

        self.view_Btn = Button(self.root, text="Ver Arquivo PY", font=self.fontstyle, bg="#73ba9c", fg="#0c1f17", relief="groove", activebackground="#5d967e", command=self.ver_arquivo)
        self.view_Btn.place(relx=0.3, rely=0.435, relheight=0.05)
    
    def ver_arquivo(self):
        if "Application()" not in arch.readlines():
            arch.write("\n\nApplication()")
        os.system("python CreatorTkinter/novo_projeto.py")
        arch.close()
Application()