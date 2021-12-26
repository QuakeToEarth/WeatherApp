from tkinter import *
import requests
from PIL import Image, ImageTk

def fetch():
    city = city_text.get()
    link = 'https://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=22515dbe8047cf659da74a1cae281c2e'
    respone = requests.get(link)
    data = respone.json()
    country_label['text'] = '{}, {} '.format(data['name'],data['sys']['country'])
    tempreture_label['text'] = '{}°C'.format(data['main']['temp'])


root = Tk()
root.geometry('500x350')
bg = ImageTk.PhotoImage(file = 'skyBG.jpg')
canvas = Canvas(root, width=700, height= 3500)
canvas.pack(fill = BOTH, expand = True)
canvas.create_image(0,0,image = bg, anchor = 'nw')
root.title('Weather App')

city_text = StringVar()
city_entry = Entry(root,textvariable=city_text, bg = 'lightgrey').place(x = 160, y = 50)

country_label = Label(root,text = '', font = ('bold',20))
country_label.place(x = 190, y = 150)


tempreture_label = Label(root,text = '', font = ('bold', 20))
tempreture_label.place(x = 190, y = 180)


searchBar = Button(root, text = 'Search Weather :)', width=12, command = fetch).place(x = 200, y = 80)



root.mainloop()