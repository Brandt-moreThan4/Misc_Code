import csv
import sys
import matplotlib.pyplot as plt
from datetime import datetime
from os import path

filename = 'data\\sitka_weather_tt2018_simple.csv'
if path.exists(filename):
    print('file exists!')
else:
    print('file not found. going to quit now')
    sys.exit()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    highs,dates,lows = [],[],[]
    for row in reader:
        high = int(row[5])
        low = int(row[6])
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

plt.style.use('seaborn')


fig, ax = plt.subplots(figsize=(12,8))
ax.plot(dates,highs,c='red',alpha=.5,label='highs')
ax.plot(dates,lows,c='blue',alpha=.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=.1)
ax.set_title('Daily high temps for 2018',fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temp (F)', fontsize = 16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()