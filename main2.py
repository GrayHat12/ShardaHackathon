from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import requests
import json

options = Options()
#options.add_argument('--headless')
options.add_argument('chromedriver --log-level=OFF')
options.add_argument('--disable-gpu')
options.add_argument("--disable-logging")
options.add_argument('log-level=3')

path = r"C:\Users\Rahul\PaidProjects\ShardaHackathon\chromedriver.exe"

def flights(infrom="Delhi",into="Goa",trgetmonth="february",trgetyear="2020",trgetdate="12"):
    global options
    global path
    driver = webdriver.Chrome(executable_path=path,options=options)
    #driver = webdriver.Firefox(options=options)
    defdatedata = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    driver.get('https://www.goibibo.com/flights/')
    
    triptype = 0 #0 - one way, 1 - roundTrip
    if len(trgetdate)==1:
        trgetdate="0"+trgetdate
        
    trgtmnthnum = str(defdatedata.index(trgetmonth)+1)
    if len(trgtmnthnum) == 1:
        trgtmnthnum="0"+trgtmnthnum
    frmatdate = trgetyear+trgtmnthnum+trgetdate

    if triptype == 1:
        driver.find_element_by_id('roundTrip').click()
    
    drfrom = driver.find_element_by_id('gosuggest_inputSrc')
    drfrom.send_keys(infrom)
    time.sleep(3)
    driver.find_element_by_class_name('autoSuggestBoxList.flt.autoSgstFlt.autoSuggestBoxListHm').find_elements_by_tag_name('li')[0].click()

    drto = driver.find_element_by_id('gosuggest_inputDest')
    drto.send_keys(into)
    time.sleep(3)
    driver.find_element_by_class_name('autoSuggestBoxList.flt.autoSgstFlt.autoSuggestBoxListHm').find_elements_by_tag_name('li')[0].click()

    current_top_date = ["",""]
    driver.find_element_by_id('departureCalendar').click()
    datehead = driver.find_element_by_class_name('DayPicker-Caption').text.split(' ')

    current_top_date[0]=datehead[0].lower()
    current_top_date[1]=datehead[1].lower()

    if int(trgetyear) < int(current_top_date[1]):
        while driver.find_element_by_class_name('DayPicker-Caption').text.split(' ')[1].lower() != trgetyear:
            #print(driver.find_element_by_class_name('DayPicker-Caption').text.split(' ')[1])
            try:
                driver.find_element_by_class_name('DayPicker-NavButton DayPicker-NavButton--next'.replace(' ','.')).click()
            except:
                time.sleep(1)
    elif int(trgetyear) > int(current_top_date[1]):
        while driver.find_element_by_class_name('DayPicker-Caption').text.split(' ')[1].lower() != trgetyear:
            #print(driver.find_element_by_class_name('DayPicker-Caption').text.split(' ')[1])
            try:
                driver.find_element_by_class_name('DayPicker-NavButton DayPicker-NavButton--prev'.replace(' ','.')).click()
            except:
                time.sleep(1)

    if defdatedata.index(current_top_date[0]) < defdatedata.index(trgetmonth):
        while driver.find_element_by_class_name('DayPicker-Caption').text.split(' ')[0].lower() != trgetmonth:
            #print(driver.find_element_by_class_name('DayPicker-Caption').text.split(' ')[0])
            try:
                driver.find_element_by_class_name('DayPicker-NavButton DayPicker-NavButton--next'.replace(' ','.')).click()
            except:
                time.sleep(1)
    elif defdatedata.index(current_top_date[0]) > defdatedata.index(trgetmonth):
        while driver.find_element_by_class_name('DayPicker-Caption').text.split(' ')[0].lower() != trgetmonth:
            #print(driver.find_element_by_class_name('DayPicker-Caption').text.split(' ')[0])
            try:
                driver.find_element_by_class_name('DayPicker-NavButton DayPicker-NavButton--prev'.replace(' ','.')).click()
            except:
                time.sleep(1)

    #print(frmatdate)
    driver.find_element_by_id('fare_'+frmatdate).click()
    
    driver.find_element_by_id('gi_search_btn').click()
    time.sleep(5)
    i=0
    buttons = driver.find_elements_by_class_name('button fr fltbook fb widthF105 fb quicks'.replace(' ','.'))
    size = len(buttons)
    def_size = len('https://www.goibibo.com/flight-review/?ls=1&t=ba07793b209f65b2cbbd7a43e93372f6')
    data = dict()
    while i<size:
        but = driver.find_elements_by_class_name('button fr fltbook fb widthF105 fb quicks'.replace(' ','.'))[i]
        but.click()
        driver.switch_to.window(driver.window_handles[1])
        curl = driver.current_url
        time.sleep(5)
        if len(curl) == def_size:
            #print(driver.current_url)
            title = driver.find_element_by_class_name('fl mobdn ico18 padL10'.replace(' ','.')).text
            hlp=''
            try:
                hlp = driver.find_element_by_class_name('fr txtTransUpper white ico11 brRadius2 pad5 greenBgLt'.replace(' ','.')).text
            except:
                hlp = ''
            flight = driver.find_element_by_class_name('col-md-2 padT10 col-sm-2 col-xs-3 bkAirlineLogo'.replace(' ','.')).text
            img = driver.find_element_by_class_name('flightImagesNew').get_attribute('src')
            source = driver.find_element_by_class_name('col-md-3 col-sm-3 col-xs-4 padL20'.replace(' ','.')).text
            delay = driver.find_element_by_class_name('padLR10 whiteBg'.replace(' ','.')).text
            dest = driver.find_element_by_class_name('col-md-3 col-sm-3 col-xs-4 padL10 mobTxtRight'.replace(' ','.')).text
            price = driver.find_element_by_class_name('fr ico20 blue'.replace(' ','.')).text
            tdat = {
                'title' : title,
                'help' : hlp,
                'flight' : flight,
                'img' : img,
                'source' : source,
                'dest' : dest,
                'delay' : delay,
                'price' : price
            }
            data.update({str(i):tdat})
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        i+=1
    f=open('flight.json','w+')
    f.write(str(data).replace('\'','\"'))
    f.close()
    driver.close()
    return data

