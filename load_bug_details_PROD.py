#!/usr/bin/python2
import cx_Oracle
import time
import sqlite3

def bugreportFunc():

	try:	
		
		conn = cx_Oracle.connect('bkakani/xxxx@bugap')
		
		conn2 = sqlite3.connect('/scratch/apps/bugdbProd/db.sqlite3')
		subj = " "
		while True:
		
				cur = conn.cursor()
		
				cur2 = conn2.cursor()
		
				cur2.execute("delete from  bug_details")
		
				sql1 = "select rptno,programmer,status,subject from rpthead where product_id = 12609 and status in (11,30) and category = 'STRATENV' and (subject like '%DEV 10%' or subject like '%DEV10%' or rptno in (select rptno from rptbody where rptno in (select rptno from rpthead where product_id = 12609 and status in (11,30) and category = 'STRATENV') and (comments like '%DEV10%' or comments like '%DEV 10%')))"
		
				sql2 = "select rptno,programmer,status,subject from rpthead where product_id = 12609 and status in (11,30) and category = 'STRATENV' and (subject like '%DEV 15%' or subject like '%DEV15%' or rptno in (select rptno from rptbody where rptno in (select rptno from rpthead where product_id = 12609 and status in (11,30) and category = 'STRATENV') and (comments like '%DEV15%' or comments like '%DEV 15%')))"
		
				cur.execute(sql1)
		
				i = 1
		
				for data in cur:
						subj = data[3]
						if "'" in data[3]:
								subj = data[3].split("'")[0]+data[3].split("'")[1]
		
						cur2.execute("insert into bug_details values(%s,%s,'%s',%s,'%s','%s')" %(int(i),data[0],data[1],data[2],subj,'DEV10'))
						i += 1
		
				cur.execute(sql2)
		
				for data in cur:
						subj = data[3]
						if "'" in data[3]:
								subj = data[3].split("'")[0]+data[3].split("'")[1]
		
						cur2.execute("insert into bug_details values(%s,%s,'%s',%s,'%s','%s')" %(int(i),data[0],data[1],data[2],subj,'DEV15'))
						i += 1
		
				conn2.commit()
				cur.close()
				cur2.close()
				time.sleep(5)
	except cx_Oracle.Error:
		bugreportFunc()

bugreportFunc()
