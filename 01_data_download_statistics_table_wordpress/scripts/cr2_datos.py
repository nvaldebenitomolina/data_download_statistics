#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import time
import imaplib
import email
import pandas as pd
import os

ORG_EMAIL   = os.environ['ORG_EMAIL']
FROM_EMAIL  = os.environ['FROM_EMAIL'] + ORG_EMAIL
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

date_glo=[];date_reg=[];date_cr2met=[];date_chirps=[];
messages_glo=[];messages_reg=[];messages_cr2met=[];messages_chirps=[]
subject_glo=[];subject_reg=[];subject_cr2met=[];subject_chirps=[]

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
	if message['subject'] == "Uso de archivos datos CR2MET" or message['subject'] == "Fwd: Uso de archivos datos CR2MET" :
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


        for i in reversed(range(first_email_id+12000,latest_email_id)):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    #email_subject = msg['subject']
                    #email_from = msg['from']
                    #email_date = msg['date']
                    #email_message = msg['message-id']
                    mes_global = getbodyglob(msg)
                    mes_regional = getbodyreg(msg)
                    mes_cr2met = getbodycr2met(msg)
                    mes_chirps = getbodychirps(msg)
                    if mes_regional is not None:
                   		print mes_regional
                   		messages_reg.append(mes_regional)
                   		subject_reg = msg['subject']
                   		date_reg.append(msg['date'])
                    if mes_global is not None:
                    	print mes_global
                    	messages_glo.append(mes_regional)
                   		subject_glo = msg['subject']
                   		date_glo.append(msg['date'])
                    if mes_cr2met is not None:
                    	print mes_cr2met
                    	messages_cr2met.append(mes_cr2met)
                    	subject_cr2met = msg['subject']
                    	date_cr2met.append(msg['date'])
                    if mes_chirps is not None:
                    	print mes_chirps
                    	messages_chirps.append(mes_chirps)
                    	subject_chirps = msg['subject']
                    	date_chirps.append(msg['date'])

                   
	
    except Exception, e:
        print str(e)



read_email_from_gmail()

name1=[]; name2=[];name3=[]; name4=[];
email1=[]; email2=[];email3=[]; email4=[];
intitution1=[]; intitution2=[];intitution3=[]; intitution4=[]
city1=[];city2=[];city3=[];city4=[]
reason1=[]; reason2=[];reason3=[]; reason4=[]
refresh1=[];refresh2=[];refresh3=[];refresh4=[]

def split_between_more(string,one,two):
	date=string.split(one)
	date1=date[1].split(two)
	return date1[0]

		
def split_message(message,name,email,institution,city,reason,refresh):

	for n in range(0,len(message)):
		print('Split message')
		print(message[n])
		menssage.append(split_between_more(message[n], 'Cuerpo del reason:', 'Desea que le envíen email en caso de Actualización de Datos?'))
		name.append(split_between_more(message[n], 'De:', ' <'))
		email.append(split_between_more(message[n], '<', '>'))
		institution.append(split_between_more(message[n], 'Institucion:', 'Ciudad:'))
		city.append(split_between_more(message[n], 'Ciudad:', 'Cuerpo del reason:'))
		reason.append(split_between_more(message[n], 'Cuerpo del reason:', 'Desea que le envíen email en caso de Actualización de Datos?'))
		refresh.append(split_between_more(message[n], 'Desea que le envíen email en caso de Actualización de Datos?', '--'))
		
split_message(messages_glo,name1,email1,institution1,city1,reason1,refresh1)
split_message(messages_reg,name2,email2,institution2,city2,reason2,refresh2)
split_message(messages_cr2met,name3,email3,institution3,city3,reason3,refresh3)
split_message(messages_chirps,name4,email4,institution4,city4,reason4,refresh4)

def create_table(name,email,subject,reason,city,refresh,table_name,date):
	df= pd.DataFrame({'Category:'table_name, 'Date': date, 'Name':name, 'Email': email, 'Subject': subject, 'City:' city, 'Reason': reason, 'Refresh?'= refresh })
	#Create a new dataframe
	
	df.to_csv(str(table_name+".csv"), sep=',', encoding='utf-8')
	print('table '+table_name+'.csv created')

create_table(name1,email1,subject1,reason1,city1,refresh1,"simulaciones_globales",date_glo)
create_table(name2,email2,subject2,reason2,city2,refresh2,"simulaciones_regionales",date_reg)
create_table(name3,email3,subject3,reason3,city3,refresh3,"cr2met",date_cr2met)
create_table(name4,email4,subject4,reason4,city4,refresh4,"chirps",date_chirps)