def suggest_places(city="New Delhi"):
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=city+point+of+interest&language=en&key='
    api = 'AIzaSyArxL9rYIDW4sjqa6615Wa1jc4pNfh7I20'
    url = url+api
    city = city.replace(' ','+')
    url=url.replace('city',city)
    print(url)
    r = requests.get(url=url)
    with open('places.json', 'w+') as f:
        json.dump(r.json(), f)
    return r.json()

def hotels(rooms='1',name="Delhi",trgetmonth="february",trgetyear="2020",trgetdate="12",retmonth="february",retyear="2020",retdate="14"):
    global options
    global path
    driver = webdriver.Chrome(executable_path=path,options=options)
    #driver = webdriver.Firefox(options=options)
    defdatedata = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    driver.get('https://www.goibibo.com/hotels/')
    if len(trgetdate)==1:
        trgetdate = "0"+trgetdate
    if len(retdate)==1:
        retdate = "0"+retdate
    trgtmnthnum = str(defdatedata.index(trgetmonth)+1)
    if len(trgtmnthnum) == 1:
        trgtmnthnum="0"+trgtmnthnum
    frmatdate = trgetyear+trgtmnthnum+trgetdate
    retmonthnum = str(defdatedata.index(retmonth)+1)
    if len(retmonthnum)==1:
        retmonthnum = "0"+retmonthnum
    frmatdateret = retyear+retmonthnum+retdate
    #driver.find_element_by_id('gosuggest_inputL').send_keys(name)
    driver.find_element_by_id('downshift-1-input').send_keys(name)
    time.sleep(2)
    driver.find_element_by_id('downshift-1-menu').find_elements_by_tag_name('li')[0].click()
    #driver.find_element_by_class_name('searchList').find_elements_by_tag_name('li')[0].click()
    date_fields = driver.find_elements_by_class_name('SearchBlockUIstyles__CheckInDateWrapDiv-fity7j-13 jKVcTv'.replace(' ','.'))
    check_in = date_fields[0]
    check_out = date_fields[1]
    #if check_in.get_attribute('placeholder') == 'Choose Checkin':
    #    print()
    #else:
    #    check_in = check_out
    #    check_out = date_fields[0]
    
    check_in.click()
    time.sleep(1)
    print('Check in clicked')
    current_top_date = ["",""]
    datehead = driver.find_element_by_class_name('dcalendarstyles__MonthNamePara-r2jz2t-3 bVBYQn'.replace(' ','.')).text.split(' ')
    current_top_date[0]=datehead[0].lower()
    current_top_date[1]=datehead[1].lower()
    if int(trgetyear) < int(current_top_date[1]):
        while driver.find_element_by_class_name('dcalendarstyles__MonthNamePara-r2jz2t-3 bVBYQn'.replace(' ','.')).text.split(' ')[1].lower() != trgetyear:
            try:
                driver.find_element_by_class_name('dcalendarstyles__MonthChangeRightArrowDiv-r2jz2t-16 eVCvYn'.replace(' ','.')).click()
            except:
                time.sleep(1)
    elif int(trgetyear) > int(current_top_date[1]):
        while driver.find_element_by_class_name('dcalendarstyles__MonthNamePara-r2jz2t-3 bVBYQn'.replace(' ','.')).text.split(' ')[1].lower() != trgetmonth:
            try:
                driver.find_element_by_class_name('dcalendarstyles__MonthChangeLeftArrowDiv-r2jz2t-15 jxjYIU'.replace(' ','.')).click()
            except:
                time.sleep(1)
    
    if defdatedata.index(current_top_date[0]) < defdatedata.index(trgetmonth):
        while driver.find_element_by_class_name('dcalendarstyles__MonthNamePara-r2jz2t-3 bVBYQn'.replace(' ','.')).text.split(' ')[0].lower() != trgetmonth:
            try:
                driver.find_element_by_class_name('dcalendarstyles__MonthChangeRightArrowDiv-r2jz2t-16 eVCvYn'.replace(' ','.')).click()
            except:
                time.sleep(1)
    elif defdatedata.index(current_top_date[0]) > defdatedata.index(trgetmonth):
        while driver.find_element_by_class_name('dcalendarstyles__MonthNamePara-r2jz2t-3 bVBYQn'.replace(' ','.')).text.split(' ')[0].lower() != trgetmonth:
            try:
                driver.find_element_by_class_name('dcalendarstyles__MonthChangeLeftArrowDiv-r2jz2t-15 jxjYIU'.replace(' ','.')).click()
            except:
                time.sleep(1)

    #driver.find_element_by_id('fare_'+frmatdate).click()
    for el in driver.find_elements_by_class_name('dcalendarstyles__DateWrapDiv-r2jz2t-7 SVVbO'.replace(' ','.')):
        try:
            if int(el.text) == int(trgetdate):
                el.click()
                break
        except:
            pass
    
    print('check in done')
    time.sleep(2)
    check_out.click()
    time.sleep(2)
    datehead = driver.find_element_by_class_name('dcalendarstyles__MonthNamePara-r2jz2t-3 bVBYQn').text.split(' ')
    current_top_date[0]=datehead[0].lower()
    current_top_date[1]=datehead[1].lower()
    if int(retyear) < int(current_top_date[1]):
        while driver.find_element_by_class_name('dcalendarstyles__MonthNamePara-r2jz2t-3 bVBYQn').text.split(' ')[1].lower() != retyear:
            try:
                driver.find_element_by_class_name('dcalendarstyles__MonthChangeRightArrowDiv-r2jz2t-16 eVCvYn'.replace(' ','.')).click()
            except:
                time.sleep(1)
    elif int(retyear) > int(current_top_date[1]):
        while driver.find_element_by_class_name('dcalendarstyles__MonthNamePara-r2jz2t-3 bVBYQn').text.split(' ')[1].lower() != retyear:
            try:
                driver.find_element_by_class_name('dcalendarstyles__MonthChangeLeftArrowDiv-r2jz2t-15 jxjYIU'.replace(' ','.')).click()
            except:
                time.sleep(1)
    
    if defdatedata.index(current_top_date[0]) < defdatedata.index(retmonth):
        while driver.find_element_by_class_name('dcalendarstyles__MonthNamePara-r2jz2t-3 bVBYQn').text.split(' ')[0].lower() != retmonth:
            try:
                driver.find_element_by_class_name('dcalendarstyles__MonthChangeRightArrowDiv-r2jz2t-16 eVCvYn'.replace(' ','.')).click()
            except:
                time.sleep(1)
    elif defdatedata.index(current_top_date[0]) > defdatedata.index(retmonth):
        while driver.find_element_by_class_name('dcalendarstyles__MonthNamePara-r2jz2t-3 bVBYQn').text.split(' ')[0].lower() != retmonth:
            try:
                driver.find_element_by_class_name('dcalendarstyles__MonthChangeLeftArrowDiv-r2jz2t-15 jxjYIU'.replace(' ','.')).click()
            except:
                time.sleep(1)

    #driver.find_element_by_id('fare_'+frmatdateret).click()
    for el in driver.find_elements_by_class_name('dcalendarstyles__DateWrapDiv-r2jz2t-7 SVVbO'.replace(' ','.')):
        try:
            if int(el.text) == int(retdate):
                el.click()
                break
        except:
            pass
    
    driver.find_element_by_id('home_textHook').click()
    select = driver.find_element_by_name('Room(s)')
    for options in select.find_elements_by_tag_name('option'):
        if options.text == rooms:
            options.click()
            break
    select = driver.find_element_by_name('Adult')
    for options in select.find_elements_by_tag_name('option'):
        if options.text == '1':
            options.click()
            break
    driver.find_element_by_class_name('button blue fr margin5 small'.replace(' ','.')).click()
    driver.find_element_by_class_name('width100 button orange xlarge'.replace(' ','.')).click()
    time.sleep(5)
    hotels = driver.find_elements_by_class_name('newSrpCard')
    data = dict()
    i=0
    for hotel in hotels:
        imgel = hotel.find_element_by_class_name('col-md-4 col-sm-4 col-xs-12 pad10 posRel'.replace(' ','.'))
        img = imgel.find_element_by_tag_name('img').get_attribute('src')
        url = imgel.find_element_by_tag_name('a').get_attribute('href')
        restel = hotel.find_element_by_class_name('col-md-8 col-sm-8 col-xs-6 pad0'.replace(' ','.'))
        priceel = hotel.find_element_by_class_name('col-md-4 col-sm-4 col-xs-6 pad10 borderLeft'.replace(' ','.'))
        title = restel.find_element_by_class_name('width100 fl padT10 padB5'.replace(' ','.')).find_element_by_class_name('ico20.fb').text
        area = restel.find_element_by_class_name('width100 fl padT5 padB15'.replace(' ','.')).find_element_by_class_name('ico13.grey').text
        #status = restel.find_element_by_class_name('width100 fl padB10'.replace(' ','.')).find_element_by_class_name('ico13.green').text
        price = priceel.find_element_by_class_name('dib padL5 ico25 fb vMid'.replace(' ','.')).text
        tdat = {
            'url' : url,
            'img' : img,
            'name' : title,
            'area' : area,
            #'status' : status,
            'price' : price
        }
        #print(tdat)
        data.update({i:tdat})
        i+=1
    with open('hotel.json','w+') as f:
        json.dump(data,f)
    driver.close()
    return data

