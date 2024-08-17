import requests
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk

import ttkbootstrap


# OpenWeatherMap API Key
API_KEY = 'YOUR_API_KEY'


def get_weather(city, api_key):
    '''
    This is a function that gets the weather data for a choosen city from openweathermap API 

    city -> String
    api_key -> String
    '''
    endpoint = 'https://api.openweathermap.org/data/2.5/weather'
    
    params={
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    # getting the api request response
    response = requests.get(endpoint, params=params)

    # Converting the response to a JSON format
    data = response.json()

    return data


def get_weather_icon(icon_id):

    base_url = 'https://openweathermap.org/img/wn/'

    icon_url = f"{base_url}{icon_id}@2x.png"

    response = requests.get(icon_url,stream=True).raw
    
    icon = Image.open(response)

    return icon


def search():

    '''
    This function return the weather data for a the city that user searches for
    '''
    city = entry.get()  
    result = get_weather(city, API_KEY)

    if result == None:
        return
    
    # Requesting the icon from the openweathermap's server
    response = get_weather_icon(result['weather'][0]['icon'])

    # Converting it to a compatible format with the tkinter

    icon = ImageTk.PhotoImage(response)
    
    location = f"{result['name']}, {result['sys']['country']}"
    description = result['weather'][0]['description']
    temp = result['main']['temp']
    windspeed = result['wind']['speed']
    humidity = result['main']['humidity']

    location_label.configure(text=f"{location}")
    descriptionLabel.configure(text=f"Weather state: {description}")
    windspeed_label.configure(text=f"Wind speed: {windspeed}km/h")
    humidity_label.configure(text=f"Humidity: {humidity}%")
    temp_label.configure(text=f"Temperature: {temp}°C")
    weather.configure(image=icon)
    weather.image = icon


    


root = tk.Tk()

root.geometry("500x500")
root.title("Weather App")

# Search bar to specify the city which you want
entry = ttkbootstrap.Entry(root, font=('Helvetica', 18))
entry.pack(padx=20,pady=20)

# Submit the search
submit = ttkbootstrap.Button(root,style="success", text="Search", command=search,)
submit.pack()


# Location Label
location_label = tk.Label(root, text="", font=('Helvetica',24))
location_label.pack(pady=10)

# Weather state icon
weather = tk.Label(root, bg="black")
weather.pack()

# Description of the weather

descriptionLabel = tk.Label(root, text="", font=('Helvetica', 18))
descriptionLabel.pack(pady=10)

# Temperature

temp_label = tk.Label(root, text="", font=('Helvetica', 18))
temp_label.pack()

# Humidity

humidity_label = tk.Label(root, text="", font=('Helvetica', 18))
humidity_label.pack()

# Windspeed

windspeed_label = tk.Label(root, text="", font=('Helvetica', 18))
windspeed_label.pack()



root.mainloop()

    

