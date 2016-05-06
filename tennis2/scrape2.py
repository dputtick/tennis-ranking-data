import requests
import csv
from lxml import html


def page_getter(url, date=None):
	payload = {'rankDate': date, 'rankRange': '1-5000'}
	if date == None:
		payload['rankRange'] = None
	page = requests.get(url, params=payload)
	return html.fromstring(page.content)
	
def date_parser(page):
	date_table = page.xpath('//ul[@data-value="rankDate"]/*')
	date_list = list()
	for date_entry in date_table[1:]:
		attributes = date_entry.attrib
		# print(attributes)
		date = attributes['data-value']
		date_list.append(date)
	return date_list

def tablehead_getter(page):
	'''Select thead from table and pull out table headers'''

	rankings_table = page.get_element_by_id("singlesRanking")
	thead = rankings_table.xpath("div/table/thead//div[@class='sorting-label']/text()") 
	header = [e.strip() for e in thead if e.strip() not in ['Move', 'Country']]
	header.insert(0, 'Date')
	return header

def players_getter(page, date):
	'''Select table body and return list of all players'''

	rankings_table = page.get_element_by_id("singlesRanking")
	tbody = rankings_table.xpath("div/table/tbody") # select the tbody
	players = tbody[0].xpath("tr") # select a list of all players
	player_table = list() # list for player data to be appended to
	for player in players:
		rank = player.xpath('td[@class="rank-cell"]//text()')
		player_info = player.xpath('td[position()>3]//text()')
		player_info = [x.strip() for x in player_info if x.strip()]
		if len(player_info) == 5:
			player_info.insert(1, 'None')
		player_info.insert(0, rank[0].strip()) # add rank to beginning of list
		player_info.insert(0, date) # add date to beginning of list
		player_info[4] = player_info[4].replace(',', '') # removing commas
		player_info[6] = player_info[6].replace(',', '') # from numbers
		player_info[1] = player_info[1].strip('T')
		player_table.append(player_info)
	return player_table

def main():
	# input parameters:
	base_url = 'http://www.atpworldtour.com/en/rankings/singles'
	startdate, enddate = '2016-03-21', '1996-08-12' # format is 'YYYY-MM-DD'
	output_filename = 'data2.csv'

	base_page = page_getter(base_url)
	list_of_dates = date_parser(base_page)
	if (startdate, enddate) != ('', ''):
		begin = list_of_dates.index(startdate)
		end = list_of_dates.index(enddate) + 1
	else:
		begin, end = '', ''
	print('Start on {}, end on {}.'.format(startdate, enddate))
	with open(output_filename, 'w', newline='') as csvfile:
		csv_writer = csv.writer(csvfile, delimiter=',')
		header = tablehead_getter(base_page)
		csv_writer.writerow(header)
	for date in list_of_dates[begin:end]:
		page = page_getter(base_url, date)
		players_table = players_getter(page, date)
		with open(output_filename, 'a', newline='') as csvfile:
			csv_writer = csv.writer(csvfile, delimiter=',')
			csv_writer.writerows(players_table)
		print('{} completed'.format(date), end='\r')


if __name__ == '__main__':
	main()


# Earliest available date is 1996-08-12


# I want to organize this to be a modular and effective as possible
# Control flow:
	# Call a requests function that takes a date and returns the page
	# Run a function on the base page that returns a list of all possible dates
	# Use CSVwriter to generate a csv file in append mode
	# Use the get_thead function to populate the headers for the csv table
	# For each date, call the requests function to return a page
	# Then call a function that uses lxml to return a table of all players
	# Write that table to the csv file




# First, I'm going to query and download the web page using Requests.

# Then, I'll have to figure out how to traverse the various dates, using Requests.

# Once I have a shit ton of html pages as files,
# I'll have to use HTMLparser to analyze them and pull out the data I want,
# and send it to a great big csv file.

# Then, I'll have to put the csv in a pandas dataframe, and maybe save it that way?

# what's the spec:
# I'm curious how long it takes the average player to break into the top 100
# Anything in the rankings predicts whether a player will make it into the top XX
# Ranking, change, name, age, points, tourn played, next best 