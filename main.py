import requests

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Weather Application with Tkinter")

image = PhotoImage(file="weatherimage.png")
image_label = Label(window, image=image, padx=20, pady=20)
image_label.pack()

city_label = Label(window, text="Enter City: ")
city_label.pack()
city_entry = Entry(window)
city_entry.pack()

get_weather_button = Button(window, text="Get Weather")
get_weather_button.pack()

weather_label = Label(window,  text="")
weather_label.pack()


def get_weather():
    city = city_entry.get()
    api_key = "Enter Your API Key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather}")
        else:
            messagebox.showerror("Error", "City not found or typed it wrong!")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")

get_weather_button.config(command=get_weather)
window.mainloop()