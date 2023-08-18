import mysql.connector
#Create the connection object 
conn= mysql.connector.connect(host='localhost',
                        database='INTELLI',
                        user='root',
                        password='7877766268')


#creating the cursor object  
cur=conn.cursor(buffered=True)

# to create table in SQL
try:  
    dbs = cur.execute("create table hotelsF1( Name varchar(20) not null,address varchar(20) not null,phone_number int(20) not null ,no_of_days int(10) not null,total_amount int(20) not null)")  
    # dbs = cur.execute("show databases")  
except:  
    conn.rollback()  
#create a function to insert data
def submit():
    sql = "insert into hotelsF1(Name,address ,phone_number,no_of_days,total_amount ) values (  %s, %s, %s,%s,%s)"  
    val = (text2.get(),text3.get(),text4.get(),int(text5.get(1.0,END)),label7['text'])  
    #inserting the values into the table  
    cur.execute(sql,val)
    #commit the transaction   
    conn.commit()  
# create a function to define cost of room
def cost():
    days = int(text5.get(1.0,END))
    if(basic.get()==1):
       label7.config(text=500*days)
       c2.deselect()
       c3.deselect()
    if(delux.get()==1):
       label7.config(text=1000*days)     
       c1.deselect()
       c3.deselect()
    if(superdelux.get()==1):
       label7.config(text=1500*days)
       c1.deselect()
       c2.deselect()
    if(basic.get()==0 and delux.get()==0 and superdelux.get()==0):
         label7.config(text="0") 
# create a function to show all data
def show_data():
    cur.execute("select * from hotelsF1")
    ans = cur.fetchall()
    for i in ans:
        print(i)
#design a main window
from tkinter import *
window=Tk()
window.geometry("1100x500")
basic = IntVar()
delux = IntVar()
superdelux = IntVar()
label1 = Label(window,text="HOTEL",font="Verdana 50 bold",bg="#ff0000")
label1.place(x=100,y=20)
c1 = Checkbutton(window, text='Basic', onvalue=1, offvalue=0,variable=basic,command=cost)
c1.place(x=50,y=120)
c2 = Checkbutton(window, text='Delux', onvalue=1, offvalue=0,variable=delux,command=cost)
c2.place(x=200,y=120)
c3 = Checkbutton(window, text='Super delux', onvalue=1, offvalue=0,variable=superdelux,command=cost)
c3.place(x=350,y=120)
label2 = Label(window,text="Name",font="Verdana 10 bold")
label2.place(x=100,y=180)
text2 = Entry(window)
text2.place(x=300,y=180)
label3 = Label(window,text="Address",font="Verdana 10 bold")
label3.place(x=100,y=220)
text3 = Entry(window)
text3.place(x=300,y=220)
label4 = Label(window,text="Phone number",font="Verdana 10 bold")
label4.place(x=100,y=260)
text4 = Entry(window)
text4.place(x=300,y=260)
label5 = Label(window,text="Number of days",font="Verdana 10 bold")
label5.place(x=100,y=300)
text5 = Text(window,height=1,width=20)
text5.place(x=300,y=300)
label6 = Label(window,text="Total amount to be paid",font="Verdana 10 bold")
label6.place(x=100,y=340)
label7 = Label(window,text="0",font="Verdana 10 bold")
label7.place(x=300,y=340)
b1 = Button(text="Add new entry",command=submit)
b1.place(x=100,y=400)
b2 = Button(text="show_data",command=show_data)
b2.place(x=200,y=400)
window.mainloop()