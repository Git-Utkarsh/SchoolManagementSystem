# School Management System

The School Management System is a Python program designed to manage various aspects of a school, including admissions, campus facilities, school timings, fee structures, student records, and more. This system is primarily aimed at school administrators, teachers, and staff to streamline and organize school-related tasks.

![Alt text](https://img.lovepik.com/free-png/20210919/lovepik-school-png-image_400499294_wh1200.png)

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#Contributors)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **Admission Availability Check**: 
   - Users can check if there are available admission slots for a specific class.
   - If admission is available, students are prompted to enter their entrance exam marks to determine eligibility.

2. **Campus & Facility Information**:
   - Provides information about the various facilities available on the school campus, such as labs, classrooms, library, IT lab, and sports rooms.

3. **School Timings**:
   - Displays the school timings for different classes, including summer and winter schedules.

4. **Fee Structure**:
   - Shows the fee structure for each class from 1 to 12, including admission fees and transport fees.

5. **Entrance System**:
   - Includes an entrance system with options to:
     - Add student details to the database.
     - Display records class-wise.
     - Edit and update student records.
     - Delete student records.
     - Search for specific student records.
     - Display the full database of student records.

6. **Banner Display**:
   - Presents visually appealing banners at the start of the program to create a school-themed user interface.
7. **Teacher Management**:
   - A teacher management system where we can add edit and remove teachers (Only in version V2)

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.x installed on your system.
- MySQL database server installed and running.
- Required Python packages (`mysql-connector-python` and `tabulate`) installed. You can install them using pip:

## Installation

1. Clone the repository:
```
git clone https://github.com/Git-Utkarsh/SchoolManagementSystem.git
```

2. Install the rquired modules
```pip
pip install -r requirements.txt
```

3. Create a MySQL database named `schooldb`:

```sql
mysql > create database if not exists schooldb;
mysql > use schooldb;
mysql > create table class(Reg int(20) primary key NOT NULL, Name Varchar(30) NOT NULL, Class Varchar(12) NOT NULL,
      > Sec Varchar(5) NOT NULL,Phone Varchar(20) NOT NULL,Father Varchar(30) NOT NULL,
      > Mother Varchar(30) NOT NULL ,Address Varchar(40) NOT NULL);

mysql > create table teacher(ID int(20) primary key NOT NULL, Name Varchar(30) NOT NULL, Subject Varchar(12) NOT NULL,
      > Phone Varchar(20) NOT NULL, Salary Varchar(20));
```

4. Update the database credentials in the code. You can change the host, user, and password in the `connection` line:

   ```python
   connection = sql.connect(host="localhost", user="root", passwd="root", database="schooldb")
   ```

## Usage

1. **Run the Program**:
   - Run the program using a Python interpreter. The program will start with a menu displaying various options.
   ```run
   python student_management.py
   ```

2. **Navigation**:
   - Use the numeric keys to navigate through the menu and perform different operations.
   - Follow the on-screen instructions to input data and interact with the system.

3. **Exit**:
   - You can exit the program at any time by selecting the "Exit" option from the menu.

## Contributors

- [Git-Utkarsh](https://github.com/Git-Utkarsh)
- [Ssp-coder](https://github.com/Ssp-coder)
- [SaurabhK2608](https://github.com/SaurabhK2608)
- [PULLAAA](https://github.com/PULLAAA)


## Development
If you want to contribute to this project, follow these steps:

- Fork the repository on GitHub.
- Clone your forked repository to your local machine.
- Create a new branch for your feature or bug fix.
- Make your changes and test thoroughly.
- Commit your changes and push them to your GitHub fork.
- Create a pull request to the original repository, explaining your changes and improvements.

## Contributing
Contributions to this project are welcome! If you have any ideas, bug fixes, or improvements, please open an issue or submit a pull request.


## License
This School Management System is open-source software released under the [MIT License](https://github.com/Git-Utkarsh/SMSProject/blob/main/LICENSE). You are free to use, modify, and distribute this software in accordance with the license terms.
