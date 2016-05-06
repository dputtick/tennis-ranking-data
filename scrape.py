import urllib.request
from html.parser import HTMLParser
import re
import os

class myHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self) #call the parent init
		self.data = []

	def handle_data(self, data):
		if re.match(r"\d", data) != None:
			self.data.append(data)

def build_url(date):
	return 'http://www.stevegtennis.com/men-atp-rankings/' + date + '/1/all/'

def get_dates(filename):
	page = open(('/Users/dputtic/Documents/projects/tennis_data/raw_pages/'
					+ filename), 'r').read()
	start = page.find('<td>Select Date: <select name="date" id="date">')
	stop = page.find('</select>', start)
	parser = myHTMLParser()
	parser.feed(page[start:stop])
	return parser.data


def get_page(url, filename):
	data_to = open(('/Users/dputtic/Documents/projects/tennis_data/raw_pages/'
					+ filename), 'w')
	page = urllib.request.urlopen(url)
	html = page.read().decode()
	data_to.write(html)


if __name__ == '__main__':
	raw_pages_path = '/Users/dputtic/Documents/projects/tennis_data/raw_pages/'
	start_date = '2016-03-07'
	start_date_url = build_url(start_date)
	filename = start_date + '.html'
	get_page(start_date_url, filename)
	all_dates = get_dates(filename)
	for item in all_dates:
		if os.path.exists(raw_pages_path + item + '.html') == False:
			filename = item + '.html'
			date_url = build_url(item)
			get_page(date_url, filename)

