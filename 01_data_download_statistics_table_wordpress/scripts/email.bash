#!/bin/bash

username=$EMAIL
password=$FROM_PWD
echo
curl -u $username:$password --silent "https://mail.google.com/mail/feed/atom" |  grep -oPm1 "(?<=<title>)[^<]+" | sed '1d'

#curl --url 'smtps://smtp.gmail.com:465' --ssl-reqd \
#  --mail-from username --mail-rcpt 'nvaldebenito@uchile.cl' \
#  --upload-file email.txt --user $username:$password --insecure

echo 'Nueva busqueda'
curl -u $username:$password --silent "https://mail.google.com/mail/feed/atom" | tr -d '\n' | awk -F '<entry>' '{for (i=2; i<=NF; i++) {print $i}}' | sed -n "s/<title>\(.*\)<\/title.*name>\(.*\)<\/name>.*/\2 - \1/p" 
echo " NEW"
curl -u $username:$password --silent "https://mail.google.com/mail/feed/atom" | grep -oPm1 "(?<=<title>)[^<]+"
