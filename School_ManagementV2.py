#School Management System
import mysql.connector as sql #pip install mysql-connector-python
from tabulate import tabulate #pip install tabulate
connection = sql.connect(host="localhost",user="root",passwd="root",database="schooldb")
cursor = connection.cursor()

def banner_1():
    print("""
 __________________________________________________________________________________________________________________________________________       
|   _____      _                 _   __  __                                                   _      _____           _                     |
|  / ____|    | |               | | |  \/  |                                                 | |    / ____|         | |                    |
| | (___   ___| |__   ___   ___ | | | \  / | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_  | (___  _   _ ___| |_ ___ _ __ ___      |
|  \___ \ / __| '_ \ / _ \ / _ \| | | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|  \___ \| | | / __| __/ _ \ '_ ` _ \     |
|  ____) | (__| | | | (_) | (_) | | | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_   ____) | |_| \__ \ ||  __/ | | | | |    |
| |_____/ \___|_| |_|\___/ \___/|_| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__| |_____/ \__, |___/\__\___|_| |_| |_|    |
|                                                              __/ |                                        __/ |                          |
|                                                             |___/                                        |___/                           |
|__________________________________________________________________________________________________________________________________________|

                    """)

def banner_2():
    print("""
      ______       _                               _____           _                 
     |  ____|     | |                             / ____|         | |                
     | |__   _ __ | |_ _ __ __ _ _ __   ___ ___  | (___  _   _ ___| |_ ___ _ __ ___  
     |  __| | '_ \| __| '__/ _` | '_ \ / __/ _ \  \___ \| | | / __| __/ _ \ '_ ` _ \ 
     | |____| | | | |_| | | (_| | | | | (_|  __/  ____) | |_| \__ \ ||  __/ | | | | |
     |______|_| |_|\__|_|  \__,_|_| |_|\___\___| |_____/ \  / |___/\__\___|_| |_| |_|
                                                      __/ /                     
                                                     |___/                      
""")

def add_teacher():
    """This Function is used to add the data to the sql database
    
    """
    ID = input("Enter Teacher ID :")
    Name =input("Enter Teacher's Name:")
    Subject = input("Enter Teacher's Subject:")
    Phone =input("Enter Teacher's Phone Number:")
    Salary =input("Enter Teacher's Salary:")
    query = """INSERT INTO teacher(ID,Name,Subject,Phone,
    Salary) VALUES({},'{}','{}','{}','{}')""".format(ID,Name,Subject,Phone,Salary)
    cursor.execute('Select * from teacher where ID='+str(ID))
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

def teacher_data():
    """
    Teachers data
    """
    cursor.execute('SELECT * FROM teacher ORDER BY ID ASC')
    row = cursor.fetchall()
    head = ["ID", "Name","Subject","Phone","Salary"]
    print(tabulate(row, headers=head, tablefmt="grid"))

def delete_teacher():
    """
    delete teacher
    """
    var_data_11 = int(input("Enter the teacher ID whose data you want to delete:"))
    sql1 = "DELETE FROM teacher WHERE ID='%s'"
    data1=(var_data_11,)
    cursor.execute(sql1,data1)
    connection.commit()
    print('Deleted successfully')

def teacher_search():
    try:
        ID = int(input("Enter the teacher ID whose data you want to Find:"))
    except NameError:
          print("[-] Error!! Option must be integer type")
    cursor.execute("SELECT * FROM teacher WHERE ID='%s'",(ID,))  
    data = cursor.fetchall()
    if data==[]:
         print("No data found !!")
    else:
        head = ["ID", "Name","Subject","Phone","Salary"]
        print(tabulate(data, headers=head, tablefmt="grid"))


def teachersys():
        table = tabulate([
        [1,"Add Teacher in Database"],
        [2,"Show full database"],
        [3,"Delete Record"],
        [4,"Search Record"],
        [5,"Back"]
        ],['No.','Operation'],'outline')
        print(table)
        inp = int(input("Select option :"))
        try:
            if inp==1:
                add_teacher()
            elif inp==2:
                teacher_data()
            elif inp==3:
                delete_teacher()
            elif inp==4:
                teacher_search()
            elif inp==5:
                start()
            else:
                print("[-] Select Valid option !!")
        except:
          print("[-]Error!! Option must be integer type")           
        

