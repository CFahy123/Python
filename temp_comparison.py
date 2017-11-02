import csv
from matplotlib import pyplot as plt
from datetime import datetime

def get_data(filename,highs,lows,dates):
    '''Take a file and pull the highs,lows,and dates'''
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                high = int(row[1])
                low = int(row[3])
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
            except ValueError:
                print(current_date,'missing data')
            else:
                lows.append(low)
                highs.append(high)
                dates.append(current_date)

#get the death_valley_2014 data
highs,lows,dates = [],[],[]
get_data('death_valley_2014.csv',highs,lows,dates)


fig = plt.figure(dpi=128, figsize=(10, 6))

#plot death_valley_2014
plt.plot(dates,lows,c='blue',alpha = 0.3)
plt.plot(dates,highs,c='red',alpha = 0.3)
plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha = 0.15)


# get the sitka data
highs,lows,dates = [],[],[]
get_data('sitka_weather_2014.csv',highs,lows,dates)

#plot the sitka data
plt.plot(dates,lows,c='blue',alpha = 0.6)
plt.plot(dates,highs,c='red',alpha = 0.6)
plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha = 0.5)


# Format plot.
title = "Daily high and low temperatures - 2014"
title += "\nSitka, AK and Death Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 120)

plt.show()
