#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import time
import imaplib
import email
import pandas as pd
import os


FROM_EMAIL  = os.environ['EMAIL']
FROM_PWD    = os.environ['FROM_PWD']
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL,FROM_PWD)
mail.select('inbox')

type, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()


first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])

print(first_email_id)
print(latest_email_id)
#def readmail():
    # mail reading logic will come here !!

date_glo=[];date_reg=[];date_cr2met=[];date_chirps=[];date_precip=[];date_tasmaxmin=[];date_caudal=[];

def getbodyglob(message): #getting plain text 'email body'
    body = None

    if message['subject'] == "Uso de archivos simulaciones globales" or message['subject'] == "Fwd: Uso de archivos simulaciones globales":
	    if message.is_multipart():
	        for part in message.walk():
	            if part.is_multipart():
	                for subpart in part.walk():
	                    if subpart.get_content_type() == 'text/plain':
	                        body = subpart.get_payload(decode=True)
	            elif part.get_content_type() == 'text/plain':
	                body = part.get_payload(decode=True)
	    elif message.get_content_type() == 'text/plain':
	        body = message.get_payload(decode=True)
	    return body

def getbodyreg(message):
	body = None
	if message['subject'] == "Uso de archivos simulaciones regionales" or message['subject'] == "Fwd: Uso de archivos simulaciones regionales" :
		if message.is_multipart():
			for part in message.walk():
				if part.is_multipart():
					for subpart in part.walk():
						if subpart.get_content_type() == 'text/plain':
							body = subpart.get_payload(decode=True)
						elif part.get_content_type() == 'text/plain':
							body = part.get_payload(decode=True)
		elif message.get_content_type() == 'text/plain':
			body = message.get_payload(decode=True)
		return body

def getbodycr2met(message):
	body = None
	if message['subject'] == "Uso de archivos CR2MET" or message['subject'] == "Fwd: Uso de archivos CR2MET" :
		if message.is_multipart():
			for part in message.walk():
				if part.is_multipart():
					for subpart in part.walk():
						if subpart.get_content_type() == 'text/plain':
							body = subpart.get_payload(decode=True)
						elif part.get_content_type() == 'text/plain':
							body = part.get_payload(decode=True)
		elif message.get_content_type() == 'text/plain':
			body = message.get_payload(decode=True)
		return body
def getbodychirps(message):
	body = None
	if message['subject'] == "Uso de archivos datos CHIRPS" or message['subject'] == "Fwd: Uso de archivos datos CHIRPS" or message['subject'] == "Fwd: Uso de archivos datos CHIRPS, upd Si" or message['subject'] == "Fwd: Uso de archivos datos CHIRPS, upd No" :
		if message.is_multipart():
			for part in message.walk():
				if part.is_multipart():
					for subpart in part.walk():
						if subpart.get_content_type() == 'text/plain':
							body = subpart.get_payload(decode=True)
						elif part.get_content_type() == 'text/plain':
							body = part.get_payload(decode=True)
		elif message.get_content_type() == 'text/plain':
			body = message.get_payload(decode=True)
		return body

def getbodytasmaxmin(message):
	body = None
	if message['subject'] == "Uso de archivos datos tasmaxmin" or message['subject'] == "Fwd: Uso de archivos datos tasmaxmin":
		if message.is_multipart():
			for part in message.walk():
				if part.is_multipart():
					for subpart in part.walk():
						if subpart.get_content_type() == 'text/plain':
							body = subpart.get_payload(decode=True)
						elif part.get_content_type() == 'text/plain':
							body = part.get_payload(decode=True)
		elif message.get_content_type() == 'text/plain':
			body = message.get_payload(decode=True)
		return body

def getbodyprecip(message):
	body = None
	if message['subject'] == "Uso de archivos datos precip" or message['subject'] == "Fwd: Uso de archivos datos precip":
		if message.is_multipart():
			for part in message.walk():
				if part.is_multipart():
					for subpart in part.walk():
						if subpart.get_content_type() == 'text/plain':
							body = subpart.get_payload(decode=True)
						elif part.get_content_type() == 'text/plain':
							body = part.get_payload(decode=True)
		elif message.get_content_type() == 'text/plain':
			body = message.get_payload(decode=True)
		return body

def getbodycaudal(message):
	body = None
	if message['subject'] == "Fwd: Uso de archivos datos caudal, upd No" or message['subject'] == "Fwd: Uso de archivos datos caudal, upd Si":
		if message.is_multipart():
			for part in message.walk():
				if part.is_multipart():
					for subpart in part.walk():
						if subpart.get_content_type() == 'text/plain':
							body = subpart.get_payload(decode=True)
						elif part.get_content_type() == 'text/plain':
							body = part.get_payload(decode=True)
		elif message.get_content_type() == 'text/plain':
			body = message.get_payload(decode=True)
		return body

