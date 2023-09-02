# Database query 
# mysql > create database if not exists schooldb
# mysql > create table class(Reg int(20) primary key NOT NULL, Name Varchar(30) NOT NULL, Class Varchar(12) NOT NULL,Sec Varchar(5) NOT NULL,
#         Phone Varchar(20),Father Varchar(30),
#         Mother Varchar(30),Address Varchar(40));
# mysql > insert into class(Reg,Name,Class,Sec,Phone,Father,Mother,Address) Values
#     (1,"Name",11,"PCM",1234123412,"Father","Mother","Mars");
import mysql.connector as sql
from tabulate import tabulate #pip install tabulate
connection = sql.connect(host="localhost",user="root",passwd="root",database="schooldb")
cursor = connection.cursor()

def start():
    print("""

    Choose the operation you want to perform 

    1.Check admission avalibility
    2.Show Fee structure
    3.Show School Management information
    4.Entrance status
    5.Exit

    """)
    inp = int(input("Select option :"))
    if inp==1:
        admission_ava()
    elif inp==2:
        pass
    elif inp==3:
        pass
    elif inp==4:
        entrance_system()
    elif inp==5:
        exit()
    else:
        print("[-] Select Valid option !!")

def admission_ava():
    """
    This fucntions checks that in a class if number of student is less than 40 
    Then only admission is possible else
    Admission will be not possible
    """
    ad_check = int(input("In which class you want to get admission (11-12):"))
    if ad_check == 11:
        cursor.execute('Select count(Class) "Class" from class Where Class=11')
        row = cursor.fetchone()
        print("Number of students in class 11 is",row[0])
        if row[0] < 40:
            print("Admission is available")
        else:
            print("Admission is not available") 
    elif ad_check ==12:
        cursor.execute('Select count(Class) "Class" from class Where Class=12')
        row = cursor.fetchone()
        print("Number of students in class 12 is",row[0])
        if row[0] < 40:
            print("Admission is available")
        else:
            print("Admission is not avalible") 

def disply_rec():
    """
    This function use tabulate module to create table while 
    retriving the data from the table
    """
    clas = input("Enter the class whose data you want to retrive:")
    cursor.execute('Select * from class where Class='+str(clas))
    row = cursor.fetchall()
    head = ["Reg", "Name","Class","Section","Phone","Father","Mother","Address"]
    print(tabulate(row, headers=head, tablefmt="grid"))

def delete():
    var_data_11 = int(input("Enter the registration number whose data you want to delete:"))
    sql1 = "DELETE FROM class WHERE Reg='%s'"
    data1=(var_data_11,)
    cursor.execute(sql1,data1)
    connection.commit()
    print('Deleted successfully')

def search():
    var_data_11 = int(input("Enter the registration number whose data you want to Find:"))
    cursor.execute("SELECT * FROM class WHERE Reg='%s'",(var_data_11,))  
    data = cursor.fetchall()
    head = ["Reg", "Name","Class","Section","Phone","Father","Mother","Address"]
    print(tabulate(data, headers=head, tablefmt="grid"))


def add_student():
    Reg = input("Enter Student's Registration number :")
    Name =input("Enter Student's Name:")
    Class = input("Enter Student's Class:")
    Section =input("Enter Student's Section:")
    Phone =input("Enter Student's Phone Number:")
    Father =input("Enter Student's Father's Name:")
    Mother =input("Enter Student's Mother's Name:")
    Address =input("Enter Student's Address:")
    query = """INSERT INTO class(Reg,Name,Class,Sec,Phone,
    Father,MOther,Address) VALUES({},'{}','{}','{}','{}','{}','{}','{}')""".format(Reg,Name,Class,Section,Phone,Father,Mother,Address)
    cursor.execute('Select * from class where Reg='+str(Reg))
    row = cursor.fetchall()
    try:
        if row == []:
            cursor.execute(query)
            connection.commit()
            print("[+] Data Entered Successfully !!")
        else:
            print("[-] ERROR Registration number already exists in the database !!!")
            print("Make Sure Your Registration number is unique ")
    except:
        print("[ERROR] \n Make sure to Enter all the required data !!!")

    
def entrance_system():
    print("""
        This is Student Entrance System
        
        Select operation you want to perform
          
        1.Add Student Details in Database
        2.Disply Record Class Wise
        3.Edit Record
        4.Delete Record
        5.Search Record
        6.Back
""")
    option = int(input("Select option:"))
    if option== 1:
        add_student()
    elif option==2:
        disply_rec()
    elif option==3:
        pass
    elif option==4:
        delete()
    elif option==5:
        search()
    elif option==6:
        start()
    else:
        pass
while True:
    start()
    input("Press Enter to continue. . .")
