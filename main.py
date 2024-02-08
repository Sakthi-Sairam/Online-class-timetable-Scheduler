a="ONLINE CLASS TIMETABLE SHEDULER"
from pickle import load,dump #importing modules
import sys
import mysql.connector as mycon 
from tabulate import tabulate
from datetime import date
import time
print("%100s"%" ",end="")
time.sleep(0.5)
for i in a:
    print(i,end="")
    time.sleep(0.1)
print(" ")
#user defined functions
def insert(subject):
    clas = input("Enter Class (in Roman letters) ")
    section = input("Enter Section ")
    date = input("Enter Date (YYYY-MM-DD)")
    if len(date)!=10:
        print("DATE value is wrong, it should be in[YYYY-MM-DD] format")
        print("for example:  2020-08-09")
        print("program exiting")
        sys.exit()
    timing = input("Enter The Timing (HH:MM) ")
    if len(timing)!=5:
        print("timing value is wrong, it should be in[HH:MM] format")
        print("for example:  08:30")
        print("program exiting")
        sys.exit()
    ttnum=int(input("Enter time table number"))
    qry = "insert into octimetable values ({},'{}','{}','{}','{}','{}')".format(ttnum,clas,section,date,timing,subject)
    cur.execute(qry)
    con.commit()
    count = cur.rowcount
    print(count," record is inserted successfully.")
    print("Press Enter to continue.")
    input()
def showtt():
    print("SHOWING THE TIME TABLE")
    qry = "Select * from octimetable "
    cur.execute(qry)
    data = cur.fetchall()
    count = cur.rowcount
    h=['ttnum','clas','section','date','timing','subject']
    print(tabulate(data,headers=h,tablefmt='grid'))
    print("Press Enter to continue.")
    input()
def deletion(var):
    ttnum = input("Enter time table number to be deleted")
    subject = var
    qry = "delete from octimetable where ttnum = {} and subject='{}'".format(ttnum,subject)
    cur.execute(qry)
    con.commit()
    count = cur.rowcount
    if count>0:
        print("Record is deleted successfully.")
    else:
         print("Record is NOT deleted")
    print("Press Enter to continue.")
    input()
def autodel():
    today=date.today()
    today=str(today)
    qry = "delete from octimetable where date<'{}'".format(today)
    cur.execute(qry)
    con.commit()
    count = cur.rowcount
def update():
    print("UPDATION::")
    showtt()
    choice=input("WHAT YOU WANT TO UPDATE::CLASS-C,SECTION-S,DATE-D,TIME-T,SUBJECT-SUB").upper()
    ttno=int(input("ENTER THE TABLE NO::"))
    if choice=='C':
        clas=input("ENTER THE NEW CLASS::")
        qry="update octimetable set clas='{}' where ttnum={}".format(clas,ttno)
        cur.execute(qry)
        con.commit()
        count=cur.rowcount
        if count>0:
            print("UPDATED SUCCESSFULLY::")
        else:
            print("INVALID TABLENUMBER")
    elif choice=='S':
        sec=input("ENTER THE NEW SECTION::")
        qry="update octimetable set section='{}' where ttnum={}".format(sec,ttno)
        cur.execute(qry)
        con.commit()
        count=cur.rowcount
        if count>0:
            print("UPDATED SUCCESSFULLY::")
        else:
            print("INVALID TABLENUMBER")
    elif choice=='D':
        date=input("ENTER THE NEW DATE(YYYY-MM-DD,EX-2020-01-02)::")
        Len=len(date)
        if Len==10:
            qry="update octimetable set date='{}' where ttnum={}".format(date,ttno)
            cur.execute(qry)
            con.commit()
            count=cur.rowcount
            if count>0:
                print("UPDATED SUCCESSFULLY::")
            else:
                print("NO RECORDS FOUND")
        else:
            print("INVALID DATE CHECK IT AGAIN::")
    elif choice=='T':
        timing=input("ENTER THE NEW TIMING(HH:MM)::")
        qry="update octimetable set timing='{}' where ttnum={}".format(timing,ttno)
        cur.execute(qry)
        con.commit()
        count=cur.rowcount
        if count>0:
            print("UPDATED SUCCESSFULLY::")
        else:
            print("NO RECORDS FOUND")
    elif choice=='SUB':
        subject=input("ENTER THE SUBJECT::")
        qry="update octimetable set subject='{}' where ttnum={}".format(subject,ttno)
        cur.execute(qry)
        con.commit()
        count=cur.rowcount
        if count>0:
            print("UPDATED SUCCESSFULLY::")
            
        else:
            print("NO RECORDS FOUND")
    else:
        print("INVALID OPTION::")
    print("Press Enter to continue.")
    input()
