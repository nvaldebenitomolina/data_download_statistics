 #!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import datetime

#Reading dataframe
df = pd.read_csv("wordpress.csv", sep=',', encoding='utf-8') 
date   		= df['date']
dateparsed 	= df['dateparsed']
category  	= df['category']
datetime2=[]

def month(month):
	if month == 'ene':
		return '01'
	elif month == 'feb':
		return '02'
	elif month == 'mar':
		return '03'
	elif month == 'abr':
		return '04'
	elif month == 'may':
		return '05'
	elif month == 'jun':
		return '06'
	elif month == 'jul':
		return '07'
	elif month == 'ago':
		return '08'
	elif month == 'sept':
		return '09'
	elif month == 'oct':
		return '10'
	elif month == 'nov':
		return '11'
	elif month == 'dic':
		return '12'


for n in range(0,len(category)):
	if str(dateparsed[n]) != 'nan' :
		datetime2.append(dateparsed[n][0]+dateparsed[n][1]+dateparsed[n][2]+dateparsed[n][3]+'-'+dateparsed[n][5]+dateparsed[n][6]+'-'+dateparsed[n][8]+dateparsed[n][9])
		print(n)
	else:
		#print(dateparsed[n])
		# if date[n].startswith('Fri, 24 mar'):
		# 	print(n)
		# 	print(date[n])
		# 	datetime2.append('bad date')
		# else:
		print(n)
		datestr=date[n].split(' ')
		print(int(datestr[3]), int(month(datestr[2])), int(datestr[1]))
		x = datetime.datetime(int(datestr[3]),int(month(datestr[2])), int(datestr[1]))
		print(x.strftime("%Y-%m-%d"))
		datetime2.append(x.strftime("%Y-%m-%d"))


print(len(category))
print(len(datetime2))

df['date plot'] = datetime2
df.to_csv(str("wordpress_date.csv"), sep=',', encoding='utf-8', index=False)


#print(datetime)
#print(len(datetime))

#x = datetime.datetime(2018, 9, 15)
#print(x.strftime("%m-%d-%Y %H:%M:%S"))
#result = text.endswith('+00:00') 
#print (result)
