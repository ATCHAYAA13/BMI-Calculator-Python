#BMI CALCULATOR USING TKINTER WITH EXCEPTION HANDLING AND USER INPUT VALIDATION
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from packaging import version
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.title("BMI Calculator")
app.iconbitmap("D:\ATCHAYAA THINGAL\Projects\Oasis Infotech\BMI Calculator\Bmi icon.ico")
app.geometry("500x650")

#Image
bmi_image = ImageTk.PhotoImage(Image.open("D:\ATCHAYAA THINGAL\Projects\Oasis Infotech\BMI Calculator\BMI image.jpg"))
bmi1 = Label(app, image=bmi_image, bd=0)
bmi1.pack(pady=20)

def clear_screen():
    h.delete(0,END)
    w.delete(0,END)
    r.configure(text="")

def bmicalc():
    #weight(kg)/height(m)^2
    #rounded=round(int(w.get())/((int(h.get())/0.01)*(int(h.get())/0.01)),1)
    try:
        
        hegtry = float(h.get())
        heg = (float(h.get())/100)*(float(h.get())/100)
        weg = float(w.get())

        if hegtry==0 or weg==0:
            raise ValueError("Please give valid inputs.")        
        if hegtry<0 or weg<0:
            raise ValueError("Please give valid inputs.")
        if not hegtry or not weg:
            raise ValueError("Please give valid inputs.")
       
        rounded = round(float(weg/heg),1)
        #print(rounded)
        #r.config(text=f"{str(rounded)}")
    
        if rounded<18.5:
            r.configure(text=f"{str(rounded)}\nUnderweight",text_color="#54b1e1")
        elif rounded>18.5 and rounded<25:
            r.configure(text=f"{str(rounded)}\nNormal",text_color="#b3d686")
        elif rounded>25 and rounded<30:
            r.configure(text=f"{str(rounded)}\nOverweight",text_color="#fed429")
        elif rounded>30:
            r.configure(text=f"{str(rounded)}\nObesity",text_color="#fbaf42")
    except ValueError as v:
        messagebox.showerror("Invalid input",str(v))

#Textbox
h = customtkinter.CTkEntry(master = app, placeholder_text="Height in cm",width=200,height=30,border_width=1,corner_radius=20)
h.pack(pady=10)

w = customtkinter.CTkEntry(master = app, placeholder_text="Weight in kg",width=200,height=30,border_width=1,corner_radius=20)
w.pack(pady=20)

#buttons
b1 = customtkinter.CTkButton(master=app, text="Calculate BMI",width=190,height=40,fg_color="#951555",hover_color="#e6af2e",compound="top",command=bmicalc)
b1.pack(pady=10)
b2 = customtkinter.CTkButton(master=app, text="Clear Screen",width=190,height=40,fg_color="#771144",hover_color="#f67e7d",command=clear_screen)
b2.pack(pady=20)


#result
r = customtkinter.CTkLabel(master=app,text="",font=("Helvitica",24))
                           
r.pack(pady=10)

app.mainloop()