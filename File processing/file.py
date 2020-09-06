import time
import os
import pandas

while True:
    if os.path.exists('files/temps.csv'):
        data = pandas.read_csv('files/temps.csv')
        print(data.mean()['st1'])
    else:
        print('file doesnt exist')
    time.sleep(2)