def search():
    print("SEARCHING::")
    showtt()
    opt=input("SEARCH USING---TABLENUMBER-T,CLASS-C,SECTION-S,DATE-D,TIME-TI,SUBJECT-SUB").upper()
    if opt=='T':
        tno=int(input("ENTER THE TABLE NO::"))
        qry="select * from octimetable where ttnum='{}'".format(tno)
        cur.execute(qry)
        data=cur.fetchall()
        count=cur.rowcount
        if count>0:
            h=['TABLENUMBER','CLASS','SECTION','DATE','TIME','SUBJECT']
            print(tabulate(data,headers=h,tablefmt='grid'))
            input("ENTER ANY KEY::")
        else:
            print("NO RECORDS FOUND::")
    elif opt=='C':
        Class=input("ENTER THE CLASS::")
        qry="select * from octimetable where clas='{}'".format(Class)
        cur.execute(qry)
        data=cur.fetchall()
        count=cur.rowcount
        if count>0:
            h=['TABLENUMBER','CLASS','SECTION','DATE','TIME','SUBJECT']
            print(tabulate(data,headers=h,tablefmt='grid'))
            input("ENTER ANY KEY::")
        else:
            print("NO RECORDS FOUND::")
    elif opt=='S':
        sec=input("ENTER THE SECTION::")
        qry="select * from octimetable where section='{}'".format(sec)
        cur.execute(qry)
        data=cur.fetchall()
        count=cur.rowcount
        if count>0:
            h=['TABLENUMBER','CLASS','SECTION','DATE','TIME','SUBJECT']
            print(tabulate(data,headers=h,tablefmt='grid'))
            input("ENTER ANY KEY::")
        else:
            print("NO RECORDS FOUND::")
    elif opt=='D':
        date=input("ENTER THE  DATE(YYYY-MM-DD,EX-2020-01-02)::")
        Len=len(date)
        if Len==10:
            qry="select * from octimetable where date='{}'".format(date)
            cur.execute(qry)
            data=cur.fetchall()
            count=cur.rowcount
            if count>0:
                h=['TABLENUMBER','CLASS','SECTION','DATE','TIME','SUBJECT']
                print(tabulate(data,headers=h,tablefmt='grid'))
                input("ENTER ANY KEY::")
            else:
                print("NO RECORDS FOUND")
        
        else:
            print("INVALID DATE CHECK IT AGAIN::")
    elif opt=='TI':
        time=input("ENTER THE TIME(HH:MM)::")
        Len=len(time)
        if Len==5:
            qry="select * from octimetable where timing='{}'".format(time)
            cur.execute(qry)
            data=cur.fetchall()
            count=cur.rowcount
            if count>0:
                h=['TABLENUMBER','CLASS','SECTION','DATE','TIME','SUBJECT']
                print(tabulate(data,headers=h,tablefmt='grid'))
                input("ENTER ANY KEY::")
            else:
                print("INVALID TIME::")
        else:
            print("PLEASE CHECK THE FORMAT AGAIN")
    elif opt=='SUB':
        sub=input("ENTER THE SUBJECT::")
        qry="select * from octimetable where subject='{}'".format(sub)
        cur.execute(qry)
        data=cur.fetchall()
        count=cur.rowcount
        if count>0:
            h=['TABLENUMBER','CLASS','SECTION','DATE','TIME','SUBJECT']
            print(tabulate(data,headers=h,tablefmt='grid'))
            input("ENTER ANY KEY::")
        else:
            print("NO RECORDS FOUND::")
    else:
        print("INVALID OPTION::")
        sys.exit()
#MAIN PROGRAM
con = mycon.connect(host='localhost',user='root',passwd='root') #connecting mysql
if con.is_connected():
    cur = con.cursor()
    cur.execute("Create database if not exists onlineclass_sheduler") #Creating Database
    cur.execute("use onlineclass_sheduler") #Using Database
    cur.execute("create table if not exists octimetable(ttnum int(6) primary key,clas char(4),\
section char(1),date char(15),timing char(5), subject char(20))")
else:
    print("mysql not connected")
    
#admin logins
try:
    with open ('principleadmin.dat','rb') as fin:
        rec=load(fin)
