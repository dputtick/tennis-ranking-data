import re
import csv
import os


def get_player_index(data_slice, start_index, search_string='/profile-bio/men/'):
	i = data_slice.find(search_string, start_index)
	return i

def get_player(page_slice):
	match = re.search(r">([–\w\s-]+)<.*?(\d+)<", page_slice)
	return match.groups()

def get_player_data(player_data_slice, date):
	full_player_list = []
	index = 0
	for number in range(300):
		i1 = get_player_index(player_data_slice, index) #these first few lines can all be HTML parser
		i2 = get_player_index(player_data_slice, i1 + 1)
		individual_player_slice = player_data_slice[i1:i2]
		player_data_tuple = get_player(individual_player_slice)
		player_data_list = list(player_data_tuple)
		player_data_list.insert(0, number + 1)
		player_data_list.insert(1, date)
		full_player_list.append(player_data_list)
		index = i2
	return full_player_list
		

if __name__ == '__main__':
	project_path = '/Users/dputtic/Documents/projects/tennis_data/'
	files = os.listdir(project_path + 'raw_pages/')
	csv_path = project_path + 'all_data.csv'
	with open(csv_path, 'w', newline='') as csvfile:
		csv_writer = csv.writer(csvfile, delimiter=',')
		csv_writer.writerow(['rank', 'date', 'name', 'points'])
	for filename in files[1:]:
		file_path =  project_path + 'raw_pages/' + filename #build file path
		with open(file_path, 'r') as data: #open html file
			data = data.read()
		begin = data.find("id='matchs_info") #find start of player data section
		end = data.find('<table width="600" border="0"', begin) #end of 
		player_data_slice = data[begin:end] #slice out all player data
		date = filename[:-5]
		try:
			player_data_list = get_player_data(player_data_slice, date)
		except AttributeError:
			continue
		with open(csv_path, 'a', newline='') as csvfile:
			csv_writer = csv.writer(csvfile, delimiter=',')
			csv_writer.writerows(player_data_list)




# What does setting newline and delimiter do
	# newline should always be '' for csv files.
# What do I do when I have some bad data? What's a good practice to catch it?
	# pass does nothing, break stops the whole loop, continue goes to next iteration
# Is it a bad habit to import whole modules?
	# dir() shows whole namespace. globals() locals() builtins() namespaces
# Should I make this more functional? How should I structure the program?
	# best idea is to think in modularity. Code that can be reused

# Ideas for the future:
# Switch from using Regex to HTMLParser to parse player data
# Switch from using urllib to requests library
# Upload project to github
# Take some basic means (mean age to break into top 100).
	# This involves tracking individual players over time, and knowing their age
# Check for duplicate names or issues like that.
# Potential directions for the future:
	# Present data in a web page with a GUI of some sort
	# Learn how to make charts using matplotlib
	# Figure out how to store the date in a SQLite database or pandas dataframe
	# Find a source for specific match data and scrape it -> match fixing
	# Try to link match data with rankings data, maybe make it predictive
	# Try to predict match outcomes and get them close to betting lines


# look through builtins and keywords for stuff I know and don't know