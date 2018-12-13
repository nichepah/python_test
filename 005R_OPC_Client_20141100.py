# Written by Aneeh PA in Nov 2014
# Uses openOPC to read data from a Simulated OPC Server and saves it to a database
import os
import OpenOPC
import sqlite3
import time


dbfile='tagListSqlite3.db'                  #database file
opcserver='Matrikon.OPC.Simulation.1'       #'RSLinx OPC Server'
# topic='[test]'                             #Linx's topic
# tag1='RIO_8:9:O.Ch0Data'
# tag2='CURRENT_PASS'
# taglist=[topic+tag1,topic+tag2]
tag_count=4;
taglist=[]
with open('input.txt', 'r') as f:
    for (i=0; i<tag_count, i++):
        taglist.append( f.readline().strip()) #change to include topic for RS
print("taglist: "+taglist+"\n")
sampletime=10;                              #seconds                    
dbexist=os.path.exists(dbfile)  #checks if dbfile exists
db = sqlite3.connect(dbfile)
cur=db.cursor()
# create Table
# saves timestamps of all tags
# +might not be gud for u!
# we save a ref sys stamp as well
if not dbexist:
    sqlstring = 'CREATE TABLE opcdata (id INTEGER PRIMARY KEY, '
    for (i=0; i<tag_count; i++):
        sqlstring += tags[i]+' TEXT, val'+i+'stat1 TEXT, timestamp'+i+'TEXT,'
    sqlstring += 'atime TEXT)'
    cur.execute(sqlstring)
    db.commit()
while 1>0:                          #thtz infinite
    opc=OpenOPC.client()
    opc.connect(opcserver)      #its opctag1 moal, not topic+tag1
    opctagstring='['
    for (i=0; i<tag_count; i++):
        opctagstring += '(opctag'+i+', opcvalue'+i+', opcstat'+i+', opctime'+i+')'
        if (i != tag_count-1):
            opctagstring += ','
            else:
                opctagstring += ']'
    print ("opctagstring: "+opctagstring+"\n"
    opctagstring = opc.read(taglist)
    opc.close()
    atime = time.asctime()
    ins_sqlstring = []
    ins_sqlstring = 'INSERT INTO opcdata (id, '
    for (i=0; i<tag_count; i++):
           ins_sqlstring += '
    tag1, val1, stat1, timestamp1, \
    tag2, val2, stat2, timestamp2, \
    atime) \
    VALUES(NULL, \
    "%s", "%f", "%s", "%s", \
    "%s", "%f", "%s", "%s", \
    "%s")'\
    %(topic+tag1, opcvalue1, opcstat1, opctime1, \
    topic+tag2, opcvalue2, opcstat2, opctime2, \
    atime)
    cur.execute(sqlstring)
    db.commit()
    # cur.execute('SELECT * FROM opcdata')
    # dbvalues=cur.fetchall()
    # dblen=len(dbvalues)
    # print dbvalues[dblen-1]
    db.close()
    time.sleep(sampletime)