def getPlaces(snt=[]):
    places = []
    for pl in snt:
        ch = pl[0]
        f = open('IN/'+ch+'.txt','r',encoding='utf-8')
        data = f.readlines()
        #print(data)
        f.close()
        #print(pl)
        if pl+'\n' in data:
            places.append(pl)
    i=0
    while i<len(snt)-1:
        ch0 = snt[i]
        ch1 = snt[i+1]
        f = open('IN/'+ch0[0]+'.txt','r',encoding='utf-8')
        data = f.readlines()
        f.close()
        #print(ch0+ch1)
        if ch0+ch1+'\n' in data:
            places.append(ch0+' '+ch1)
        i+=1
    return places
           
def customHotels(rooms=1,guest=1,name="New Delhi",trgetmonth='02',trgetyear='2020',trgetdate='12',retmonth='02',retyear='2020',retdate='14'):
    global options
    global path
    data = json.load(open('cities.json','r+',encoding='utf-8'))
    fname = name.replace(' ','').lower()
    cities = list(data.keys())
    if fname not in cities:
        print('City Not Found')
        return -1
    driver = webdriver.Chrome(options=options,executable_path=path)
    driver.get('https://www.goibibo.com/hotels/')
    cookies = driver.get_cookies()
    fcookie = ''
    names = []
    for cook in cookies:
        if cook['name'] in names:
            continue
        names.append(cook['name'])
        fcookie+= cook['name']+'='+cook['value']+';'
    #print(fcookie)
    driver.close()
    url = 'https://hermes.goibibo.com/hotels/v12/search/data/v3/cityid/fromdate/todate/rooms-guest-0?s=popularity&cur=INR&tmz=-330'
    url = url.replace('cityid',data[fname]['id'])
    url = url.replace('fromdate',trgetyear+trgetmonth+trgetdate)
    url = url.replace('todate',retyear+retmonth+retdate)
    url = url.replace('rooms',str(rooms))
    url = url.replace('guest',str(guest))
    print(url)
    headers = {
        "User-Agent": "PostmanRuntime/7.25.0",
        'authority' : 'www.goibibo.com',
        'cookie' : fcookie,
        'host' : 'hermes.goibibo.com',
        'accept' : '*/*',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Connection' : 'keep-alive'
        }
    resp = requests.get(url,headers=headers)
    #print(resp.headers)
    #print(364,resp.request.headers)
    hotelData = resp.text
    #print(hotelData)
    hotelData = json.loads(hotelData)
    json.dump(hotelData,open('hotel.json','w+',encoding='utf-8'))
    return hotelData

"""def loadCities(path='placeid.csv'):
    data = {}
    text = open(path,'r',encoding='utf-8').read()
    lines = text.split('\n')
    lines.pop(0)
    for line in lines:
        line = line.replace(' ','')
        line = line.lower()
        dats = line.split(',')
        name = dats[0][1:-1]
        id = dats[1][1:-1]
        domestic = dats[2][1:-1]
        data[name] = {'id' : id, 'domestic': domestic}
    with open('cities.json','w+',encoding='utf-8') as f:
        json.dump(data,f)

loadCities()"""