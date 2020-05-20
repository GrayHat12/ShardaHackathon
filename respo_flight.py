import mode
info = mode.flight()
if info[2] is None:
    print("where do you wanna book your flight to")
    info[2] = input()
if info[3] is None:
    print("when do you wanna book your flight")
    info[3] = input()
    '''['mode of transport', 'from', 'to' 'date' 'month']'''
print(info)