from tkinter import END
import customtkinter as ctk
from middleware.death import Death
from ui.components.Btn_Notify import Btn_Notify
from ui.components.Table import Table

class DEATH_rec(ctk.CTkFrame):
    def __init__(self, master,command):
        super().__init__(master)
        self.Command=command
        self.columnconfigure(0, weight=0)
        self.columnconfigure((1,2), weight=2)
        self.rowconfigure((0, 1, 2,3), weight=1)

        self.Label(0,'Names')

        self.Names = ctk.CTkEntry(self,placeholder_text="first_name  last_name ")
        self.Names.grid(row=0, column=1, padx=(
            10,0 ), pady=(10, 0), sticky="ew")


        #choose file
        self.filepick= ctk.CTkButton(self,text="choose a file ...",command=self.selected_file)
        self.filepick.grid(row=1, column=2, padx=(
            10, 10), pady=(10, 0), sticky="ew")


    def selected_file(self):
        self._FILE_PATH =ctk.filedialog.askopenfilename(title="Select a file", filetypes=[("image files", "*.jpg"), ("All files", "*.*")])
        self.image_path= self._FILE_PATH
        self.Command(self._FILE_PATH)


    def Label(self, row, text):
        label = ctk.CTkLabel(self, text=text)
        label.grid(row=row, column=0, padx=(
            10,0 ), pady=(10, 0), sticky="ew")
        return label

    def get_entries(self):
       data= {
                "Names":self.Names.get(),
                "file_url":self.image_path 
            } 
       return data
    def clear_entries(self):
            self.Names.configure(state="normal")
            self.Names.delete(0,END)

class Edit_Death(DEATH_rec):
    def __init__(self, master,command):
        super().__init__(master,command=command)

        self.Edit = Btn_Notify(self, text="Edit",command=self.submit)
        self.Edit.grid(row=3, column=2, padx=(
            10,10), pady=(0, 0), sticky="ew")

    def submit(self):
        try:
            self.death = Death()
            self.death.update(self.get_entries())
            self.Edit.set_message(success=True,message="Edited")
        except:
            self.Edit.set_message(success=False,message="Error")

class Add_Death(DEATH_rec):

    def __init__(self, master,command):
        super().__init__(master,command=command)

        self.Add = Btn_Notify(self, text="Add",command=self.submit)
        self.Add.grid(row=3, column=2, padx=(
            10,10), pady=(0, 0), sticky="ew")

    def submit(self):
        try:
            self.death = Death()
            self.death.Add(self.get_entries())
            self.Add.set_message(success=True,message="Added")
            self.clear_entries()
        except:
            self.Add.set_message(success=False,message="Error")

