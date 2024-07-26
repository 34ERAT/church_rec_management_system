from tkinter import END
import customtkinter as ctk
from middleware.Baptism import BAPTISM
from ui.components.Btn_Notify import Btn_Notify
# import tkinter as tk
# from ui.components.NotificationLable import NotificationLabel


class Baptism_rec(ctk.CTkFrame):
    def __init__(self, master,command):
        super().__init__(master)
        self.Command = command
        self.columnconfigure(0, weight=0)
        self.columnconfigure((1,2), weight=2)
        self.rowconfigure((0, 1, 2,3), weight=1)
        # baptism
        self.Label(0,"baptims no")
        self.entry_var = ctk.StringVar()
        self.entry_var.trace_add("write",self.on_entry_change)
        # self.entry_var.set("baptism_no e.g 001")

        self.baptism_no = ctk.CTkEntry(self,textvariable=self.entry_var, placeholder_text="baptism_no e.g 001")
        self.baptism_no.grid(row=0, column=1, padx=(
            10,0 ), pady=(10, 0), sticky="ew")
        #god_child
        self.Label(1,"god child")
        self.godchild = ctk.CTkEntry(self, placeholder_text="god child")
        self.godchild.grid(row=1, column=1, padx=(
            10, 0), pady=(10, 0), sticky="ew")

        self.Label(2,'Father name')
        self.father_names = ctk.CTkEntry(self,placeholder_text= "first_name  last_name ")
        self.father_names.grid(row=2, column=1, padx=(
            10, 0), pady=(10, 0), sticky="ew")

        self.Label(3,'Mother names')
        self.mother_names = ctk.CTkEntry(self,placeholder_text="first_name  last_name ")
        self.mother_names.grid(row=3, column=1, padx=(
            10, 0), pady=(10, 0), sticky="ew")

        self.image_path =None

        #choose file
        self.filepick= ctk.CTkButton(self,text="choose a file ...",command=self.selected_file)
        self.filepick.grid(row=1, column=2, padx=(
            10, 10), pady=(10, 0), sticky="ew")


    def selected_file(self):
        self._FILE_PATH =ctk.filedialog.askopenfilename(title="Select a file", filetypes=[("image files", "*.jpg"), ("All files", "*.*")])
        self.image_path= self._FILE_PATH
        self.Command(self._FILE_PATH)

    def set_image(self,path):
        self.image_path = path

    def on_entry_change(self,*args):
        value = self.entry_var.get()
        self.is_number(value)

    def is_number(self,value):
        if value == "" or value.isdigit() or value.replace(".", "", 1).isdigit():
            self.baptism_no.configure(text_color="white")  # Reset to default color when input is valid
            return True
        else:
            self.baptism_no.configure(text_color="#cf3c3c")  # Change to red color when input is invalid
            return False

    def get_entries(self):
       data= {
            "baptism_no":int(self.baptism_no.get()),
            "godchild":self.godchild.get(),
            "mother": self.mother_names.get(),
            "father": self.father_names.get(),
            "file_url": self.image_path
        } 
       return data
    def clear_entries(self):
            self.baptism_no.configure(state="normal")
            self.baptism_no.delete(0,END)
            self.godchild.configure(state="normal")
            self.godchild.delete(0,END)
            self.mother_names.configure(state="normal")
            self.mother_names.delete(0,END)
            self.father_names.configure(state="normal")
            self.father_names.delete(0,END)

    def Label(self, row, text):
        label = ctk.CTkLabel(self, text=text)
        label.grid(row=row, column=0, padx=(
            10,0 ), pady=(10, 0), sticky="ew")
        return label

class Edit_Baptism(Baptism_rec):
    def __init__(self, master,command):
        super().__init__(master,command=command)

        self.Edit = Btn_Notify(self, text="Edit",command=self.submit)
        self.Edit.grid(row=3, column=2, padx=(
            10,10), pady=(0, 0), sticky="ew")

    def submit(self):
        try:
            self.baptims = BAPTISM()
            self.baptims.update(self.get_entries())
            self.Edit.set_message(success=True,message="Edited")
        except:
            self.Edit.set_message(success=False,message="Error")


class Add_Baptism(Baptism_rec):
    def __init__(self, master,command):
        super().__init__(master,command=command)
        self.Add = Btn_Notify(self, text="Add",command=self.submit)
        self.Add.grid(row=3, column=2, padx=(
            10,10), pady=(0, 0), sticky="ew")

    def submit(self):
        try:
            self.baptims = BAPTISM()
            self.baptims.Add(self.get_entries())
            self.Add.set_message(success=True,message="Added:-]")
            self.clear_entries()
        except :
            self.Add.set_message(success=False,message="Error")