def start():
    """
    From here the program starts

    """
    banner_1()
    table = tabulate([
        [1,"Check admission avalibility"],
        [2,"Campus & Facility"],
        [3,"School Timings"],
        [4,"Show Fee structure"],
        [5,"School Management"],
        [6,"Entrance status"],
        [7,"Exit"]
        ],['No.','Operation'],'outline')
    
    print(table)

    try:
        inp = int(input("Select option :"))
        if inp==1:
                admission_ava()
        elif inp==2:
             campus_facility()
        elif inp==3:
                time_table()
        elif inp==4:
                fee_details()
        elif inp==5:
                teachersys()
        elif inp==6:
                while True:
                        entrance_system()
        elif inp==7:
             exit()
        else:
                print("[-] Select Valid option !!")
    except ValueError:
         print("[-]Error!! Option must be integer type")


def campus_facility():
    """
    This fucntion give the information about the campus and facilities
    
    """
    camp = tabulate([
          ["Labs"],
          ["Classroom"],
          ["Library"],
          ["IT Lab"],
          ["Sports Room"]
    ],["CAMPUS & FACILITY"],'outline')
    print(camp)

def time_table():
    """
    This fucntion shows the school timing of the students from Class I to Class XII.
    
    """
    Time = tabulate([
        ["I and Class II","09:00 a.m to 01:00 p.m.","10:00 a.m to 02:00 p.m."],
        ["Classes III to XII","08:00 a.m to 02:00 p.m.","09:00 a.m to 03:00 p.m."]
    ],["CLASS","SUMMER","WINTER"],'outline')
    print(Time)

def marks():
    """
    This fucntion checks the marks obtained by the candidate in the entrance exam.

    If marks is greater then 40 then entrance_system fucntion is executed
    """
    n=float(input("Enter the percentage student got in the entrance exam:"))
    if n>=40:
        entrance_system()
    else:
          print("Sorry !! But You are failed We can't admit you in our school")

def check(class_):
    """
    This function performs the check using SQL count method
    
    """
    cl = int(class_)
    cursor.execute('Select count(Class) "Class" from class Where Class='+str(cl))
    row = cursor.fetchone()
    print("Number of students in class ",cl," is",row[0])
    if row[0] < 40:
        print("Admission is available")
        marks()
    else:
        print("Admission is not avalible")

def admission_ava():

    """
    This fucntions checks that in a class if number of student is less than 40 
    
    Then only admission is possible else
    Admission will be not possible
    """
    try:
        ad_check = int(input("In which class you want to get admission (1-12):"))
        if ad_check<=12 and ad_check>0:
            check(ad_check)
        else:
            print("[-]Enter valid option")
    except NameError:
        print("[-]Error!! Option must be integer type")


def fee_details():
    """
    Print Fee details of each class from 1 to 12
    
    """
    print(tabulate([
        [1,2500,120,2620],
        [2,2700,120,2820],
        [3,2900,120,3020],
        [4,3100,120,3220],
        [5,3300,120,3420],
        [6,3600,150,3750],
        [7,3800,150,3950],
        [8,4000,150,4150],
        [9,4300,170,4470],
        [10,4600,170,4770],
        [11,5000,200,5200],
        [12,5500,250,5750]

        ],['Class','Admission Fees','Transport Fees','Total Fee'],'outline'))

def disply_rec():
    """
    This function use tabulate module to create table
    
    while retriving the data from the table
    """
    try:
        clas = int(input("Enter the class whose data you want to retrive:"))
    except NameError:
          print("[-] Error!! Option must be integer type")
    if clas<=12 and clas>0:
        cursor.execute('Select * from class where Class='+str(clas))
        row = cursor.fetchall()
        head = ["Reg", "Name","Class","Section","Phone","Father","Mother","Address"]
        print(tabulate(row, headers=head, tablefmt="grid"))
    else:
         print("[-] Error Occured! Enter Valid class")

def delete():
    """
    This function take registration number as input and
    
    delete the corresponding record from the database
    """
    var_data_11 = int(input("Enter the registration number whose data you want to delete:"))
    sql1 = "DELETE FROM class WHERE Reg='%s'"
    data1=(var_data_11,)
    cursor.execute(sql1,data1)
    connection.commit()
    print('Deleted successfully')

