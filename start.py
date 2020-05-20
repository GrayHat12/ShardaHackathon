import pyfiglet
import requests
import keyboard
import main2
from os import system

def show_menu():
    global selected
    str0="Choose an option:"+'\n'
    str0+="{1} {0}. Hotel Booking {0} {2}".format(1, ">" if selected == 1 else " ", "<" if selected == 1 else " ")+'\n'
    str0+="{1} {0}. Flight Booking {0} {2}".format(2, ">" if selected == 2 else " ", "<" if selected == 2 else " ")+'\n'
    str0+="{1} {0}. Suggestions {0} {2}".format(3, ">" if selected == 3 else " ", "<" if selected == 3 else " ")
    print(str0)

def hotel_book():
    print('\n\n')
    hot = pyfiglet.figlet_format("Hotel Service",font='computer',width=100)
    print(hot)
    print('\n\n')
    input()
    area = input('Area Name / Hotel Name : ')
    rooms = str(int(input('Number of rooms : ')))
    date = input('Date Checkin (dd/mm/yyyy) : ')
    datedata = []
    defdatedata = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    if len(date) == 10:
        date = date.split('/')
        datedata.append(date[0])
        datedata.append(date[1])
        datedata.append(date[2])
        datedata[1] = defdatedata[int(datedata[1])+1]
    else:
        print('Incorrect Date format ',date)
        return
    date = input('Date Checkout (dd/mm/yyyy) : ')
    datedataout = []
    if len(date) == 10:
        date = date.split('/')
        datedataout.append(date[0])
        datedataout.append(date[1])
        datedataout.append(date[2])
        datedataout[1] = defdatedata[int(datedataout[1])+1]
    else:
        print('Incorrect Date format ',date)
        return
    data = main2.hotels(rooms,area,datedata[1],datedata[2],datedata[0],datedataout[1],datedataout[2],datedataout[0])
    print('\n\nHotels Found :',len(data.keys()),'\n\n')
    for key in data.keys():
        print('\n\n')
        print("URL :",data.get(key)['url'])
        print("IMAGE :",data.get(key)['img'])
        print("NAME :",data.get(key)['name'])
        print("AREA :",data.get(key)['area'])
        #print(data.get(key)['status'])
        print("PRICE :",data.get(key)['price'])
    
def flight_book():
    print('\n\n')
    hot = pyfiglet.figlet_format("Flight Service",font='computer',width=100)
    print(hot)
    print('\n\n')
    input()
    area = input('From City/Airport : ')
    rooms = input('To City/Airport : ')
    date = input('Date (dd/mm/yyyy) : ')
    datedata = []
    defdatedata = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    if len(date) == 10:
        date = date.split('/')
        datedata.append(date[0])
        datedata.append(date[1])
        datedata.append(date[2])
        datedata[1] = defdatedata[int(datedata[1])+1]
    else:
        print('Incorrect Date format ',date)
        return
    data = main2.flights(area,rooms,datedata[1],datedata[2],datedata[0])
    print('\n\nFlights Found :',len(data.keys()),'\n\n')
    for key in data.keys():
        print('\n\n')
        print("TITLE :",data.get(key)['title'])
        print("HELP :",data.get(key)['help'])
        print("FLIGHT :",data.get(key)['flight'])
        print("SOURCE :",data.get(key)['source'])
        print("DESTINATION :",data.get(key)['dest'])
        print("TIME :",data.get(key)['delay'])
        print("PRICE :",data.get(key)['price'])

def suggest():
    print('\n\n')
    hot = pyfiglet.figlet_format("Hotel Service",font='computer',width=100)
    print(hot)
    print('\n\n')
    input()
    area=input('City : ')
    data = main2.suggest_places(area)
    for res in data['results']:
        print()
        print(res['formatted_address'])

def up():
    global selected
    if selected == 1:
        return
    _=system('cls')
    selected -= 1
    print(pig)
    show_menu()

def down():
    global selected
    if selected == 3:
        return
    _=system('cls')
    selected += 1
    print(pig)
    show_menu()
    
def enter():
    _=system('cls')
    print(pig)
    global selected
    if selected == 1:
        hotel_book()
    elif selected == 2:
        flight_book()
    elif selected == 3:
        suggest()

_=system('cls')
pig = pyfiglet.figlet_format("GrayBot",font='computer',width=200)
print(pig)

selected = 1
show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter',enter)
keyboard.wait()