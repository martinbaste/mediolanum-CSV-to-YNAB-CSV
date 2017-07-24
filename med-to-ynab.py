#Converts mediolanum csv to ynab csv
#Usage: python3 med-to-ynab.py infile.csv outfile.csv

import sys

start = False
with open(sys.argv[1], 'r') as i, open(sys.argv[2], 'w') as o:

	#Output header
	o.write("Date,Payee,Category,Memo,Outflow,Inflow\n");

	for line in i:
		if start: 
			line = line.strip()
			fields_in = line.split(';')

			fields_out = [fields_in[0]] #Date
			#Payee will be first two words of "concept"
			payee = '"' + ' '.join(fields_in[1].split(' ')[:2]) + '"'
			fields_out.append(payee)

			fields_out.append('') #Empty category

			fields_out.append('"' + fields_in[1] + '"') #Concept as memo

			fields_out.append(fields_in[3].replace(',','.')) #Outflow

			fields_out.append(fields_in[4].replace(',','.')) #Inflow

			#Write
			o.write(','.join(fields_out) + '\n')
		elif line[0] == 'F': #First line starts with "Fecha..."
			start = True


			
