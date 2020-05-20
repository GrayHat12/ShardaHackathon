import filter
from geotext import GeoText
import main
import main2

def flight(line=[]):
    strline = ''
    for l in line:
        strline+=l+' '
    src = ''
    dest = ''
    if 'from' in line:
        tmp = line[line.index('from'):]
        placei = main2.getPlaces(tmp)
        if len(placei)==0:
            print('No Source')
        else : 
            src = placei[0]
            print(placei)
    if 'to' in line:
        tmp = line[line.index('to'):]
        placef = main2.getPlaces(tmp)
        if len(placef)==0:
            print('No Dest')
        else : 
            dest = placei[0]
            print(placef)
    
    '''['mode of transport', 'from', 'to' 'date' 'month']'''


def place():
    dat = []
    str1 = ""
    print(new_sentences)
    for i in new_sentences:
        for ele in i:
            str1 += " " + ele
    str1 = str1.upper()
    print(str1)
    places = GeoText(str1)
    dat.append(places.cities)
    print(dat)


def hotel():
    dat = []
    if 'book' in new_sentences:
        a = ['book', 'hotel']
        dat = dat + a
    else:
        b = ['find', 'hotel']
        dat = dat + b

    str1 = ""
    for ele in new_sentences:
        str1 += ele
        nlp = spacy.load('en_core_web_lg')
        doc = nlp(str1)
    for ent in doc.ents:
        dat.append(ent)

    month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'november',
             'december']

    for i in range(0, size):
        for j in range(0, num):
            if new_sentences[i][j] == 'room' and new_sentences[i][j - 1].isnumeric():
                dat.append(new_sentences[i][j - 1])

    for i in range(0, size):
        for j in range(0, num):
            if new_sentences[i][j] in month:
                dat.append(new_sentences[i][j])

    print(dat)
