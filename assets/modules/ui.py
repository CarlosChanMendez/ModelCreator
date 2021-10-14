import tkinter as tk
from tkinter import messagebox
import os
import assets.modules.data_analyzer as data_analyzer

class UI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Model Creator")
        self.window.geometry("500x200")
        self.window.resizable(0,0)
        self.image_data = tk.PhotoImage(file=f"{os.getcwd()}/assets/img/ui_bottom_image.png")
        self.icon_folder = tk.PhotoImage(file=f"{os.getcwd()}/assets/img/icon_folder.png")
        self.createFileImport()
        self.createLineditPackage()
        self.createUiBottomImage()
        self.createButton()
    
    def createFileImport(self):
        container = tk.Frame()
        self.icon = tk.Label(container,text="File: ",width=10)
        self.lineedit = tk.Entry(container,bd=0,highlightcolor="royalblue")
        self.button = tk.Button(container, image=self.icon_folder, width=20, height="20")
        self.icon.pack(side="left")
        self.lineedit.pack(side="left", expand=True, fill="x")
        self.button.pack(side="left")
        container.pack(fill="x", padx=10,pady=10)    

    def createLineditPackage(self):
        container = tk.Frame()
        icon = tk.Label(container,text="Package: ",width=10)
        self.lineedit_package = tk.Entry(container,bd=0,highlightcolor="royalblue")
        icon.pack(side="left")
        self.lineedit_package.pack(side="left", expand=True, fill="x")
        container.pack(fill="x", padx=10,pady=5)
    
    def onClickButton(self):
        try:
            analyzer = data_analyzer.dataAnalyze(file=self.lineedit.get(),package=self.lineedit_package.get())
            analyzer.getTables()
        except:
            messagebox.showerror("Notificacion","Ha ocurrido un error")
            return 0
        messagebox.showinfo("Notificacion","Se han creado correctamente los modelos")

    
    def createButton(self):
        container = tk.Frame(self.window)
        button = tk.Button(text="Create Model",bg="#1894b4",fg="white", bd=0, width=25,height=2,command=self.onClickButton)
        button.configure(activebackground="#05445e",activeforeground="white")
        button.pack(side="top", pady=10)
        container.pack(side="top",fill="x")
    
    def createUiBottomImage(self):
        image = tk.Label(self.window, image=self.image_data)
        image.pack(side="bottom")

    def mainloop(self):
        self.window.mainloop()
        #a = data_analyzer.dataAnalyze(file="/home/carlos/Escritorio/SoftwareHacienda/db/dbhacienda.sql")
        #a.getTables()