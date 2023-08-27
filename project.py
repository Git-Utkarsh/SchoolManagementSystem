from tkinter import * 
import mysql.connector as sqltor
import tkinter.messagebox 
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# mycon = sqltor.connect(host="localhost",user="root",passwd="root",database="project")
#https://www.phpmyadmin.co/
try:
     mycon = sqltor.connect(host="sql6.freesqldatabase.com",user="sql6642699",passwd="fDAg7Cj5AW",database="sql6642699")
     cursor = mycon.cursor()
except:
     tkinter.messagebox.showinfo('Project','Error !! Not Connected to database')
     exit()

l = []
data = []
info = ['Reg No. :-','Name :-','Class :-','Sec :-','D.O.B. :-','Mobile No. :-','Adhar No. :-','Address :-','Father Name. :-','Mother Name. :-']

def add():
     var_data_1 = var_1entry.get()
     var_data_2 = var_2entry.get()
     var_data_3 = var_3entry.get()
     var_data_4 = var_4entry.get()
     var_data_5 = var_5entry.get()
     var_data_6 = var_6entry.get()
     var_data_7 = var_7entry.get()
     var_data_8 = var_8entry.get()
     var_data_9 = var_9entry.get()
     var_data_10 = var_10entry.get()
     query = """INSERT INTO data(Reg_no,Name,Class,Section,DOB,
     Mobile_no,Adhaar_No,Address,Father_Name,
     Mother_Name) VALUES({},'{}',{},'{}','{}',{},'{}','{}',
     '{}','{}')""".format(var_data_1,var_data_2,var_data_3,var_data_4,var_data_5,var_data_6,var_data_7,var_data_8,var_data_9,var_data_10)
     try:
          cursor.execute(query)
          mycon.commit()
          l = [var_data_1,var_data_2,var_data_3,var_data_4,var_data_5,var_data_6,var_data_7,var_data_8,var_data_9,var_data_10]
          print(l)
          tkinter.messagebox.showinfo('Project','Data Stored successfully !!!')
     except Exception as e:
          print(e)
          tkinter.messagebox.showinfo('Project','Error Occured !!!')
     
def retrive():
     try:
          var_data_11 = int(var_11entry.get())
          cursor.execute("SELECT * FROM data WHERE Reg_no='%s'",(var_data_11,))
          data = cursor.fetchall()
          count = cursor.rowcount
          if count==0:
                tkinter.messagebox.showinfo('Project','No data found !')
          for i in range(len(data)):
               print(data[i])
               s = ''
               for j in range(10):
                         s += info[j]+' '+ str(data[i][j])+'\n'
                         display_label.config(text=s)
     except:
          tkinter.messagebox.showinfo('Project','Enter the Data to be Retrived !')
               
def delete():
    try:
     var_data_11 = int(var_11entry.get())
     sql1 = "DELETE FROM data WHERE Reg_no='%s'"
     data1=(var_data_11,)
     result=tkinter.messagebox.askquestion('Project','Are you sure you want to delete ')
     if result=='yes':
          cursor.execute(sql1,data1)
          mycon.commit()
          tkinter.messagebox.showinfo('Project','Deleted successfully')
    except:
         tkinter.messagebox.showinfo('Project','Enter the Data to be deleted !')

display = tkinter.Tk()
display.title('Student Info')
frame = tkinter.Frame(display)
frame.pack()

f1 = tkinter.LabelFrame(frame,text='Data')
f1.grid(row = 0,column =0,sticky = 'news',padx=20,pady=10)

var_1 = tkinter.Label(f1, text='Reg.No. :- ')
var_1.grid(row = 1, column = 0)
var_1entry = tkinter.Entry(f1)
var_1entry.grid(row = 1,column = 1)

var_2 = tkinter.Label(f1, text='Name :-')
var_2.grid(row = 2, column = 0)
var_2entry = tkinter.Entry(f1)
var_2entry.grid(row = 2,column = 1)

var_3 = tkinter.Label(f1, text='Class :-')
var_3.grid(row = 3, column = 0)
var_3entry = tkinter.Entry(f1)
var_3entry.grid(row = 3,column = 1)

var_4 = tkinter.Label(f1, text='Sec :-')
var_4.grid(row = 4, column = 0)
var_4entry = tkinter.Entry(f1)
var_4entry.grid(row = 4,column = 1)

var_5 = tkinter.Label(f1, text='D.O.B. :-')
var_5.grid(row = 5, column = 0)
var_5entry = tkinter.Entry(f1)
var_5entry.grid(row = 5,column = 1)

var_6 = tkinter.Label(f1, text='Mobile No. :-')
var_6.grid(row = 6, column = 0)
var_6entry = tkinter.Entry(f1)
var_6entry.grid(row = 6,column = 1)

var_7 = tkinter.Label(f1, text='Adhar No. :-')
var_7.grid(row = 7, column = 0)
var_7entry = tkinter.Entry(f1)
var_7entry.grid(row = 7,column = 1)

var_8 = tkinter.Label(f1, text='Address :-')
var_8.grid(row = 8, column = 0)
var_8entry = tkinter.Entry(f1)
var_8entry.grid(row = 8,column = 1)

var_9 = tkinter.Label(f1, text='Father Name :-')
var_9.grid(row = 9, column = 0)
var_9entry = tkinter.Entry(f1)
var_9entry.grid(row = 9,column = 1)

var_10 = tkinter.Label(f1, text='Mother Name :-')
var_10.grid(row = 10, column = 0)
var_10entry = tkinter.Entry(f1)
var_10entry.grid(row = 10,column = 1)

for widget in f1.winfo_children():
     widget.grid_configure(padx = 10,pady = 5)

button1 = tkinter.Button(f1,text="Add",command = add)
button1.grid(row = 11, column = 1,sticky='news',padx=10,pady=10)
button1.configure(bg="green",fg="white",borderwidth=4)

f2 = tkinter.LabelFrame(frame,text='Retrive Or Delete')
f2.grid(row = 0,column =1,sticky = 'news',padx=20,pady=10)

var_11 = tkinter.Label(f2, text='Reg No. :-')
var_11.grid(row = 1, column = 0)
var_11entry = tkinter.Entry(f2)
var_11entry.grid(row = 1,column = 1)

button2 = tkinter.Button(f2,text="Retrive",command = retrive)
button2.grid(row = 2, column = 0,sticky='news',padx=10,pady=10)

button3 = tkinter.Button(f2,text="Delete",command = delete)
button3.grid(row = 2, column = 1,sticky='news',padx=10,pady=10)
button3.configure(bg="red",fg="white")

display_label = tkinter.Label(f2,relief='raised',border=0,justify='left',anchor=tkinter.W)
display_label.grid(row=3,column=0,columnspan=2)

for widget in f2.winfo_children():
     widget.grid_configure(padx = 10,pady = 5)

display.mainloop()
