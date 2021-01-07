from tkinter import *
from tkinter import ttk, messagebox 

root = Tk()

class Application:
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets()
        root.mainloop()
    
    def tela(self):
        self.root.title("Calculadora de Download")
        self.root.geometry("340x170")
        self.root.configure(background="#204031")
        self.root.resizable(False, False)

    def widgets(self):
        self.velocity_Lb = Label(self.root, text="Velocidade da internet(Mb ou Megas): ", font=("Calibri", 12), fg="#00ff8c", background="#204031")
        self.velocity_Lb.place(relx=0.02, rely=0.07)

        self.velocity = StringVar()
        self.velocity_Ent = Entry(self.root, font=("Calibri", 12), justify="center", fg="#204031", textvariable=self.velocity)
        self.velocity_Ent.place(relx=0.8, rely=0.06, relwidth=0.15, relheight=0.17)

        self.archsize_Lb = Label(self.root, text="Tamanho do Arquivo:", font=("Calibri", 12), fg="#00ff8c", bg="#204031")
        self.archsize_Lb.place(relx=0.02, rely=0.3)

        self.archsize = StringVar()
        self.archsize_Ent = Entry(self.root, font=("Calibri", 12), textvariable=self.archsize, justify="center", fg="#204031")
        self.archsize_Ent.place(relx=0.46, rely=0.287, relwidth=0.31, relheight=0.17)

        values = ["KB", "MB", "GB"]
        self.sizetype = ttk.Combobox(self.root, values=values, font=("Calibri", 12), state="readonly", justify='center')
        self.sizetype.set("MB")
        self.sizetype.place(relx=0.8, rely=0.285, relwidth=0.153, relheight=0.18)

        self.calculate_Btn = Button(self.root, text="Calcular", font=("Arial", 11), bg="#3f6956", fg="white", command=self.calculate)
        self.calculate_Btn.place(relx=0.02, rely=0.52, relwidth=0.97)

        self.timeDownload_Lb = Label(self.root, text="Tempo de Espera:", font=("Calibri", 14), fg="#00ff8c", background="#204031")
        self.timeDownload_Lb.place(relx=0.08, rely=0.755)

        self.hours = StringVar()
        self.hours_Ent = Entry(self.root, textvariable=self.hours, font=("Calibri", 12), fg="#204031", state="disabled", justify="center")
        self.hours_Ent.place(relx=0.535, rely=0.755, relwidth=0.1, relheight=0.17)

        self.twopoints1 = Label(self.root, text=":", font=("Calibri", 16), fg="#00ff8c", background="#204031")
        self.twopoints1.place(relx=0.634, rely=0.74)

        self.minutes = StringVar()
        self.minutes_Ent = Entry(self.root, textvariable=self.minutes, font=("Calibri", 12), fg="#204031", state="disabled", justify="center")
        self.minutes_Ent.place(relx=0.67, rely=0.755, relwidth=0.1, relheight=0.17)

        self.twopoints2 = Label(self.root, text=":", font=("Calibri", 16), fg="#00ff8c", background="#204031")
        self.twopoints2.place(relx=0.77, rely=0.74)

        self.seconds = StringVar()
        self.seconds_Ent = Entry(self.root, textvariable=self.seconds, font=("Calibri", 12), fg="#204031", state="readonly", justify="center", bg="white")
        self.seconds_Ent.place(relx=0.81, rely=0.755, relwidth=0.1, relheight=0.17)

    def calculate(self):
        veloc_net = self.velocity.get()
        arcsize = self.archsize.get()
        typesize = self.sizetype.get()

        if ',' in arcsize:
            arcsize = arcsize.replace(',', '.')
        
        try:
            veloc_net = int(veloc_net)
            arcsize = float(arcsize)
        except ValueError:
            messagebox.showerror("Erro", "Valor Invalido. Insira um valor real")
            return 0
        
        veloc_conv = veloc_net * 125
        metade = int(veloc_conv * 0.5)
        timingsec = 0
        timingmin = 0
        timinghor = 0

        if typesize == 'KB':
            timingsec = int(arcsize / metade)
        elif typesize == 'MB':
            arcsize *= 1024
            timingsec = int(arcsize / metade)
        elif typesize == 'GB':
            arcsize *= 1048576
            timingsec = int(arcsize / metade)

        if int(timingsec) == 0:
            self.hours.set("00")
            self.minutes.set("00")
            self.seconds.set("01")
            return 0
        
        elif int(timingsec) > 60:
            timingmin = timingsec / 60
            if timingmin > 60:
                timinghor = int(timingmin / 60)
                timingsec = int(timingsec) - (int(timingmin) * 60)
                timingmin = int(timingmin - (timinghor * 60))
                self.hours.set(timinghor)
                self.minutes.set(timingmin)
                self.seconds.set(timingsec)
                return 0
            else:
                timingmin = int(timingmin)
                timingsec = timingsec - (timingmin * 60)
                self.minutes.set(timingmin)
                self.seconds.set(timingsec)
                return 0
        else:
            self.hours.set("00")
            self.minutes.set("00")
            self.seconds.set(timingsec)


Application()