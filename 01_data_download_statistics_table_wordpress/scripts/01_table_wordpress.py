
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import os
import xlrd
from openpyxl import load_workbook
from datetime import datetime

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get("http://www.cr2.cl/wp-admin/edit.php?post_type=wpdmpro&page=wpdm-stats&type=pvdpu")

enter = driver.find_element_by_id('user_login')
enter.send_keys(os.environ["USER_WORDPRESS"])

enter = driver.find_element_by_id('user_pass')
enter.send_keys(os.environ["PASSWORDWORDPRESS"])

enter = driver.find_element_by_id("wp-submit")
enter.click()

def writevariable(selectname):
	select = Select(driver.find_element_by_name(selectname))
	selected_option = select.first_selected_option
	value=selected_option.text
	return value



def createtable():
	data=[]
	header =[]
	driver.maximize_window()

	for tr in driver.find_elements_by_xpath('//table[@class="table table-bordered table-hover"]//tr'):
	    
	    ths = tr.find_elements_by_tag_name('th')

	    tds = tr.find_elements_by_tag_name('td')
	    if ths:
	    	header.append([th.text for th in ths])

	table = driver.find_element_by_css_selector("[class='table table-bordered table-hover']")
	print(table)
	for row in table.find_elements_by_css_selector('tr'):
		data.append([int(d.text) for d in row.find_elements_by_css_selector('td')])

	return header,data


def numbertomonth(number):
	if number == "1":
		return "enero"
	elif number == "2":
		return "febrero"
	elif number == "3":
		return "marzo"
	elif number == "4":
		return "abril"
	elif number == "5":
		return "mayo"
	elif number == "6":
		return "junio"
	elif number == "7":
		return "julio"
	elif number == "8":
		return "agosto"
	elif number == "9":
		return "septiembre"
	elif number == "10":
		return "octubre"
	elif number == "11":
		return "noviembre"
	elif number == "12":
		return "diciembre"

def savetable(data,month,table_name):
		
		if len(data) == 0:
			print("It's not possible save sheet: "+numbertomonth(month)+", year :"+writevariable('y')+" because data = null ")
		else:
			
			df= pd.DataFrame(data)
			d = datetime.now() #today's datetime
			print(d.strftime("%Y-%m-%d"))
			if os.path.isfile('../output/'+str(table_name)+"_"+d.strftime("%Y-%m-%d")+".xlsx"):
				book = load_workbook("../output/"+str(table_name)+"_"+d.strftime("%Y-%m-%d")+".xlsx")
				writer = pd.ExcelWriter("../output/"+str(table_name)+"_"+d.strftime("%Y-%m-%d")+".xlsx", engine='openpyxl') 
				writer.book = book
				writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

				df.to_excel(writer, sheet_name=numbertomonth(month))

				writer.save()

				# with pd.ExcelWriter(str(table_name)+".xlsx", mode='a') as writer:
				#     df.to_excel(writer, sheet_name=numbertomonth(month), index=False)
				#     writer.save()
				print('table '+table_name+'_'+d.strftime("%Y-%m-%d")+' changed')
				# Close the Pandas Excel writer and output the Excel file.
				
			else: 
				df.to_excel("../output/"+str(table_name)+"_"+d.strftime("%Y-%m-%d")+".xlsx",sheet_name=numbertomonth(month))
				print('table '+table_name+'_'+d.strftime("%Y-%m-%d")+'.xlsx created')
				# Close the Pandas Excel writer and output the Excel file.
			

def tablebyyear(year):
	for n in range(1,13):
		driver.find_element_by_xpath("//select[@name='y']/option[text()='"+str(year)+"']").click()
		driver.find_element_by_xpath("//select[@name='m']/option[text()='"+str(n)+"']").click()
		driver.find_element_by_xpath("//input[@type='submit']").click()
	

		savetable(createtable()[1],writevariable('m'),writevariable('y')+'-forms')

#tablebyyear(2015)
#tablebyyear(2016)
#tablebyyear(2017)
tablebyyear(2018)
tablebyyear(2019)
tablebyyear(2020)
