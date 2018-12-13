#!/usr/bin/python
import xlrd
import os
import sqlite3
# Written by aneesh on 18/10/16
# Reads "130616.xls" and writes its contents to sqlite db "130616.db"

dbfile='130616.db'
rCode="131016"   #ref code for the database 

def open_file(path):
    """ Process xls file and store into sqlite

    """
    book = xlrd.open_workbook(path)
    dbexist=os.path.exists(dbfile)  #checks if dbfile exists
    db = sqlite3.connect(dbfile)
    cur=db.cursor()
    # create Table
    # saves timestamps of all tags
    # +might not be gud for u!
    # we save a ref sys stamp as well
    if not dbexist:
        sqlstring = 'CREATE TABLE contactsTable (id INTEGER PRIMARY KEY, \
        name TEXT, designation TEXT, epabx TEXT, mobileNumber TEXT, refCode TEXT)'
        cur.execute(sqlstring)
        db.commit()
    # get the first worksheet
    first_sheet = book.sheet_by_index(0)
    # read a row
    for i in range (234):
        name=first_sheet.cell(i,0).value.rstrip('0').rstrip('.')
	desig=first_sheet.cell(i,1).value.rstrip('0').rstrip('.')
	epabx_f=first_sheet.cell(i,2)
        epabx=str(epabx_f.value).rstrip('0').rstrip('.')	
	mobile_f=first_sheet.cell(i,3)
        mobile=str(mobile_f.value).rstrip('0').rstrip('.')	
	sqlstring = 'INSERT INTO contactsTable (id, \
    	name, designation, epabx, mobileNumber, refCode) \
    	VALUES(NULL, "%s", "%s", "%s", "%s", "%s")'\
    	%(name, desig, epabx, mobile,rCode)
    	cur.execute(sqlstring)
    	db.commit()


if __name__ == "__main__":
    path = "130616.xls"
    open_file(path)


