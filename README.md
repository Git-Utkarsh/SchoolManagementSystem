# Student Management System

![Alt text](https://img.lovepik.com/free-png/20210919/lovepik-school-png-image_400499294_wh1200.png)

This Python program is a simple student management system that allows users to perform various operations related to student information and school management. It uses MySQL as the database to store student records and other related information.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Features

The Student Management System provides the following features:

1. **Check Admission Availability**: Users can check if admission is available for a specific class (9-12). It checks if the number of students in a class is less than 40.

2. **Show Fee Structure**: Display the fee structure for classes from 1 to 12, including admission fees, transport fees, and total fees.

3. **Display School Management Information**: This feature is a placeholder and can be expanded to display school management information.

4. **Entrance Status**: Enter the student entrance system, which allows you to add, display, edit, delete, search, and show the full database of student records.

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

4. Create a MySQL database named `schooldb` and update the database credentials in the code. You can change the host, user, and password in the `connection` line:

```sql
mysql > create database if not exists schooldb;
mysql > use schooldb;
mysql > create table class(Reg int(20) primary key NOT NULL, Name Varchar(30) NOT NULL, Class Varchar(12) NOT NULL,
      > Sec Varchar(5) NOT NULL,Phone Varchar(20) NOT NULL,Father Varchar(30) NOT NULL,
      > Mother Varchar(30) NOT NULL ,Address Varchar(40) NOT NULL);
```

4. Create a MySQL database named `schooldb` and update the database credentials in the code. You can change the host, user, and password in the `connection` line:

```python
connection = sql.connect(host="localhost", user="root", passwd="root", database="schooldb")
```

## Usage
```run
python student_management.py
```

## Development
If you want to contribute to this project, follow these steps:

1.Fork the repository on GitHub.
2.Clone your forked repository to your local machine.
3.Create a new branch for your feature or bug fix.
4.Make your changes and test thoroughly.
5.Commit your changes and push them to your GitHub fork.
6.Create a pull request to the original repository, explaining your changes and improvements.

## Contributing
Contributions to this project are welcome! If you have any ideas, bug fixes, or improvements, please open an issue or submit a pull request.

## license
This project is licensed under the MIT License. See the [license](https://github.com/Git-Utkarsh/SMSProject/blob/main/LICENSE)
 file for details.