def search():
    """
    This Function search record
    
    from the data base using Registration number
    """
    try:
        clas = int(input("Enter the registration number whose data you want to Find:"))
    except NameError:
          print("[-] Error!! Option must be integer type")
    cursor.execute("SELECT * FROM class WHERE Reg='%s'",(clas,))  
    data = cursor.fetchall()
    if data==[]:
         print("No data found !!")
    else:
        head = ["Reg", "Name","Class","Section","Phone","Father","Mother","Address"]
        print(tabulate(data, headers=head, tablefmt="grid"))


def add_student():
    """This Function is used to add the data to the sql database
    
    """
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

    
def edit_rec():
    """
    This function will update values of a particular
    
    record in the database using SQL's UPDATE keyword
    """
    full_data()
    ed = int(input("Enter the registration no. of the student whose record you want to edit:"))
    print("\n\n You Selected ===> ")
    cursor.execute("SELECT * FROM class WHERE Reg='%s'",(ed,))  
    data = cursor.fetchall()
    head = ["Reg", "Name","Class","Section","Phone","Father","Mother","Address"]
    print(tabulate(data, headers=head, tablefmt="grid"))
    print("""
          
    \t \t \t Which field you want to edit 
          
1.Name  2.Class  3.Section 4.Phone 5.Father's Name 6.Mother's Name 7.Address 8.Back
          
          """)
    inp = int(input("Select the option :"))
    if inp==1:
        name=input("Enter the new name :")
        cursor.execute("UPDATE class set Name=%s WHERE Reg='%s'",(name,ed,))  
        connection.commit()
    if inp==2:
        Class=input("Enter the new Class :")
        cursor.execute("UPDATE class set Class=%s WHERE Reg='%s'",(Class,ed,))  
        connection.commit()
    elif inp==3:
        Section=input("Enter the new Section :")
        cursor.execute("UPDATE class set Sec=%s WHERE Reg='%s'",(Section,ed,))  
        connection.commit()
    elif inp==4:
        Phone=input("Enter the new Phone.no :")
        cursor.execute("UPDATE class set Phone=%s WHERE Reg='%s'",(Phone,ed,))  
        connection.commit()
    elif inp==5:
        Father=input("Enter the new Father's name :")
        cursor.execute("UPDATE class set Father=%s WHERE Reg='%s'",(Father,ed,))  
        connection.commit()
    elif inp==6:
        Mother=input("Enter the new Mother's name :")
        cursor.execute("UPDATE class set Mother=%s WHERE Reg='%s'",(Mother,ed,))  
        connection.commit()
    elif inp==7:
        Address=input("Enter the new Address :")
        cursor.execute("UPDATE class set Address=%s WHERE Reg='%s'",(Address,ed,))  
        connection.commit()
    elif inp==8:
         entrance_system()
    else:
        print("[-] Error Occured")

def full_data():
    """
    This Function prints all the record from the database in ascending order
    
    """
    cursor.execute('SELECT * FROM class ORDER BY Reg ASC')
    row = cursor.fetchall()
    head = ["Reg", "Name","Class","Section","Phone","Father","Mother","Address"]
    print(tabulate(row, headers=head, tablefmt="grid"))

def entrance_system():
    banner_2()
    table = tabulate([
        [1,"Add Student Details in Database"],
        [2,"Disply Record Class Wise"],
        [3,"Edit Record"],
        [4,"Delete Record"],
        [5,"Search Record"],
        [6,"Show full Database"],
        [7,"Back"]
        ],['No.','Operation',],'outline')
    print(table)
    option = int(input("Select option:"))
    if option== 1: 
        add_student()
        input("Press Enter to continue. . .")
    elif option==2:
        disply_rec()
        input("Press Enter to continue. . .")
    elif option==3:
        edit_rec()
        input("Press Enter to continue. . .")
    elif option==4:
        delete()
        input("Press Enter to continue. . .")
    elif option==5:
        search()
        input("Press Enter to continue. . .")
    elif option==6:
        full_data()
        input("Press Enter to continue. . .")
    elif option==7:
        start()
    else:
        pass

if __name__ == '__main__':
    while True:
        start()
        input("Press Enter to continue. . .")