except:
    with open ('principleadmin.dat','wb') as fout:
        print("SIGNIN PRINCIPLE ADMIN")
        adname=input("ENTER ADMIN USERNAME:")
        adpass=input("ENTER ADIMIN PASSWORD :")
        print("signin sucesfull")
        rec=[adname,adpass]
        dump(rec,fout)
#validation for admins
print(" ")
time.sleep(0.25)
print("WHO ARE YOU? student,subject teacher or principal")
print(" ")
time.sleep(0.25)
who=input("if you are a STUDENT press 's',TEACHER press't',PRINCIPAL press'p'::").lower()
print(" ")
time.sleep(0.25)
autodel()

if who=='p': #principal interface
    adname=input("ENTER ADMIN USERNAME:")
    adpass=input("ENTER ADIMIN PASSWORD :")
    if adname==rec[0] and adpass==rec[1]:
        print("permission granted")
    else:
        print("permission denied")
        sys.exit()
    while True:
        print(" ")
        time.sleep(0.5)
        print("press 1:To add subject teachers")
        time.sleep(0.5)
        print("press 2:To insert a class in the timetable")
        time.sleep(0.5)
        print("press 3:To view timetable")
        time.sleep(0.5)
        print("press 4:To update anything in time table")
        time.sleep(0.5)
        print("press 5:To delete a class in time table")
        time.sleep(0.5)
        print("press 6:To search for anything in time table")
        time.sleep(0.5)
        print("press 7: To exit")
        time.sleep(0.5)
        print(" ")
        cho=int(input("enter your choice::"))
        if cho==7:
            print("exited")
            sys.exit()
        elif cho==5:
            showtt()
            print("Delete a Record")
            var=input("Enter The subject to be deleted ")
            deletion(var)
        elif cho==3:
            showtt()
        elif cho==4:
            update()
        elif cho==2:
            print("Inserting a Record")
            subject = input("Enter Subject ").lower()
            insert(subject)
        elif cho==6:
            search()
        elif cho==1:
            try:
                fin=open('teacherslogin.bin','rb')
                rec1=load(fin)
                fin.close()
            except :
                rec1=[]
            ch='y'
            fout=open('teacherslogin.bin','wb')
            while ch=='y':
                name=(input("ENTER TEACHER NAME:"))
                pas=input("SET PASSWORD:")
                sub=input("ENTER SUBJECT::")
                rec1+=[[name,pas,sub]]
                print("SUCCESSFULLY ADDED A NEW TEACHER")
                ch=input("WANT TO ADD MORE LOGIN DETAILS: y or n").lower
            dump(rec1,fout)
            fout.close()
        else:
            print("wrong choice")
    
elif who=='t': #teacher interface
    try:
        fin=open('teacherslogin.bin','rb')
        r=load(fin)
        fin.close()
    except:
        print("first principal should add you first")
        sys.exit()
    tname=(input("ENTER TEACHER NAME:"))
    tpas=input("PASSWORD:")
    for i in r:
        if i[0]==tname and i[1]==tpas:
            print("teacher access granted")
            dsub=i[2]
            break
    else:
        print("access denied")
        sys.exit()
    while True:
        print(" ")
        time.sleep(0.5)
        print("press 1:To insert a class in the timetable")
        time.sleep(0.5)
        print("press 2:To deletion")
        time.sleep(0.5)
        print("press 3:To view timetable")
        time.sleep(0.5)
        print("press 4:To search for anything in time table")
        time.sleep(0.5)
        print("press 5:To exit")
        time.sleep(0.5)
        print(" ")
        cho=int(input("enter your choice::"))
        if cho==5:
            print("exited")
            sys.exit()
        elif cho==4:
            search()
        elif cho==1:
            print("Inserting a Record")
            insert(dsub)
        elif cho==3:
            showtt()
        elif cho==2:
            showtt()
            print("Delete a Record")
            deletion(dsub)
        else:
            print("wrong choice")



else:#student login
    while True:
        print(" ")
        time.sleep(0.5)
        print("press 1:To view timetable")
        time.sleep(0.5)
        print("press 2:To search anything in timetable")
        time.sleep(0.5)
        print("press 3:To exit")
        time.sleep(0.5)
        print(" ")
        cho=int(input("enter your choice"))
        if cho==1:
            showtt()
        elif cho==3:
            print("terminating")
            sys.exit()
        elif cho==2:
            search()
        else:
            print("wrong choice")

