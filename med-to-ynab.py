#Converts mediolanum csv to ynab csv
#Usage: python3 med-to-ynab.py infile.csv outfile.csv

import sys, io
import csv
from datetime import datetime

start = False
with io.open(sys.argv[1], encoding='latin-1') as i, open(sys.argv[2], 'w') as o:

	#Output header
	o.write("Date,Payee,Category,Memo,Outflow,Inflow\n");

	csvreader = csv.reader(i, delimiter=",",quotechar='"')

	for line in csvreader:
		if start:
			if line[0] == "":
				continue
			fields_in = line
			date = datetime.strptime(fields_in[0], "%d-%m-%y")
			fields_out = [date.strftime("%m-%d-%Y")] #Date
			#Payee will be first two words of "concept"
			payee = '"' + fields_in[1] + '"'
			fields_out.append(payee)

			fields_out.append('') #Empty category

			fields_out.append('"' + fields_in[1] + '"') #Concept as memo

			fields_out.append(fields_in[3].replace(',','.')) #Outflow

			fields_out.append(fields_in[4].replace(',','.')) #Inflow

			#Write
			o.write(','.join(fields_out) + '\n')
		elif line[0][0] == 'F': #First line starts with "Fecha..."
			start = True


			
