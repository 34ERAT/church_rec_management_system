import customtkinter as ctk
from Navigation import Naviagation
from RecordsList import RecordList
from Preview import Preview

ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Church Record Management system")
        self.geometry("400x150")
        # self.grid_columnconfigure((0,1), weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=9)
        self.grid_rowconfigure((0, 1), weight=1)
        self.attributes('-fullscreen',True)
        self.leftFrame = ctk.CTkFrame(self)
        self.leftFrame.configure(fg_color="transparent")
        self.leftFrame.grid(row=0, column=0, padx=0, pady=(10,0), sticky="nsew" ,rowspan=2,columnspan=1)
        self.leftFrame.grid_columnconfigure((0,1),weight=1)
        self.leftFrame.grid_rowconfigure((1),weight=1)
        self.naviagation = Naviagation(self.leftFrame,width=700,height=100)
        self.naviagation.grid(row=0, column=0, padx=10, pady=(0), sticky="nsew" ,columnspan =2)

        self.recordlist = RecordList(self.leftFrame,title="Record List",width=700,height=590)
        self.recordlist.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsew",columnspan=2)

        self.preview= Preview(self,title="Preview window",width=600,height=00) 
        self.preview.grid(row=0, column=1, padx=(10,10), pady=(10,10), sticky="nsew",columnspan=2,rowspan=2)

app = App()
app.mainloop()
