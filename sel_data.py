import filter
import mode


def entity(text=""):
    new_sentences = filter.filt(text)
    print(new_sentences)
    for i in new_sentences:
        if 'flight' in i:
            mode.flight(i)
            break
        elif 'places' or 'place' and 'near' in i:
            mode.place()
            break
        elif 'hotel' or 'hotels' in i:
            mode.hotel()
            break
