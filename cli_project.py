#School Management Systemmmm!!
import mysql.connector as sql #pip install mysql-connector-python
from tabulate import tabulate #pip install tabulate
connection = sql.connect(host="localhost",user="YOU_SQL_USERNAME",passwd="<YOU_PASSWORD>",database="schooldb")
cursor = connection.cursor()

def banner():
    print("""
___________________________________________________________________________________________________________________________________________        
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

def start():
    banner()
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
        fee_details()
    elif inp==3:
        pass
    elif inp==4:
        while True:
            entrance_system()
    elif inp==5:
        exit()
    else:
        print("[-] Select Valid option !!")


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
    else:
        print("Admission is not avalible")

def admission_ava():
    """
    This fucntions checks that in a class if number of student is less than 40 
    Then only admission is possible else
    Admission will be not possible
    """
    
    ad_check = int(input("In which class you want to get admission (1-12):"))
    if ad_check<=12 and ad_check>0:
        check(ad_check)
    else:
        print("[-]Enter valid option")


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
    This function use tabulate module to create table while 
    retriving the data from the table
    """

    clas = input("Enter the class whose data you want to retrive:")
    cursor.execute('Select * from class where Class='+str(clas))
    row = cursor.fetchall()
    head = ["Reg", "Name","Class","Section","Phone","Father","Mother","Address"]
    print(tabulate(row, headers=head, tablefmt="grid"))

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
    This Function search record from the data base using
    Registration number
    """

    var_data_11 = int(input("Enter the registration number whose data you want to Find:"))
    cursor.execute("SELECT * FROM class WHERE Reg='%s'",(var_data_11,))  
    data = cursor.fetchall()
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
          
    "\t \t Which field you want to edit "
          
    "\t1.Name  2.Class  3.Section 4.Phone 5.Father's Name 6.Mother's Name 7.Address""")
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
    else:
        print("[+] Modified Successfully")

def full_data():
    """
    This Function prints all the record from the database in ascending order
    """
    cursor.execute('SELECT * FROM class ORDER BY Reg ASC')
    row = cursor.fetchall()
    head = ["Reg", "Name","Class","Section","Phone","Father","Mother","Address"]
    print(tabulate(row, headers=head, tablefmt="grid"))

def entrance_system():
    print("""
        This is Student Entrance System
        
        Select operation you want to perform
          
        1.Add Student Details in Database
        2.Disply Record Class Wise
        3.Edit Record
        4.Delete Record
        5.Search Record
        6.Show full Database
        7.Back
""")
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
