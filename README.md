🍽️ Terminal-Based Food Ordering System
A Python + MySQL terminal application for managing food orders. Built for admin and user interactions, where the admin can manage menu items and users can register, log in, and place food orders.

📌 Features
👨‍🍳 Admin Panel:
Secure login (name: aditi, password: 0602)

View current menu

Add new food items to the menu

Delete food items from the menu

View all orders and total revenue

🙋 User Panel:
Register with name, email, phone number, and password

Login with email and password

View menu and order items

Automatically adds selected items to the database

View final bill after placing an order

🗃️ Database Schema
user Table
Column	Type
name	VARCHAR(100)
email	VARCHAR(100)
phone_no	VARCHAR(15)
password	VARCHAR(15)

menu Table
Column	Type
item_name	VARCHAR(50)
price	INT

orders Table
Column	Type
item_name	VARCHAR(50)
price	INT

⚙️ How to Run
Install MySQL Server and Python

Create Database

sql
Copy
Edit
CREATE DATABASE food_center;
Clone this Repository

bash
Copy
Edit
git clone https://github.com/yourusername/food-ordering-system.git
cd food-ordering-system
Install Required Python Modules

bash
Copy
Edit
pip install mysql-connector-python
Run the Application

bash
Copy
Edit
python food_order.py
Make sure your MySQL server is running and the credentials in the code (user='root', password='root') match your system.

🧾 Sample Admin Credentials
Name: aditi

Password: 0602

🛡️ Security Notes
Passwords are entered securely using getpass.

Email and phone number validation is implemented.

Uses prepared statements to prevent SQL injection.

