import pyfiglet
import requests
import keyboard
import main2
from os import system
import json

# https://www.goibibo.com/hotels/the-daanish-residency-hotel-in-Delhi-1436991033012202026/?hquery={%22ci%22:%2220200606%22,%22co%22:%2220200608%22,%22r%22:%221-2-0%22,%22ibp%22:%22v3%22}&hmd=07e8570856fee84deaed9e8c2cdc2f2d88ac7d198e7086f95d4d92da417db27e157e849661f40a56468c45567f3c07079d7c313032b7267bb0713951e009e35fbd8c429870d1aa3344b364fbde63111f112d3ad244d788701917f43b386f44cec0791fb3b334d469e1ddd13ae081f2726f210a8233c6731124a5a1fb55abc048a5d3293680d782250f3b181333b31bbdfe8b5fb9d4e1c32e414a0d1bb7bf347a735db9894b75760a2582c3875cc0c3a6148c4345ab66017499b084706a17c4a02e590eb2ad51b540d60539a9945b2f28a2c03c218286f883056fd83bdadbe2ea92f26983717d01d527c4911e79f82d890aab59f98b6722d9fa18b45d35bd8d108b8821157e63b904f98b29b6a2df39c8288a54ecca08ff903bc8a1e25ac3&cc=IN

def show_menu():
    global selected
    str0="Choose an option:"+'\n'
    str0+="{1} {0}. Hotel Booking {0} {2}".format(1, ">" if selected == 1 else " ", "<" if selected == 1 else " ")+'\n'
    str0+="{1} {0}. Flight Booking {0} {2}".format(2, ">" if selected == 2 else " ", "<" if selected == 2 else " ")+'\n'
    str0+="{1} {0}. Suggestions {0} {2}".format(3, ">" if selected == 3 else " ", "<" if selected == 3 else " ")+'\n'
    str0+="{1} {0}. Exit {0} {2}".format(4, ">" if selected == 4 else " ", "<" if selected == 4 else " ")
    print(str0)

def hotel_book():
    print('\n\n')
    hot = pyfiglet.figlet_format("Hotel Service",font='computer',width=100)
    #print(hot)
    print('\n\n')
    input()
    area = input('Area Name / Hotel Name : ')
    date = input('Date Checkin (dd/mm/yyyy) : ')
    datedata = []
    defdatedata = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    if len(date) == 10:
        date = date.split('/')
        datedata.append(date[0])
        datedata.append(date[1])
        datedata.append(date[2])
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
    else:
        print('Incorrect Date format ',date)
        return
    rooms = int(input('Rooms : '))
    guests = int(input('Guests : '))
    resp = main2.customHotels(rooms,guests,area,datedata[1],datedata[2],datedata[0],datedataout[1],datedataout[2],datedataout[0])
    if resp == -1:
        print('You Entered an Invalid City Name')
        return
    data = []
    for dat in resp['data']:
        cdat = {
            'name' : dat['hn'],
            'area' : dat['l'],
            'image' : dat['t'],
            'desc' : dat['rtn'],
            'id' : dat['hc'],
            'price' : dat['spr'],
            'url name' : dat['hn'].replace(' ','-')
        }
        data.append(cdat)
    for dat in data:
        print('----'*40)
        print('Name :',dat['name'])
        print('Area :',dat['area'])
        print('Image :',dat['image'])
        print('Description :',dat['desc'])
        print('Url :','https://www.goibibo.com/hotels/name-hid/'.replace('hid',dat['id']).replace('name',dat['url name']))
        print('Price :',dat['price'])
    
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
        datedata[1] = defdatedata[int(datedata[1])-1]
    else:
        print('Incorrect Date format ',date)
        return
    try:
        data = main2.flights(area,rooms,datedata[1],datedata[2],datedata[0])
    except Exception as ex:
        print('Some unexpected Error Occured')
        print(ex)
        return
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
    try:
        data = main2.suggest_places(area)
    except Exception as ex:
        print('Some unexpected Error Occured')
        print(ex)
        return
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
    if selected == 4:
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
    elif selected == 4:
        _=system('cls')
        print('DONE')
        exit(0)
    print('\n(backspace to return to menu)')

def backspace():
    _=system('cls')
    print(pig)
    show_menu()


_=system('cls')
pig = pyfiglet.figlet_format("PBL Project",font='computer',width=200)
print(pig)

selected = 1
try:
    show_menu()
except:
    keyboard.unhook_all()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter',enter)
keyboard.add_hotkey('backspace',backspace)
keyboard.wait()