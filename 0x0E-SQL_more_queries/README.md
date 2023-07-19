# SQL Operators

The `WHERE` clause uses operators to construct conditions. Some of the commonly used operators are:

**1. Equal to Operator (=)**

```sql
-- select all columns from Customers table with first name 'John'
SELECT *
FROM Customers
WHERE first_name = 'John';
```

[Run Code](https://www.programiz.com/sql/online-compiler)

**2. Greater than (>)**

```sql
-- select all columns from Customers table with age greater than 25
SELECT *
FROM Customers
WHERE age > 25;
```

[Run Code](https://www.programiz.com/sql/online-compiler)

**3. AND Operator (AND)**

```sql
-- select all columns from Customers table with last_name 'Doe' and country 'USA'
SELECT *
FROM Customers
WHERE last_name = 'Doe' AND country = 'USA';
```

[Run Code](https://www.programiz.com/sql/online-compiler)

### SQL OR Operator

The SQL `OR` operator selects data if any one condition is `TRUE`. For example,

```sql
-- select first and last name of customers
-- who either live in the USA
-- or have the last name 'Doe'

SELECT first_name, last_name
FROM Customers
WHERE country = 'USA' OR last_name = 'Doe';
```

[Run Code](https://www.programiz.com/sql/online-compiler)

### SQL NOT Operator

The SQL `NOT` operator selects data if the given condition is `FALSE`. For example,

```sql
-- select customers who don't live in the USA

SELECT first_name, last_name
FROM Customers
WHERE NOT country = 'USA';
```

[Run Code](https://www.programiz.com/sql/online-compiler)

### Combining Multiple Operators

It is also possible to combine multiple `AND`, `OR` and `NOT` operators in an SQL statement.

For example, let's suppose we want to select customers where country is either **USA** or **UK**, and age is **less than 26**.

```sql
-- select customers who live in either USA or UK and whose age is less than 26

SELECT *
FROM Customers
WHERE (country = 'USA' OR country = 'UK') AND age < 26;
```

[Run Code](https://www.programiz.com/sql/online-compiler)

**The SQL `SELECT DISTINCT` statement retrieves distinct values from a database table.**

# SQL DISTINCT Syntax

The syntax of the SQL `DISTINCT` statement is:

```sql
SELECT DISTINCT column1, column2 ...
FROM table;
```

Here,

- `column1, column2, ...` are the table columns
- `table` is the table name from where we retrieve the distinct columns

### **Example**

```sql
-- select the unique ages from the Customers table
SELECT DISTINCT age
FROM Customers;
```

[Run Code](https://www.programiz.com/sql/online-compiler)

**Here, the SQL command selects only the unique values of age from the Customers table.**

# DISTINCT With COUNT

If we need to count the number of unique rows, we can use the `COUNT()` function with `DISTINCT`.

```sql
-- count the unique countries where customers are from
SELECT COUNT(DISTINCT country)
FROM Customers;
```

[Run Code](https://www.programiz.com/sql/online-compiler)

# SQL CREATE DATABASE Statement

**The `CREATE DATABASE` statement is the SQL command used to create databases.**

### **Example**

```sql
CREATE DATABASE my_db;
```

**Here, the SQL command creates a database named my_db.**

---

# SQL CREATE DATABASE Syntax

The syntax of the SQL `CREATE DATABASE` statement is:

```sql
CREATE DATABASE DB_NAME;
```

Here,

- `CREATE DATABASE` command creates a database
- `DB_NAME` is the name of the database created

# CREATE DATABASE IF NOT EXISTS

If a database already exists, SQL will throw an error while creating another database of the same name.

In such situations, we can use the `CREATE DATABASE IF NOT EXISTS` statement to create a database only if there is no existing database with the same name. For example,

```sql
CREATE DATABASE IF NOT EXISTS my_db;
```

Here, the SQL command creates a database named my_db only if there is no existing database with the same name.

# List all Databases

There could be multiple databases in a database management system. To show the list of databases, we can run the following statement.

```sql
SHOW DATABASES;
```

Here, the SQL command lists all the available databases in the DBMS.

# Switch Databases

We often have to work with multiple databases. To switch between available databases, we can run the following statement.

```sql
USE my_db;
```

This code selects the my_db database, and all SQL operations will be performed inside this database.

**A database table is used to store records (data). To create a database table, we use the SQL `CREATE TABLE` statement.**

### **Example**

```sql
-- create a table Companies with name, id, address, email, and phone number
CREATE TABLE Companies (
  id int,
  name varchar(50),
  address text,
  email varchar(50),
  phone varchar(10)
);
```

[Run Code](https://www.programiz.com/sql/online-compiler)

**Here, the SQL command creates a table named Companies with the columns: id, name, address, email, and phone.**

# CREATE TABLE Syntax

The syntax of the SQL `CREATE TABLE` statement is:

```sql
CREATE TABLE table_name(
column1 data type, column2 data type, ...
);
```

Here,

- `table_name` is the name of the table
- `column1, column2, ...` are the names of the columns in the table
- `data type` is the column's data type (can be an integer, string, date, etc.)

Here, `int`, `varchar(50),` and `text` are data types that tell what data could be stored in that field. Some commonly used data types are as follows:

| Data Type | Description | Example |  |
| --- | --- | --- | --- |
| int | can store numbers | 400, -300 |  |
| varchar(x) | can store variable characters with a maximum length of x | John Doe, United States of America |  |
| text | can store texts up to 65535 characters | This is a really long paragraph that can go over lines. |  |

# CREATE TABLE IF NOT EXISTS

You will get an error if you create a table with the same name as an existing table. To fix this issue, we can add the optional `IF NOT EXISTS` command while creating a table.

For example,

```sql
-- create a Companies table if it does not exist
CREATE TABLE IF NOT EXISTS Companies (
  id int,
  name varchar(50),
  address text,
  email varchar(50),
  phone varchar(10)
);
```

[Run Code](https://www.programiz.com/sql/online-compiler)

# CREATE TABLE AS

We can also create a table using records from any other existing table using the `CREATE TABLE AS` command. For example,

```sql
-- create a table by copying those records
-- from Costomers table with country name USA
CREATE TABLE USACustomers
AS (
  SELECT *
  FROM Customers
  WHERE country = 'USA'
);
```

Here, the SQL command creates a table named USACustomers and copies the records of the nested query into the new table.

# SQL DROP DATABASE Statement

**In SQL, `DROP DATABASE` is used to delete a database from our Database Management System.**

### **Example**

```
DROP DATABASE my_database;
```

**Here, the SQL command will delete a database named my_database.**

**Also, you need admin or DROP permission to run this command.**

---

# DROP DATABASE Syntax

The syntax of the SQL `DROP DATABASE` statement is:

```sql
DROP DATABASE database_name;
```

Here, `database_name` is the name of the database to be removed.

**Note:** When we delete a database, all tables and records within a database are also deleted.

## **SHOW TABLES SYNTAX :**

```sql
SHOW TABLES;
```

# SQL DROP TABLE Statement

**In SQL, `DROP TABLE` is used to delete the tables in our database.**

### **Example**

```sql
-- delete Shippings table
DROP TABLE Shippings;
```

[Run Code](https://www.programiz.com/sql/online-compiler)

**Here, the SQL command will delete a table named Shippings.**

**Also, make sure you have admin or DROP permission to run this command.**

---

# DROP TABLE Syntax

The syntax of the SQL `DROP TABLE` statement is:

```sql
DROP TABLE table_name;
```

Here, `table_name` is the name of the table to be removed.

**Note:** When we delete a database table, all records within the table are also deleted.

---

# DROP TABLE IF EXISTS

If a table does not exist, dropping it will throw an error. To fix this issue, we can add the optional `IF EXISTS` command while dropping a table. For example,

```sql
-- delete Orders table if it exists
DROP TABLE IF EXISTS Orders;
```

[Run Code](https://www.programiz.com/sql/online-compiler)

Here, the SQL command will only drop a table if there exists one with the name Orders.

# SQL ALTER TABLE Statement

**In SQL, the `ALTER TABLE` command is used to modify the structure of an existing table like adding, deleting, renaming columns, etc.**

### **Example**

```sql
-- add phone column to Customers table
ALTER TABLE Customers
ADD phone varchar(10);
```

**Here, the SQL command adds a column named phone to the Customers table.**

# ALTER TABLE Operations

We can perform the following operations on a table using the `ALTER TABLE` command:

- Add a column
- Rename a column
- Modify a column
- Delete a column
- Rename a table

# Add Multiple Columns in a Table

We can also add multiple columns at once to a table. For example,

```sql
-- add phone and age columns to Customers table
ALTER TABLE Customers
ADD phone varchar(10), age int;
```

Here, the SQL command adds the phone and age columns to the Customers table.

**Note:** Since our compiler uses SQLite, it does not support adding multiple columns with `ALTER TABLE`. However, many other database management systems support this command.

# Rename Column in a Table

We can rename columns in a table using the `ALTER TABLE` command with the `RENAME COLUMN` clause. For example,

```sql
-- rename column customer_id to c_id
ALTER TABLE Customers
RENAME COLUMN customer_id TO c_id;
```

Here, the SQL command changes the column name of customer_id to c_id in the Customers table

# Modify the Data Type of a Column

We can also change the column's data type using the `ALTER TABLE` command with `MODIFY` or `ALTER COLUMN` clause. For example,

**SQL Server**

```sql
ALTER TABLE Customers
ALTER COLUMN age VARCHAR(2);
```

**MySQL**

```sql
ALTER TABLE Customers
MODIFY COLUMN age VARCHAR(2);
```

**Oracle**

```sql
ALTER TABLE Customers
MODIFY age VARCHAR(2);
```

**PostgreSQL**

```sql
ALTER TABLE Customers
ALTER COLUMN age TYPE VARCHAR(2);
```

Here, the SQL command changes the data type of the age column to `VARCHAR` in the Customers table.

# Drop Column in a Table

We can also drop (remove) columns in a table using the `ALTER TABLE` command with the `DROP` clause. For example,

```sql
-- delete country column from Customers table
ALTER TABLE Customers
DROP COLUMN country;
```

Here, the SQL command removes the country column from the Customers table.

---

# Rename a Table

We can change the name of a table using the `ALTER TABLE` command with the `RENAME` clause. For example,

```sql
-- rename Customers table to New_customers
ALTER TABLE Customers
RENAME TO New_customers;
```

Here, the SQL command renames the Customers table to New_customers.

# SQL BACKUP DATABASE Statement

**In SQL, the `BACKUP DATABASE` statement is used to create database backups.**

### **Example**

```sql
–- backup database to the given path
BACKUP DATABASE my_db
TO DISK = 'C:\my_db_backup.bak';
```

**Here, the SQL command creates a backup file of the my_db database inside C drive, named my_db_backup.bak.**

---

# Types of Backups in SQL

There are three types of backups in SQL. They are:

- Full Backup
- Differential Backup
- Transaction Log (T-log) backup

---

# Full Backup

A full backup is a complete backup of an SQL server database.

Its syntax is:

```sql
BACKUP DATABASE database_name
TO medium = 'path\file_name';
```

Here,

- `database_name` is the name of the database to be backed up
- `medium` refers to the storage medium such as disk, tape or url
- `path` refers to the folder where the backup file should be stored
- `file_name` is the name given to the backup file

For example,

```sql
–- backup database to the given path
BACKUP DATABASE my_db
TO DISK = 'C:\my_db_backup.bak';
```

Here, the SQL command creates a backup file of the my_db database (named my_db_backup.bak) inside the **C** drive.

**Note:** It's a common convention to use the **.bak** file extension for database backup files, however, it's not mandatory.

---

# Differential Backup

In SQL, you can also backup only the new changes compared to the last full backup by using the `WITH DIFFERENTIAL` command. For example,

```sql
-- backup the changes made to the database
BACKUP DATABASE my_db
TO DISK = 'C:\my_db_backup.bak'
WITH DIFFERENTIAL;
```

Here, the SQL command appends only the new changes to the previous backup file. Hence, this command may work faster.

---

# Transaction Log Backup

A transaction log backup captures all the changes made to the database since the last transaction log backup or the creation of the database.

It allows you to create a point-in-time backup of your database and provides a way to recover the database to a specific point in time in case of a failure.

It's syntax is,

```sql
BACKUP LOG database_name
TO medium = 'path\filename';
```

For example,

```sql
-- backup database log to the given path
BACKUP LOG my_db
TO DISK = 'C:\my_db_backup.bak';
```

---

# Restore Database From Backup

To restore a backup file to a database management system, we can use the `RESTORE DATABASE` command. For example,

```sql
-- restore database from given path
RESTORE DATABASE my_db
FROM DISK = 'C:\my_db_backup.bak';
```

Here, the SQL command restores the my_db_backup.bak file to the database named my_db.

**In SQL, the `INSERT INTO` statement is used to insert new rows in a database table.**

### **Example**

```sql
-- insert a row in the Customers table
INSERT INTO Customers(customer_id, first_name, last_name, age, country)
VALUES
(7, 'Ron', 'Weasley', 31, 'UK');
```

**Here, the SQL command inserts a new row into the Customers table with the given values.**

---

# INSERT INTO Syntax

The syntax of the SQL `INSERT INTO` statement is:

```sql
INSERT INTO table_name(column1, column2, column3, ...)
VALUES
(value11, value12, value13, ...)
(value21, value22, value23, ...)
... ;
```

Here,

- `table_name` is the name of the table into which the rows are to be inserted
- `column1, column2, column3, ...` are the names of columns where the values are to be inserted
- `value11, value12, value13, ...`, `value21, value22, value23, ...` are the values to be inserted

# Insert Multiple Rows at Once in SQL

It's also possible to insert multiple rows to a database table at once. For example,

```sql
INSERT INTO Customers(first_name, last_name, age, country)
VALUES
('Harry', 'Potter', 31, 'USA'),
('Chris', 'Hemsworth', 43, 'USA'),
('Tom', 'Holland', 26, 'UK');
```

Here, the SQL command inserts three rows to the Customers table.

# SQL UPDATE Statement

**The SQL `UPDATE` statement is used to edit an existing row in a database table.**

### **Example**

```sql
-- update a single value in the given row
UPDATE Customers
SET age = 21
WHERE customer_id = 1;
```

**Here, the SQL command changes the value of the age column to 21 if customer_id is equal to 1.**

# UPDATE syntax

The syntax of the SQL `UPDATE` statement is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
[WHERE condition];
```

Here,

- `table_name` is the name of the table to be edited
- `column1, column2, ...` are the names of the columns to be edited
- `value1, value2, ...` are values to be set to the respective columns
- `[...]` signifies that the clause inside is optional
- `condition` is the condition for the values to be changed

# Update Multiple Values in a Row

We can also update multiple values in a single row at once. For example,

```sql
-- update multiple values in the given row
UPDATE Customers
SET first_name = 'Johnny', last_name = 'Depp'
WHERE customer_id = 1;
```

Here, the SQL command changes the value of the first_name column to **Johnny** and last_name to **Depp** if customer_id is equal to **1**.

# Update all Rows

We can update all the rows in a table at once by omitting the `WHERE` clause. For example,

```sql
-- update all rows
UPDATE Customers
SET country = 'NP';
```

# QL SELECT INTO (Copy Table)

**In SQL, the `SELECT INTO` statement is used to copy data from one table to another.**

### **Example**

```sql
-- copy all the contents of a table to a new table
SELECT *
INTO CustomersCopy
FROM Customers;
```

**Here, the SQL command copies all data from the Customers table to the new CustomersCopy table.**

# SELECT INTO Syntax

The syntax of the SQL `SELECT INTO` statement is:

```sql
SELECT column1, column2, column3, ...
INTO destination_table
FROM source_table;
```

Here,

- `column1, column2, column3, ...` are the columns to be copied
- `destination_table` is the new table where the data is to be copied to
- `source_table` is the table where the data is to be copied from

# Copy Selected Columns Only

We can also copy selected columns from the old table to a new table. For example,

```sql
-- copy selected columns only
SELECT customer_id, country
INTO CustomersCountry
FROM Customers;
```

Here, the SQL command only copies the customer_id and country columns to the CustomersCountry table

# Copy Records Matching a Condition

We can use the `WHERE` clause with `SELECT INTO` to copy those rows that match the specified condition. For example,

```sql
-- copy rows where country is USA
SELECT customer_id, age
INTO USACustomersAge
FROM Customers
WHERE country = 'USA';
```

Here, the SQL command

- creates the  table with  and  columns

  USACustomersAge

  customer_id

  age

- copies rows from the `Customers` table if the value of the  column is **USA**

  country

  # Copy to Another Database

  By default, `SELECT INTO` creates a new table in the current database. If we want to copy data to a table in a different database, we can do that by using the `IN` clause. For example,

    ```sql
    -- copy contents of a table to another database
    SELECT *
    INTO CustomersCopy
    IN another_db.mdb
    FROM Customers;
    ```

  Here, the SQL command copies the Customers table to the CustomersCopy table in the another_db.mdb database.

  **Note:** The user must have **WRITE** privilege to copy data to a table in a different database.

  # Copy From Two Tables to One

  We can also copy records from two different tables to a new table using the `JOIN` clause with `SELECT INTO`. For example,

    ```sql
    -- copy rows from Customers and Orders tables
    SELECT Customers.customer_id, Customers.first_name, Orders.amount
    INTO CustomerOrders
    FROM Customers
    JOIN Orders
    ON Customers.customer_id = Orders.customer_id;
    ```

  Here, the SQL command copies customer_id and first_name from the Customers table and amount from the Orders table to a new table CustomerOrders.
    
  ---

  # Copy Table Schema Only

  We can also use the `SELECT INTO` statement to create a new table with the given structure (without copying the data). For that, we use the `WHERE` clause with a condition that returns `false`.

    ```sql
    -- copy table structure only
    SELECT *
    INTO NewCustomers
    FROM Customers
    WHERE false;
    ```

  Here, the SQL command creates an empty table named NewCustomers with the same structure as the Customers table.

  # SQL INSERT INTO SELECT Statement

  **The SQL `INSERT INTO SELECT` statement is used to copy records from one table to another existing table.**

  ### **Example**

    ```sql
    -- copy data to an existing table
    INSERT INTO OldCustomers
    SELECT *
    FROM Customers;
    ```

  **Here, the SQL command copies all records from the Customers table to the**

  To list all privileges of MySQL users, you can use the following SQL query:

    ```sql
    SHOW GRANTS FOR 'username'@'localhost';
    
    ```

  Replace 'username' with the username of the user whose privileges you want to list. If you want to list the privileges for all users, you can run the following query:

    ```sql
    SELECT * FROM mysql.user;
    
    ```

  This will display a table containing all user accounts and their associated privileges.