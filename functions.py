import tabulate as t
import mysql.connector as m

a=m.connect(host="localhost",user="root",passwd="",database="school")
b=a.cursor()

def insert_record():
    print("\n\t\t-----Enter Student Details-----\n")
    x=int(input("enter admission number:"))
    y=input("enter student name:")
    c=int(input("enter student rno:"))
    d=int(input("enter student class:"))
    q="insert into student values('{}','{}','{}','{}')".format(x,y,c,d)
    b.execute(q)
    a.commit()
    print("\n\t\t-------- Data Saved to Database-------")
    
def delete_record():
    print("\n\t\t-----Delete Menu------\n")
    print("1. Delete by Admission number\n2. Delete by Name\n3. EXIT\n----Enter Option---")
    ch=int(input())
    if ch==1:
        ad=int(input("----Enter Admission Number of Student-----"))
        q="select * from student where admno='{}'".format(ad)
        b.execute(q)
        res=b.fetchall()
        if len(res)==0:
            print("\n\t\t---Data not Found----\n")
        else:
            print(t.tabulate(res,headers=['admission number','student name','student roll_no','student class'],tablefmt='pretty'))
            print("\n\t\t---Do you want to remove this record(y for yes)----\n")
            aa=input()
            if aa=='y':
                q="delete from student where admno='{}'".format(ad)
                b.execute(q)
                a.commit()
                print("\n\t\t----Data Deleted Successfully----\n")
        
    elif ch==2:
        cd=input("-----Enter  Name of Student------")
        q="select * from student where stu_name='{}'".format(cd)
        b.execute(q)
        res=b.fetchall()
        if len(res)==0:
            print("\n\t\t----Data Not Found-----\n")
        else:
            print(t.tabulate(res,headers=['admission number','student name','student roll_no','student class'],tablefmt='pretty'))
            print("\n\t\t---Do you want to remove this record(y for yes)----\n")
            aa=input()
            if aa=='y':
                q="delete from student where stu_name='{}'".format(cd)
                b.execute(q)
                a.commit()
                print("\n\t\t----Data Deleted Successfully-----\n")
    elif ch==3:
        print(ww)
    else:
        print("----Invalid option selected----")
            
def search_record():
    print("\n\t\t-----Search Menu------\n")
    print("1. Search by Admission number\n2. Search by Name\n3. EXIT\n----Enter Option---")
    ch=int(input())
    if ch==1:
        ad=int(input("----Enter Admission Number of Student-----"))
        q="select * from student where admno='{}'".format(ad)
        b.execute(q)
        res=b.fetchall()
        if len(res)==0:
            print("\n\t\t---Data not Found----\n")
        else:
            print(t.tabulate(res,headers=['admission number','student name','student roll_no','student class'],tablefmt='pretty'))
    elif ch==2:
        op=input("-----Enter Student Name------")
        q="select * from student where stu_name='{}'".format(op)
        b.execute(q)
        res=b.fetchall()
        if len(res)==0:
            print("\n\t\t---Data Not Found----\n")
        else:
            print(t.tabulate(res,headers=['admission number','student name','student roll_no','student class'],tablefmt='pretty'))
    elif ch==3:
        print(ww)
    else:
        print("----Invalid option selected----")
