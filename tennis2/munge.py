import csv

input_filename = 'data.csv'
output_file = 'munged_data.csv'

input_file = open(input_filename, 'r', newline='')
output_file = open(output_file, 'w', newline='')

reader = csv.reader(input_file, delimiter=',')
writer = csv.writer(output_file, delimiter=',')

for i, line in enumerate(reader):
	print(line[0], end='\r')
	if i == 0:
		writer.writerow(line)
	else:
		if len(line) == 7:
			line.insert(3, 'None')
			writer.writerow(line)
		else:
			writer.writerow(line)



# open the csv file
# read it line by line
# check each line for length, add age = "None" if too short
# check each line for date that's too old, if it is, don't save the line to the new file
# otherwise, save the line to the new file