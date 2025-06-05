# Required modules for database and password input
import mysql.connector
import getpass
 # Class for Food Ordering System
class food:
    def __init__(self):
        self.db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="food_center",
            auth_plugin="mysql_native_password"
        )
         # Creating cursor object for executing SQL queries
        self.my_cursor=self.db.cursor()
        self.create_tables()

    def create_tables(self):
        
        self.my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            phone_no VARCHAR(15),
            password VARCHAR(15)
                            
        )""")   
        self.my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu(
           item_name VARCHAR(50),
            price INT                                             
        )""")   

        self.my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            item_name VARCHAR(50),
            Price INT
        )""")
        self.db.commit()

    def Admin_login(self):
        self.name = input("Enter name : ")
        if self.name.lower() == "aditi":
            password = getpass.getpass("Enter password : ")
            if password == "0602":
                print("                            ")
                print("-----------> Welcome Admin<---------------")
                while(True):
                    print("                                                         ")
                    print(" 1:display item\n 2:Add items\n 3:Remove items\n 4:Order list\n 5:Exit")
                    print("                                                           ")
                    choice=int(input("---------> Enter Your Choice<------------"))
                    if choice==1:
                        self.display_menu()
                    elif choice==2:
                        self.add_items() 
                    elif choice==3:
                        self.delete_item()
                    elif choice==4:
                        self.order_list()
                    elif choice==5:
                        break
                    else:
                        print("-----------> Invalid Choice <---------------")               
            else:
                print("---------------> Incorrect Password <---------------")    
        else:
            print("-----> Enter valid-name <------")

    def display_menu(self):
        print("\n---- Current Menu ----")
        print("                              ")
        self.my_cursor.execute("SELECT * FROM menu")
        menu_items = self.my_cursor.fetchall()
        if not menu_items:
            print("Menu is empty.")
            return
        for i, (item, price) in enumerate(menu_items, start=1):
            print(f"{i}. {item} - Rs.{price}")
    
    def add_items(self):
        item_name = input("Enter item name: ")
        try:
            price = int(input("Enter price: "))
        except ValueError:
            print("Invalid price.")
            return
        self.my_cursor.execute("INSERT INTO menu (item_name, price) VALUES (%s, %s)", (item_name, price))
        self.db.commit()
        print(f"Item '{item_name}' added successfully.")

    
    def delete_item(self):
        self.display_menu()
        item_name = input("Enter item name to delete: ")
        self.my_cursor.execute("DELETE FROM menu WHERE item_name=%s", (item_name,))
        self.db.commit()
        print(f"Item '{item_name}' deleted successfully.")

    def order_list(self):
        print("\n---- Order List ----")
        self.my_cursor.execute("SELECT * FROM orders")
        orders = self.my_cursor.fetchall()
        if not orders:
            print("No orders yet.")
            return
        total = 0
        for item_name, price in orders:
            print(f"{item_name} - Rs.{price}")
            total += price
        print(f"Total Revenue: Rs.{total}")
    

    def user_register(self):

        name=input("Enter your name to register:")
        if name.isdigit():
            print("enter valid name")
            return
        
        mail=input("enter your E-mail")
        if "@gmail.com" not in mail:
            print("Enter Valid E-mail")
            return
        
        phone_no=input("enter your phone number")
        if not phone_no.isdigit() or len(phone_no)!=10:
            print("enter valid 10 digit phone no")
            return
            
        #check email/no is already exist
        self.my_cursor.execute("select * from user where email=%s or phone_no=%s",(mail,phone_no))
        if self.my_cursor.fetchone():
            print(" -------->  This E-mail or phone no is already registered  <--------- ")
            return
        
        password=getpass.getpass("Create pass.......: ")

        self.my_cursor.execute("INSERT into user (name,email,phone_no,password) values(%s, %s, %s, %s)",(name,mail,phone_no,password))
        self.db.commit()
        print("your register is completly successfully")

    def user_login(self):
            email=input("enter your email:")
            if "@gmail.com" not in email:
              print("  ------>  Enter valid E-mail  <-------  ")
              return
            result=self.my_cursor.fetchall()
        
            password=getpass.getpass("Enter your password:")
            self.my_cursor.execute("select * from user where email=%s and password=%s ", (email,password)) 
            result=self.my_cursor.fetchall()  
            if result:
                print("             ")
                print("---> Welcome foodies <---")
                while (True):
                        print("                          ")
                        print(" 1:Display_items \n 2:Exit")
                        print("                        ")
                        choice=input("enter your choice")
                        if choice=='1':
                            self.display_items()
                        elif choice=='2':
                            break
                        else:
                            print("------------> Invalid choice,try again <--------------------")    
            else:
             print("--------->login failed: incorrect email/phome_no or pass<------------")

    def display_items(self):
        print("\n---Welcome to our Restaurant. Here's the Menu ---")
        print("                                                  ")
        self.my_cursor.execute("SELECT * FROM menu")
        items = self.my_cursor.fetchall()
        if not items:
            print("Menu is currently empty.")
            return

        total = 0
        ordered_items = []
        while True:   
            for i, (item, price) in enumerate(items, 1):
                print(f"{i}. {item} - Rs.{price}")
            print(f"{len(items) + 1}. Exit and show bill")
            try:
                print("                                         ")
                choice = int(input("Select item number to order: "))
                if choice == len(items) + 1:
                    break   
                elif 1 <= choice <= len(items):   
                    item_name = items[choice - 1][0] 
                    price = items[choice - 1][1]
                self.my_cursor.execute(
                    "INSERT INTO orders (item_name, Price) VALUES (%s, %s)",(item_name, price)
                )
                self.db.commit()
                total += price
                ordered_items.append(item_name)
                print("                                         ")
                print(f" Added {items[choice - 1][0]} to order.")
            except:
                print(" Please enter a valid number.")
        print(f"\n Your total bill is Rs.{total}")
    # Main function to run the app
    def show(self):
        print("                                             ")
        print(" -------> Welcome to foody lovers <-----------")
        print("                                                     ")
        while(True):
            print(" 1:Admin login\n 2:User Register\n 3:User Login\n 4:Exit")
            choice=input("enter the choice:...")
            if not choice.isdigit():
             print(" Invalid input! Please enter a number (1-4).")
             continue
            if choice=='1':
                self.Admin_login()
            elif choice=='2':
                self.user_register()
            elif choice=='3':
                self.user_login()
            elif choice=='4': 
                break
            else:
                print("-----------> Invalid Choice <---------------")        


d=food()
d.show()
        
