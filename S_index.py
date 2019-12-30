from matplotlib.pyplot import *
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

import datetime

path = "/home/fabricio/Downloads/"
file_name = "Dsex.csv"

full_path = path + file_name

sindex_text = open(full_path).readlines()
initial_date = datetime.datetime(year=1, month=1, day=1)
date_list, initial_s_list, max_s_list, min_s_list, final_s_list, other_list = [], [], [], [], [], []
ohlc = []
for line in sindex_text:
    _, date, initial_s, max_s, min_s, final_s, other = line.split(",")
    date_list.append(datetime.datetime.strptime(date, "%m/%d/%Y"))
    days_diff = date_list[-1] - initial_date
    ohlc.append((days_diff.days, float(initial_s), float(max_s), float(min_s), float(final_s)))

ax1 = subplot2grid((1,1), (0,0))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
candlestick_ohlc(ax1, ohlc, colorup="#00FF00")
show()
