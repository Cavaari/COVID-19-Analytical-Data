import sys
import csv
#import pandas as pd



def main(argv):
	selected_year = argv[1]
	outFile = argv[2]
	try:
		#Opening the file 
		file = open('death_registrations_in_ontario_by_residence_1980-2020.csv', encoding="utf-8-sig")
		data = csv.reader(file)
	except:
		print("File Not Found")
		sys.exit(1)
	
	print(data)
	temp = ""
	count = 0
	outputm = []
	outputd = []
	output = []
	output2 = []
	
	#assigning each column a variable
	for row_data_fields in data:
		year = row_data_fields[0]
		month = row_data_fields[1]
		deaths = row_data_fields[3]

		#using an if statement and a temp variable for year/month 

		if(year != selected_year):
			continue

		if temp == month:
			count += int(deaths)
		else:
			outputd.append(count)
			outputm.append(month)
			temp = month
			count = 0
	

	outputd.append(count)
	outputd.pop(0)

	#outputing the simplied file with year,month and total deaths per month
	#in order sequentially

	i = 0
	for line in outputm:
		output.append(line + ',' + str(outputd[i]))
		i += 1

	output2.append("Month,Total Deaths")
	output2.append(output[4])
	output2.append(output[3])
	output2.append(output[7])
	output2.append(output[0])
	output2.append(output[8])
	output2.append(output[6])
	output2.append(output[5])
	output2.append(output[1])
	output2.append(output[11])
	output2.append(output[10])
	output2.append(output[9])
	output2.append(output[2])

	fp = open(outFile, 'w')

	for line in output2:
		fp.write(line + '\n')


	fp.close

main(sys.argv)	