def getbodytasmean(message):
	body = None
	if message['subject'] == "Fwd: Uso de archivos datos tasmean, upd No" or message['subject'] == "Fwd: Uso de archivos datos tasmean, upd Si":
		if message.is_multipart():
			for part in message.walk():
				if part.is_multipart():
					for subpart in part.walk():
						if subpart.get_content_type() == 'text/plain':
							body = subpart.get_payload(decode=True)
						elif part.get_content_type() == 'text/plain':
							body = part.get_payload(decode=True)
		elif message.get_content_type() == 'text/plain':
			body = message.get_payload(decode=True)
		return body
messages_global=[]
messages_regional=[]	
messages_cr2met=[]
messages_chirps=[]
messages_tasmaxmin=[]
messages_precip=[]
messages_caudal=[]
messages_tasmean=[]

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in reversed(range(first_email_id+13000,latest_email_id)):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    #email_subject = msg['subject']
                    #email_from = msg['from']
                    #email_message = msg['message-id']
                    mes_global = getbodyglob(msg)
                    mes_regional = getbodyreg(msg)
                    mes_cr2met = getbodycr2met(msg)
                    mes_chirps = getbodychirps(msg)
                    mes_tasmaxmin = getbodytasmaxmin(msg)
                    mes_precip = getbodyprecip(msg)
                    mes_caudal = getbodycaudal(msg)
                    mes_tasmean = getbodytasmean(msg)

                    if mes_regional is not None:
                   		print mes_regional
                   		messages_regional.append(mes_regional)
                   		#date_reg.append(msg['date'])
                    if mes_global is not None:
                    	print mes_global
                    	messages_global.append(mes_global)
                    	#date_glo.append(msg['date'])
                    if mes_cr2met is not None:
                    	print mes_cr2met
                    	messages_cr2met.append(mes_cr2met)
                    	#date_cr2met.append(msg['date'])
                    if mes_chirps is not None:
                    	print mes_chirps
                    	messages_chirps.append(mes_chirps)
                    	#date_chirps.append(msg['date'])
                    if mes_tasmaxmin is not None:
                    	print mes_tasmaxmin
                    	messages_tasmaxmin.append(mes_tasmaxmin)
                    if mes_precip is not None:
                    	print mes_precip
                    	messages_precip.append(mes_precip)
                    if mes_caudal is not None:
                    	print mes_caudal
                    	messages_caudal.append(mes_caudal)
                    if mes_tasmean is not None:
                    	print mes_tasmean
                    	messages_tasmean.append(mes_tasmean)


                   
	
    except Exception, e:
        print str(e)



read_email_from_gmail()

name1=[]; name2=[];name3=[]; name4=[];name5=[]; name6=[];name7=[];name8=[]
email1=[]; email2=[];email3=[]; email4=[];email5=[]; email6=[];email7=[];email8=[]
asunto1=[]; asunto2=[];asunto3=[]; asunto4=[];asunto5=[]; asunto6=[];asunto7=[];asunto8=[]
mensaje1=[]; mensaje2=[];mensaje3=[]; mensaje4=[];mensaje5=[]; mensaje6=[];mensaje7=[];mensaje8=[]
date1=[]; date2=[];date3=[]; date4=[];date5=[]; date6=[]; date7=[]; date8=[]
dateparsed1=[]; dateparsed2=[];dateparsed3=[]; dateparsed4=[];dateparsed5=[]; dateparsed6=[]; dateparsed7=[]; dateparsed8=[]
subject1=[]; subject2=[];subject3=[]; subject4=[];subject5=[]; subject6=[]; subject7=[]; subject8=[]

def monthstonumber(month):
	if month == "ene":
		return '01'
	elif month == "feb":
		return '02'
	elif month == "mar":
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

def split_between_more(string,one,two):
	date=string.split(one)
	date1=date[1].split(two)
	return date1[0]

def split_message_simulations(message,name,email,asunto,mensaje,date,dateparsed,subject):

	for n in range(0,len(message)):
		print('Split message')
		print(message[n])
		name.append(split_between_more(message[n], 'De:', ' <'))
		date.append(split_between_more(message[n], 'Date:', 'Subject:'))
		dateparsed.append((split_between_more(split_between_more(message[n], 'Date:', 'Subject:'),'. ', ' a las '))+'-'+
			monthstonumber((split_between_more(split_between_more(message[n], 'Date:', 'Subject:'),(split_between_more(split_between_more(message[n], 'Date:', 'Subject:'),'., ', ' ')+' '),'. ')))+'-'+
			(split_between_more(split_between_more(message[n], 'Date:', 'Subject:'),'., ', ' '))+' '+
			(split_between_more(message[n], 'Date:', 'Subject:').split('a las'))[1])
		subject.append(split_between_more(message[n],'Subject:', 'To:'))
		email.append(split_between_more(message[n], split_between_more(message[n], 'De:', ' <')+' <' , '>'))
		asunto.append(split_between_more(message[n], 'Asunto:', 'Cuerpo del mensaje:'))
		mensaje.append(split_between_more(message[n], 'Cuerpo del mensaje:', '--'))
		
