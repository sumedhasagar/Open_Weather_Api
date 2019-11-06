import requests # fetches response from given input url
from tkinter import messagebox # shows a message box (can be error, info etc ) on the screen
#tkinter is GUI library of Python.
import tkinter as tk

def weather():
    city = city_name.get()
    mapping = {'Baddi':7279742, 'Noida': 7279746}
    url= "https://openweathermap.org/data/2.5/weather?id={}&appid=b6907d289e10d714a6e88b30761fae22".format(mapping[city])
    res=requests.get(url)
    output= res.json()

    # 404 error is an HTTP status code that means that,
    # the page you were trying to reach on a website couldn't be found on their server
    if output['cod'] != 404:
        weather_status=output['weather'][0]['description']
        temperature= output['main']['temp']
        humidity= output['main']['humidity']
        wind_speed= output['wind']['speed']
        	
        messagebox.showinfo("info", "Weather_Status: {}".format(weather_status))
        messagebox.showinfo("info", "Temperature: {}".format(temperature))

root= tk.Tk()
root.geometry( "400x350")

tk.Label(root,text="Enter city name:",font="bold",fg="black").grid(row=6,column=0)
city_name=tk.Entry(root,width=30,bd=10)
city_name.grid(row=6,column=1)

button = tk.Button(root,text='City Details',command=weather,bg="black",fg="white").grid(row=16,column=1,padx=20,pady=5)

root.mainloop()