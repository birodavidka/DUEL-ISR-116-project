import customtkinter
from PIL import Image
import datetime
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Weather App")
app.geometry("480x380")

# Rács: engedjük nőni a belső frame-et
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

def getDateNow():
    now = datetime.datetime.now()
    monthName = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return f"{monthName[now.month-1]} {now.day}, {now.year}"

weatherData = {
    "place": "New York, US",
    "status": "default",
    "temp": 0,
    "heatIndex": None,
    "humidity": 0,
}

# NINCS text paraméter a CTkFrame-ben!
frame = customtkinter.CTkFrame(app)
frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# A belső rács is skálázható legyen
for c in (0, 1):
    frame.grid_columnconfigure(c, weight=1)
frame.grid_rowconfigure(1, weight=1)

cityLabel = customtkinter.CTkLabel(
    frame, text=weatherData["place"], font=("Arial", 25), anchor="w", width=180
)
cityLabel.grid(row=0, column=0, sticky="w")

dateLabel = customtkinter.CTkLabel(
    frame, text=getDateNow(), font=("Arial", 15), anchor="e", width=200
)
dateLabel.grid(row=0, column=1, sticky="e")

# Képelérés javítása + fallback
img_path = os.path.join("assets", "weatherImages", f"{weatherData['status']}.png")
if not os.path.exists(img_path):
    # fallback egy általános ikonra, pl. default.png ugyanebben a mappában
    img_path = os.path.join("assets", "weatherImages", "default.png")

try:
    weatherImg = customtkinter.CTkImage(Image.open(img_path), size=(120, 120))
    weatherImgLabel = customtkinter.CTkLabel(frame, text="", image=weatherImg, anchor="center")
except Exception as e:
    # Ha bármi gond van a képpel, legyen egy szöveges helyettesítés
    weatherImgLabel = customtkinter.CTkLabel(frame, text=f"[No image]\n{e}", anchor="center", justify="center")

weatherImgLabel.grid(row=1, column=0, columnspan=2, pady=20, sticky="nsew")

weatherLabel = customtkinter.CTkLabel(frame, text=f"{weatherData['temp']}°C", font=("Arial", 50), anchor="center")
weatherLabel.grid(row=2, column=0, columnspan=2,pady=[0,20], sticky="nsew")
tempLabel=customtkinter.CTkLabel(frame, text=f'Temperature: {weatherData['temp']}°C', font=("Arial", 20), anchor="w")
tempLabel.grid(row=3, column=0, columnspan=2, padx=2, sticky="w",)
heatLabel=customtkinter.CTkLabel(frame, text=f'Heat Index: {weatherData['heatIndex']}', font=("Arial", 20), anchor="w")
heatLabel.grid(row=5, column=0, columnspan=2, padx=2, sticky="w",)
humLabel=customtkinter.CTkLabel(frame, text=f'Humidity: {weatherData['humidity']}%', font=("Arial", 20), anchor="w")
humLabel.grid(row=6, column=0, columnspan=2, padx=2, sticky="w",)
app.resizable(False, False)
app.mainloop()
