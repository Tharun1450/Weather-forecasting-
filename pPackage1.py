from tkinter import *
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os
import pytz

def getWeather():
    try:
        cityName=textfield.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(cityName)
        print(location)
        obj1=TimezoneFinder()
        result=obj1.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)
        home=pytz.timezone(result)
        localTime=datetime.now(home)

        currentTime=localTime.strftime("%I:%M %p")
        clock.config(text=currentTime)
        name.config(text="CURRENT WEATHER:")

        application="https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid=bad6bdab51b6449ee6ca3f7b183ef54b"
        weatherData=requests.get(application).json()

        condition=weatherData['weather'][0]['description']
        temp1=int(weatherData['main']['temp']-273.15)
        pressure=weatherData['main']['pressure']
        humidity=weatherData['main']['humidity']
        wind=weatherData['wind']['speed']

        temp.config(text=(temp1,"C"))
        c.config(text=(condition,"|","FEELS","LIKE"))
        w.config(text=wind)
        h.config(text=humidity)
        p.config(text=pressure)

        file1=open("weatherData.txt","a")
        file1.write(str(location))
        file1.write(str(temp1))
        file1.close()

    except Exception as e:
        messagebox.showerror("Weather app","Network error or Invalid Input!")

def WeatherApp():
    process=Tk()
    process.title("Weather App")
    process.geometry("900x500")
    process.resizable(False,False)

    searchImage=PhotoImage(file='searchbox.png')
    image1=Label(image=searchImage)
    image1.place(x=20, y=20)

    global textfield
    textfield=Entry(process,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
    textfield.place(x=50,y=40)
    textfield.focus()

    searchIcon=PhotoImage(file="iconWeather.png")
    image2=Button(image=searchIcon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
    image2.place(x=420,y=34)

    searchLogo=PhotoImage(file="weather.png")
    image3=Label(image=searchLogo)
    image3.place(x=200,y=150)

    searchFrame=PhotoImage(file="frame.png")
    image4=Label(image=searchFrame)
    image4.pack(padx=5,pady=5,side=BOTTOM)

    # time
    global name,clock,temp,c,w,h,p
    name=Label(process, font=("arial",15,"bold"))
    name.place(x=100,y=100)
    clock=Label(process,font=("arial",20))
    clock.place(x=30,y=130)

    label1=Label(process,text="WIND",font=("Calibi",15,'bold'),fg="white",bg="#1ab5ef")
    label1.place(x=160,y=400)

    label2=Label(process,text="HUMIDITY",font=("Calibi",15,'bold'),fg="white",bg="#1ab5ef")
    label2.place(x=365,y=400)

    label4=Label(process,text="PRESSURE",font=("Calibi",15,'bold'),fg="white",bg="#1ab5ef")
    label4.place(x=600,y=400)

    temp=Label(font=("arial",70,"bold"),fg="#ee666d")
    temp.place(x=400,y=150)

    c=Label(font=("arial",15,'bold'))
    c.place(x=400, y=250)

    w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
    w.place(x=170, y=430)

    h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
    h.place(x=370, y=430)

    p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
    p.place(x=610, y=430)

    process.mainloop()
