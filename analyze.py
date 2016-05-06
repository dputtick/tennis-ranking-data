import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime as dt
import pandas

proj_dir = '/Users/dputtic/Documents/projects/tennis_data/'


# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.axis([0, 5, 0, 20])
# plt.savefig('/Users/dputtic/Documents/projects/tennis_data/plot.pdf', format='pdf')
# nadal = list()

# with open('all_data.csv') as csvfile:
# 	csvreader = csv.reader(csvfile, delimiter=',')
# 	count = 0
# 	for row in csvreader:
# 		if row[2] == 'Rafael Nadal':
# 			nadal.append((row[1], row[0], row[3]))

# dates = []
# ranks = []

# for date in nadal:
# 	format_date = dt.datetime.strptime(date[0], '%Y-%m-%d')
# 	dates.append(format_date)
# 	ranks.append(date[1])

df = pandas.read_csv('all_data.csv', parse_dates=['date'], index_col='date')
df2 = df.loc[df['name'] == 'Rafael Nadal']
ax = df2['points'].plot()
fig = ax.get_figure()
fig.savefig('plot2.pdf', format='pdf')



#plt.plot_date(dates, ranks, xdate=True, ydate=False)
#plt.savefig('/Users/dputtic/Documents/projects/tennis_data/plot.pdf', format='pdf')
