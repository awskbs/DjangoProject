#!/usr/bin/python2
#This Program is developped by Balasundaram Kakani!!
import cx_Oracle
import time
import sqlite3

f = open("/scratch/apps/bugs_details.csv","w")
conn = cx_Oracle.connect('bkakani/L510sundar@bugap')
subj = " "
f.write("rptno,rptdate,programmer,status,product_id,category,subject\n")
cur = conn.cursor()

sql1 = "select rptno,rptdate,programmer,status,product_id,category,subject from rpthead where product_id = 12609 and  category = 'STRATENV' and (subject like '%DEV 10%' or subject like '%DEV10%' or rptno in (select rptno from rptbody where rptno in (select rptno from rpthead where product_id = 12609 and category = 'STRATENV') and (comments like '%DEV10%' or comments like '%DEV 10%')))"

cur.execute(sql1)
       

for data in cur:
	subj = data[6]
	if "," in subj:
		subj = data[6].split(",")[0]
	content = str(data[0])+","+str(data[1])+","+data[2]+","+str(data[3])+","+str(data[4])+","+data[5]+","+subj+"\n"
	f.write(content)
	
cur.close()
f.close()



