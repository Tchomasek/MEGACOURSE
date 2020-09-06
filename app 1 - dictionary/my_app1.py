import json
import difflib
from difflib import SequenceMatcher, get_close_matches

data = json.load(open('extract/data.json'))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(),  n=1, cutoff=0.8)) > 0:
        match = get_close_matches(w, data.keys(),  n=1, cutoff=0.8)[0]
        print('did you mean "{}"?'.format(match))
        while True:
            decision = input('"y" for YES, "n" for NO: ')
            if decision == 'y':
                return data[match]
            elif decision == 'n':
                return "no entry found"
            else:
                print('you must enter "y" or "n"')
    else:
        return "no entry found"

def display(word):
    result = translate(word)
    if type(result) == list:
        for sentence in result:
            print()
            print(sentence)

    else:
        print('no entry found')

word = input("enter word: ")

display(word)