def update_record():
    print("\n\t\t-----Update Menu------\n")
    print("1.update by Admission Number\n2. update by Name\n3. EXIT\n----Enter Option---")
    ch=int(input())
    if ch==1:
        ad=int(input("------Enter Admission Number of Student--------"))
        q="select * from student where admno='{}'".format(ad)
        b.execute(q)
        res=b.fetchall()
        if len(res)==0:
            print("\n\t\t---DATA NOT FOUND----\n")
        else:
            print(t.tabulate(res,headers=['admisssion number','student name','student roll_no','student class'],tablefmt='pretty'))
            cd=input("-------DO YOU WANT TO UPDATE THIS RECORD(Y for YES)--------")
            if cd=='y':
                print("\n\t\t----Enter New Details----\n")
                m1=int(input("enter admission number:"))
                m2=input("enter name:-")
                m3=int(input("enter roll no:-"))
                m4=int(input("enter class:-"))
                q="update student set admno='{}',stu_name='{}',stu_rno='{}',stu_class='{}' where admno='{}'".format(m1,m2,m3,m4,ad)
                b.execute(q)
                a.commit()
                print("\n\t\t---Data Updated Successfully ---\n")
    if ch==2:
        cd=input("--------Enter Name of Student-------")
        q="select * from student where stu_name='{}'".format(cd)
        b.execute(q)
        res=b.fetchall()
        if len(res)==0:
            print("\n\t\t----DATA NOT FOUND-----\n")
        else:
            print(t.tabulate(res,headers=['admission number','student name','student roll_no','student class'],tablefmt='pretty'))
            tr=input("-------DO YOU WANT TO UPDATE THIS RECORD(Y FOR YES)-------")
            if tr=='y':
                print("\n\t\t----Enter New Details----\n")
                n1=int(input("enter admission number:"))
                n2=input("enter name:-")
                n3=int(input("enter roll no:-"))
                n4=int(input("enter class:-"))
                q="update student set admno='{}',stu_name='{}',stu_rno='{}',stu_class='{}' where stu_name='{}'".format(n1,n2,n3,n4,cd)
                b.execute(q)
                a.commit()
                print("\n\t\t---Data Updated Successfully---\n")
                
                
    elif ch==3:
        print(ww)
    else:
        print("-----INVALID OPTION SELECTED------")
def csvfile_record():
    print("\n\t\t----DATA STORE MENU-----\n")
    print("1. Data Store by Class\n2. Data Store by Name\n3. All Data Store\n4.EXIT----Enter Option---")
    ch=int(input())
    if ch==1:
        name=input("--Enter File Name---")
        name=name+".csv"
        try:
            f=open(name,"r")
            f.close()
            print("\n\t\t----File already Present---- Please Enter Different Name----\n")
        except:
            f=open(name,"w")
            ad=int(input("----Enter Class -----"))
            q="select * from student where stu_class='{}'".format(ad)
            b.execute(q)
            res=b.fetchall()
            if len(res)==0:
                print("\n\t\t---Data not Found----\n")
            else:
                import csv
                
                d=csv.writer(f)
                for i in res:
                    d.writerow(i)
                f.close()
                print("\n\t\t----Data saved to file----")
    if ch==2:
        name=input("--Enter file name----")
        name=name+".csv"
        try:
            f=open(name,"r")
            f.close()
            print("\n\t\t----File already Present---- Please Enter Different Name----\n")
        except:
            f=open(name,"w")
            bd=input("Enter Student Name:")
            q="select * from student where stu_name='{}'".format(bd)
            b.execute(q)
            res=b.fetchall()
            if len(res)==0:
                print("\n\t\t---DATA NOT FOUND---\n")
            else:
                import csv
                f=open("records.csv","w")
                d=csv.writer(f)
                for i in res:
                    d.writerow(i)
                f.close()
                print("\n\t\t-----DATA SAVED TO RECORDS.CSV FILE-----\n")
    if ch==3:
        
        name=input("--Enter file name----")
        name=name+".csv"
        try:
            f=open(name,"r")
            f.close()
            print("\n\t\t----File already Present---- Please Enter Different Name----\n")
        except:
            f=open(name,"w")
            
            q="select * from student"
            b.execute(q)
            res=b.fetchall()
            if len(res)==0:
                print("\n\t\t----DATA NOT FOUND----\n")
            else:
                import csv
                d=csv.writer(f)
                for i in res:
                    d.writerow(i)
                f.close()
                print("\n\t\t------ ALL DATA SAVED TO FILE-------\n")
            
    
    
        
