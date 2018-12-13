#!/usr/bin/python
import xlrd
import os
import sqlite3
# Written by aneesh on 18/10/16; final format
# WritePhoneContact("Aneesh PA", "8986880327", "DM", "2393",cntx); 

rCode="131016"   #ref code for the database 
#----------------------------------------------------------------------
def open_file(path):
    """ Process xls file and store into text file.
	
    This code will be used in android
    """
    book = xlrd.open_workbook(path)
    first_sheet = book.sheet_by_index(0)
    with open('contacts.txt', 'r+') as file:
       	for i in range (1000):
        	name=first_sheet.cell(i,0).value.rstrip('0').rstrip('.')
		desig=first_sheet.cell(i,1).value.rstrip('0').rstrip('.')
		epabx_f=first_sheet.cell(i,2)
        	epabx=str(epabx_f.value).rstrip('0').rstrip('.')	
		mobile_f=first_sheet.cell(i,3)
        	mobile=str(mobile_f.value).rstrip('0').rstrip('.')	
		file.write("WritePhoneContact(\"%s\", \"%s\", \"%s\", \"%s\",cntx);\n" %(name, desig, epabx,mobile)) 
 

if __name__ == "__main__":
    path = "130616.xls"
    open_file(path)



