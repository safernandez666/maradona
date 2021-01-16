#!/bin/bash
 

################################################################
################## Update below values  ########################
 
MYSQL_USER='root'
MYSQL_PASSWORD='secret'
DATABASE_NAME='maradona'

 
#################################################################
 
echo "Backup started for database - ${DATABASE_NAME}"
 
 
mysqldump -h ${MYSQL_HOST} \
   -P ${MYSQL_PORT} \
   -u ${MYSQL_USER} \
   -p${MYSQL_PASSWORD} \
   ${DATABASE_NAME} < /docker-entrypoint-initdb.d/init.sql
 
if [ $? -eq 0 ]; then
  echo "Ejecuto sin problemas en la Base Maradona"
else
  echo "Error found during backup"
  exit 1
fi