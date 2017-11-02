import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
   reader = csv.reader(f)
   header_row = next(reader)
   print(header_row)

   for index, column_header in enumerate(header_row):
       print(index,column_header)

   # get the high temps from the file
   dates, highs, lows = [],[],[]
   for row in reader:
       current_date = datetime.strptime(row[0],"%Y-%m-%d")
       dates.append(current_date)

       high = int(row[1])
       highs.append(high)

       low = int(row[3])
       lows.append(lows)

   print(highs)

   # Plot data.
   fig = plt.figure(dpi=128, figsize=(8, 4))
   plt.plot(dates,highs, c='red')
   plt.plot(dates,lows, c='blue')


   # Format plot
   plt.title("Daily high temperatures July 2014", fontsize = 24)
   plt.xlabel("",fontsize = 16)

   fig.autofmt_xdate()
   plt.ylabel("Tempeture (F)", fontsize = 16)
   plt.tick_params(axis='both', which='major', labelsize=16)
   plt.show()
