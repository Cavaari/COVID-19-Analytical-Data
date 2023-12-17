#!/usr/bin/env python
import sys
import csv
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt



def main(argv):
	
	if len(argv) != 3:
		print("Usage:",
			"deaths_compared.py <year to print>  <graphics file>")
		sys.exit(-1)

	inFile = argv[1]
	graphic_filename = argv[2]
	
	
	'''try:
		csv_df = pd.read_csv(inFile, encoding="utf-8-sig")
			
	except IOError as err:
		print("Unable to open source file", 'death_registrations_in_ontario_by_residence_1980-2020.csv',
						": {}".format(err), file=sys.stderr)
		sys.exit(-1)'''
	
	'''output = []

	output = trimYear(inFile, year)
	#for line in output:
	#	print(line)


	tempFile = open("tempFile.csv", 'w')
	for line in output:
		tempFile.write(line + '\n')
	tempFile.close'''

	csv_df = pd.read_csv(inFile, delimiter=',')
	fig = plt.figure()
	print(csv_df)
	sns.barplot(data = csv_df, x = csv_df.columns[0], y = csv_df.columns[1])


	fig.savefig(graphic_filename, bbox_inches="tight")

	plt.show()				

main(sys.argv)