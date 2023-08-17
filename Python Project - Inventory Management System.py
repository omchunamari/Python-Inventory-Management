#SOURCE CODE FOR INVENTORY MANAGEMENT
print("INVENTORY MANAGEMENT SYSTEM by Om Chunamari")
#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists inventory")
mycursor.execute("use inventory")
#creating required tables 
mycursor.execute("create table if not exists inventory_master(srno varchar(4) primary key,productname varchar(30),suppliername varchar(20),contactdetails varchar(10),stock int(6))")
mycursor.execute("create table if not exists inventorylogs(srno varchar (4),quantity int(6),dot date,ttype char(1),foreign key (srno) references inventory_master(srno))")
mydb.commit()
while(True):
    
    print("1=Create New Inventory Entry/Record")
    print("2=Add stock to a product record")
    print("3=Remove stock from a product record for delivery")
    print("4=Display record")
    print("5=Exit")
    ch=int(input("Enter your choice:"))
    
#PROCEDURE FOR CREATING NEW PRODUCT ENTRY
    if(ch==1):
        print("Please fill the required information to create a new product entry")
        srno=str(input("Enter a unique serial number:"))
        productname=input("Enter name(limit 35 characters):")
        suppliername=str(input("Enter Supplier name:"))
        contactdetails=str(input("Enter supplier's contact details:"))
        stock=0
        mycursor.execute("insert into inventory_master values('"+srno+"','"+productname+"','"+suppliername+"','"+contactdetails+"','"+str(stock)+"')")
        mydb.commit()
        print("Product entry has successfully created !")
        
#PROCEDURE FOR UPDATING NEW STOCK STORAGE
    elif(ch==2):
        srno=str(input("Enter Serial Number:"))
        dp=int(input("No. of stock to be added? :"))
        dot=str(input("Enter date of storage: YYYY-MM-DD :"))
        ttype="d"
        mycursor.execute("insert into inventorylogs values('"+srno+"','"+str(dp)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update inventory_master set stock=stock+'"+str(dp)+"' where srno='"+srno+"'")
        mydb.commit()
        print("New stock has been succesfully accepted!!!")
#PROCEDURE FOR UPDATING EXISTING STOCK FOR DELIVERY
    elif(ch==3):
        srno=str(input("Enter serial number:"))
        wd=int(input("Please enter the amount of stock to be made ready for delivery:"))
        dot=str(input("Enter date of transaction: YYYY-MM-DD :"))
        ttype="w"
        mycursor.execute("insert into inventorylogs values('"+srno+"','"+str(wd)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update inventory_master set stock=stock-'"+str(wd)+"' where srno='"+srno+"'")
        mydb.commit()
        print("Stock has been updated!!!")
        
#PROCEDURE FOR DISPLAYING PRODUCT ENTRY
    elif(ch==4):
        srno=str(input("Enter serial number:"))
        mycursor.execute("select * from inventory_master where srno='"+srno+"'")
        for i in mycursor:
            print(i)
    else:
        break
        
        
