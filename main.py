from customtkinter import *
from PIL import Image
from BD_module import bd_format_email, bd_validate_email, bd_mask_password, BDUser

app = CTk()
app.title("app")
app.geometry("850x520")
set_appearance_mode("light")

userCred = {}

def slider_event(value):
    slider_label.configure(text=f"Slider value: {int(value)}")

logo_img = CTkImage(
    light_image=Image.open("assets/abstract.png"),
    dark_image=Image.open("assets/abstract.png"),
    size=(80, 80)
)
enterImage = CTkImage(
    light_image=Image.open("assets/enter.png"),
    dark_image=Image.open("assets/enter.png"),
    size=(20, 20)
)

logo_label = CTkLabel(app, image=logo_img, text="")
logo_label.pack(pady=(30, 10))

email_label = CTkLabel(app, text="Email", font=("Arial", 14))
email_label.pack(pady=(10, 0))
email_entry = CTkEntry(app, placeholder_text="Enter your email", width=250, font=("Arial", 14))
email_entry.pack(pady=(0, 15))

password_label = CTkLabel(app, text="Password", font=("Arial", 14))
password_label.pack(pady=(10, 0))
password_entry = CTkEntry(app, placeholder_text="Enter your password", show="*", width=250, font=("Arial", 14))
password_entry.pack(pady=(0, 15))

status_label = CTkLabel(app, text="", font=("Arial", 12))
status_label.pack(pady=(0, 10))

def BD_login_handler():
    email_raw = email_entry.get()
    email = bd_format_email(email_raw)
    if not bd_validate_email(email):
        status_label.configure(text="Invalid email", text_color="red")
        return
    password = password_entry.get()
    user = BDUser(email, password)
    userCred.clear()
    userCred.update(user.to_dict())
    userCred["slider"] = int(slider.get())
    print("User credentials:", userCred)
    print("User object:", user)
    status_label.configure(text=f"OK: {email} | {bd_mask_password(password)}", text_color="green")

login_btn = CTkButton(app, text="Login", command=BD_login_handler, fg_color="#5158D0", width=200, image=enterImage)
login_btn.pack(pady=20)

slider = CTkSlider(master=app, from_=0, to=100, command=slider_event, width=250)
slider.pack(pady=(20, 5))

slider_label = CTkLabel(app, text="Slider value: 0", font=("Arial", 12))
slider_label.pack()

app.mainloop()
