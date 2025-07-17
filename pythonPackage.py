from tkinter import *
import tkinter as tr
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

process=Tk()
process.title("Weather App")
process.geometry("900x500+300+200")
process.resizable(False,False)

def getWeather():
    try:
        cityName=textfield.get()
        print(cityName)
        geolocator=Nominatim(user_agent="geoapiExercises")
        weatherData=requests.get(application).json()
        #print(weatherData)

        
        #geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(cityName)
        print(location)
        obj1=TimezoneFinder()
        result=obj1.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        print(home)
        local_time=datetime.now(home)
        print(local_time)
        
        currentTime=localTime.strftime("%I:%M %p")
        clock.config(text=currentTime)
        name.config(text="CURRENT WEATHER: ")

        #WEATHER
        api="https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid=bad6bdab51b6449ee6ca3f7b183ef54b"  #missing code

        #print(application)
        weatherData=requests.get(application).json()
        #print(weatherData)
        condition=weatherData['weather'][0]['description']
        #print(condition)
        temp1=int(weatherData['main']['temp1']-273.15)
        #print(temp1)
        pressure=weatherData['main']['pressure']
        #print(pressure)
        humidity=weatherData['main']['humidity']
        #print(humidity)
        wind=weatherData['wind']['speed']
        #print(wind)

        temp.config(text=(temp1,"o"))
        c.config(text=(condition,"|","FEELS","LIKE",))
        w.config(text=wind)
        h.config(text=humidity)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!")



    
#search
searchImage=PhotoImage(file='searchbox.png')
image1=Label(image=searchImage)
image1.place(x=20,y=20)
textfield=tr.Entry(process,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

searchIcon=PhotoImage(file="iconWeather.png")
image2=Button(image=searchIcon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
image2.place(x=400,y=34)

searchLogo=PhotoImage(file="weather.png")
image3=Label(image=searchLogo)
image3.place(x=200,y=150)


searchFrame=PhotoImage(file="frame.png")
image4=Label(image=searchFrame)
image4.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(process,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(process,font=("arial",20))
clock.place(x=30,y=130)

label1=Label(process,text="WIND",font=("Calibi",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=160,y=400)

label2=Label(process,text="HUMUDITY",font=("Calibi",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=365,y=400)

#label3=Label(process,text="DESCRIPTION",font=("Calibi",15,'bold'),fg="white",bg="#lab5ef")
#label3.place(x=120,y=400)

label4=Label(process,text="PRESSURE",font=("Calibi",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=600,y=400)


temp=Label(font=("arial",70,"bold"),fg="#ee666d")
temp.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=280,y=430)

#w=Label(text="...",font("arial",20,"bold"),bg="#1ab5ef")
#w.place(x=120,y=430)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=670,y=430)


process.mainloop()