def split_message_others(message,name,email,asunto,mensaje,date,dateparsed,subject):

	for n in range(0,len(message)):
		print('Split message')
		print(message[n])
		name.append(split_between_more(message[n], 'De:', ' <'))
		date.append(split_between_more(message[n], 'Date:', 'Subject:'))
		dateparsed.append((split_between_more(split_between_more(message[n], 'Date:', 'Subject:'),'. ', ' a las '))+'-'+
			monthstonumber((split_between_more(split_between_more(message[n], 'Date:', 'Subject:'),(split_between_more(split_between_more(message[n], 'Date:', 'Subject:'),'., ', ' ')+' '),'. ')))+'-'+
			(split_between_more(split_between_more(message[n], 'Date:', 'Subject:'),'., ', ' '))+' '+
			(split_between_more(message[n], 'Date:', 'Subject:').split('a las'))[1])
		subject.append(split_between_more(message[n], 'Subject:', 'To:'))
		email.append(split_between_more(message[n], split_between_more(message[n], 'De:', ' <')+' <' , '>'))
		print(message[n].find('Institucion'))
		if message[n].find('Institucion') is not -1 :
			asunto.append(split_between_more(message[n], 'Institucion:', 'Cuerpo del mensaje:'))
			mensaje.append(split_between_more(message[n], 'Cuerpo del mensaje:', 'Desea que le envíen email en caso de Actualización de Datos?'))
		if message[n].find('Asunto') is not -1:
			asunto.append(split_between_more(message[n], 'Asunto:', 'Cuerpo del mensaje:'))
			mensaje.append(split_between_more(message[n], 'Cuerpo del mensaje:', '--'))

split_message_simulations(messages_global,name1,email1,asunto1,mensaje1,date1,dateparsed1,subject1)
split_message_simulations(messages_regional,name2,email2,asunto2,mensaje2,date2,dateparsed2,subject2)
split_message_others(messages_cr2met,name3,email3,asunto3,mensaje3,date3,dateparsed3,subject3)
split_message_others(messages_chirps,name4,email4,asunto4,mensaje4,date4,dateparsed4,subject4)
split_message_others(messages_tasmaxmin,name5,email5,asunto5,mensaje5,date5,dateparsed5,subject5)
split_message_others(messages_precip,name6,email6,asunto6,mensaje6,date6,dateparsed6,subject6)
split_message_others(messages_caudal,name7,email7,asunto7,mensaje7,date7,dateparsed7,subject7)
split_message_others(messages_caudal,name8,email8,asunto8,mensaje8,date8,dateparsed8,subject8)

def create_table(name,email,institution,message,table_name,date,dateparsed,subject):
	df= pd.DataFrame({'Date': date, 'Date parsed': dateparsed,'Name':name, 'Email': email, 'Institution': institution, 'reason': message, 'Subject':subject, 'Category':table_name})
	#df= pd.DataFrame({'Date': date, 'Name':name, 'Email': email, 'Institution': institution, 'reason': message, 'Subject':subject, 'Category':table_name})

	#Create a new dataframe
	
	df.to_csv(str(table_name+".csv"), sep=',', encoding='utf-8')
	print('table '+table_name+'.csv created')

#create_table(name1,email1,asunto1,mensaje1,"simulaciones_globales",date1,dateparsed1,subject1)
create_table(name2,email2,asunto2,mensaje2,"simulaciones_regionales",date2,dateparsed2,subject2)
create_table(name3,email3,asunto3,mensaje3,"cr2met",date3,dateparsed3,subject3)
# create_table(name4,email4,asunto4,mensaje4,"chirps",date4,dateparsed4,subject4)
# create_table(name5,email5,asunto5,mensaje5,"tasmaxmin",date5,dateparsed5,subject5)
# create_table(name6,email6,asunto6,mensaje6,"precip",date6,dateparsed6,subject6)
# create_table(name7,email7,asunto7,mensaje7,"caudal",date7,dateparsed7,subject7)
# create_table(name8,email8,asunto8,mensaje8,"tasmean",date8,dateparsed8,subject8)

