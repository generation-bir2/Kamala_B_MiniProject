import mysql.connector
import os
import sys
from tabulate import tabulate
#import prettytable

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="Project",
    autocommit=True,
    #autoclose =True
    )

mycursor = mydb.cursor(buffered=True)



def clear():
    os.system( 'cls' )
        

#Main menu 
def main_menu():
      clear()
      print("Welcome to the CAfee!".center(250,  " "))
      print('''
                  0.Save and Exit
                  1.For Product
                  2. For Couriers
                  3.For Orders
                  ''')

def product_menu():
  print('''
        
                                                    Welcome to Product menu                                      
              0. To return to Main menu.
              1.List Product.
              2.Create New Product.
              3.Update/ Replace product.
              4.Delete Product.
             '''.center(250,  " "))
  
def courier_menu():
        print('''
                                                        Welcome to Courier menu
                                                        
            0. To return to Main menu.
            1.List Couriers.
            2.Create New Couriers.
            3.Update/ Replace Couriers.
            4.Delete Couriers.
             '''.center(250, " "))
        
def order_menu():
        print('''
                                                        Welcome to Order menu
                                                        
            0. To return to Main menu.
            1.List Orders.
            2.Create New Orders.
            3.Update/ Replace Orders.
            4.Delete Orders.
             '''.center(250, " ")) 
             
#reading products as table        
def read_product():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM products")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['products_id', 'product','price'], tablefmt='fancy_grid'))
    print(" ")
    
#reading couriers as table 
def read_couriers():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM couriers")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['Courier_id', 'Name','Phone Number'], tablefmt='fancy_grid'))
    print(" ")
#reading orders from Database as table   
def read_orders():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM orders")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['Orders_id', 'customer_name','customer_address','customer_phone','courier','status','item'], tablefmt='fancy_grid'))
    print(" ")
    
def read_courier_incourier():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT couriers_id,courier FROM couriers")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['Courier_id', 'Name','Phone Number'], tablefmt='fancy_grid'))
    print(" ")
    
def read_PRODUCT_inPRODUCT():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT products_id,product FROM products")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['Courier_id', 'Name','Phone Number'], tablefmt='fancy_grid'))
    print(" ")
 
        
while True:
    main_menu()       
    value = int(input('''Select a option 0:Save and Exit |1 : Show the product items: '''))
             
    if value == 0:
        sys.exit(0) 
                
    elif value == 1:
        clear()
        product_menu()
     
        while True: 
            value = int(input("Select a option 0 |1 |2 |3 |4 : "))
            if value==0:
                main_menu()
                break  
            
            elif value==1:
                
                read_product()
                
                    
                
                 
                
            elif value ==2:
                mycursor = mydb.cursor()
                new_product=input("Enter new product: ")
                product_price=float(input("Enter the price of your new product: "))
                sql = "INSERT INTO products (product, price) VALUES (%s, %s)"
                val = (new_product, product_price)
                mycursor.execute(sql,val)
                print(new_product,"is added to record: ID is ", mycursor.lastrowid)
                read_product()
                
            elif value==3:
                read_product()
                cmd="SELECT * from products"
                mycursor.execute(cmd)
                update= int(input("Enter the ID of product that you want to change: "))
                mycursor.execute("SELECT * From products where products_id=%s"%update)
                myrecord=mycursor.fetchone()
                c=mycursor.rowcount
                if update==0:
                    break
                else:
                    if c == -1: 
                        print("Id ",update,'not found')
                    else:
                        New_name=myrecord[1]
                        New_price=myrecord[2]
                        print("type value to update below or just press Enter for no change")
                        x=input("New name: ")
                        if len(x)>0:
                            New_name=x
                        x=input("New Price: ")
                        if len(x)>0:
                            New_price=x
                        sql="UPDATE products SET product=%s,price=%s WHERE products_id=%s"
                        val=(New_name,New_price,update)
                        mycursor.execute(sql,val)
                        print()
                        print("------Table successfully modidfied-------")
                        print()
                                    
                
                
            elif value==4:
                delete_product=int(input("Enter new ID of product or 0 to cancel: "))
                if delete_product==0:
                    break
                else:
                    sql = "DELETE FROM products WHERE products_id=%s" % delete_product
                    mycursor.execute(sql)
                    mydb.commit()
                    print("ID" , delete_product, "is deleted from record.", mycursor.lastrowid)
                    read_product()
                    
            else:
                print("Invalid option.Please select option from 0-4")
                
    elif value==2:
        clear()
        courier_menu()
        while True:
            value = (int(input("Select a option 0 |1 |2 |3 |4 : ")))
            if value==0:
                main_menu()  
                break
            
            elif value==1:
                read_couriers()
                
                
            elif value==2:
                
                new_courier=input("Enter new courier Name: ")
                Courier_contactNo=float(input("Contact number of new courier: "))
                sql = "INSERT INTO couriers (courier, courier_phone_number) VALUES (%s, %s)"
                val = (new_courier, Courier_contactNo)
                mycursor.execute(sql, val)
                mydb.commit()
                print(new_courier,"is added to record: ID is ", mycursor.lastrowid)
                read_couriers()
                        
                                
            elif value==3:
                read_couriers()
                # cmd="SELECT * from couriers"
                # mycursor.execute(cmd)
                update= int(input("Enter the ID of courier that you want to change: "))
                mycursor.execute("SELECT * From couriers where couriers_id=%s"%update)
                myrecord=mycursor.fetchone()
                if update==0:
                    break
                else:
                    c=mycursor.rowcount
                    if c == -1: 
                        print("Id ",update,'not found')
                    else:
                        New_courier=myrecord[1]
                        New_phone=myrecord[2]
                        print("Type value to update below or just press Enter for no change")
                        x=input("New courier: ")
                        if len(x)>0:
                            New_courier=x
                        x=input("New Contact Number: ")
                        if len(x)>0:
                            New_phone=x
                        sql="UPDATE couriers SET courier=%s,courier_phone_number=%s WHERE couriers_id=%s"
                        val=(New_courier,New_phone,update)
                        mycursor.execute(sql,val)
                        print()
                        print("Table successfully modified")
                        print()
                # read_couriers()
                # cmd="SELECT * from couriers"
                # mycursor.execute(cmd)
                # update= int(input("Enter the ID of courier that you want to change: "))
                # mycursor.execute("SELECT * From couriers where couriers_id=%s"%update)
                # myrecord=mycursor.fetchone()
                # c=mycursor.rowcount
                # if c == -1: 
                #     print("Id ",update,'not found')
                # else:
                #     New_courier=myrecord[1]
                #     New_phone=myrecord[2]
                #     print("Type value to update below or just press Enter for no change")
                #     x=input("New courier: ")
                #     if len(x)>0:
                #         New_courier=x
                #     x=input("New Conatct Number: ")
                #     if len(x)>0:
                #         New_phone=x
                #     sql="UPDATE couriers SET courier=%s,courier_phone_number=%s WHERE couriers_id=%s"
                #     val=(New_courier,New_phone,update)
                #     mycursor.execute(sql,val)
                #     print()
                #     print("Table successfully modidfied")
                #     print()
                        
                        
            elif value ==4: 
                    delete_courier=int(input("Enter product's ID to delete: "))
                    if delete_product==0:
                        break
                    else:                      
                        sql ="DELETE FROM couriers WHERE couriers_id=%s" % delete_courier
                        mycursor.execute(sql)
                        mydb.commit()
                        print("ID" , delete_courier, "is deleted from record.", mycursor.lastrowid)   
                        read_couriers()
                    
            else:             
                print("Invalid option Select option 0-5") 
    
    elif value == 3:
        clear()
        order_menu()
        while True:
            value = (int(input("Select a option 0 |1 |2 |3 |4 : ")))
            if value==0:
                main_menu()
                break
                    
            if value == 1:
                read_orders()
                                
            if value==2:
                Customer_name=input("Enter Customer Name: ")
                Customer_address=input("Enter Customer address: ")
                Courier_contactNo=int(input("Enter Customer phone number: "))
                read_courier_incourier()
                courier=input("courier ID  ")
                read_PRODUCT_inPRODUCT()
                item=str(input("item: "))
                cmd=mycursor.execute("SELECT courier from couriers")
                myresult=mycursor.fetchall()
                sql = "INSERT INTO orders (customer_name, Customer_address,Customer_phone,courier,items) VALUES (%s, %s,%s, %s,%s)"
                val = (Customer_name, Customer_address,Courier_contactNo,courier,item)
                mycursor.execute(sql, val)
                print("order is added to record: ID is ", mycursor.lastrowid)  
                 
            if value==3:
                read_orders()
                cmd="SELECT * from orders"
                mycursor.execute(cmd)
                update= int(input("Enter the ID of order that you want to change: "))
                mycursor.execute("SELECT * From orders where orders_id=%s"%update)
                myrecord=mycursor.fetchone()
                if update==0:
                    break
                else:
                        
                    c=mycursor.rowcount
                    if c == -1: 
                        print("Id ",update,'not found')
                    else:
                        name=myrecord[1]
                        address=myrecord[2]
                        phone=myrecord[3]
                        courier=myrecord[4]
                        status=myrecord[5]
                        items=myrecord[6]
                        print("Type value to update below or just press Enter for no change")
                        x=input("Name: ")
                        if len(x)>0:
                            name=x
                        x=input("New address: ")
                        if len(x)>0:
                            address=x
                        x=input("New Conact Number: ")
                        if len(x)>0:
                            phone=x
                        x=input("Newcourier ID: ")
                        if len(x)>0:
                            courier=x
                        x=input("New order status: ")
                        if len(x)>0:
                            status=x
                        x=input("New Items selection: ")
                        if len(x)>0:
                            item=x
                        sql="UPDATE orders SET customer_name=%s,Customer_address=%s,customer_phone=%s,courier=%s,status=%s,items=%s WHERE orders_id=%s"
                        val=(name,address,phone,courier,status,items,update)
                        mycursor.execute(sql,val)
                        print()
                        print("Table successfully modidfied")
                        print()
                    
            if value==4:
                delete_orders=int(input("Enter Order ID to cancel: "))
                sql ="DELETE FROM orders WHERE orders_id=%s" % delete_orders
                mycursor.execute(sql)
                mydb.commit()
                read_orders()
                print(" ")
                print("ID" , delete_orders, "is deleted from record.", mycursor.lastrowid)   
                print(" ")
                    
            
                
            
    else:
        print('''
                            INVALID OPTION | Select Option from 0 |1 |2 
                            ''')
        print(" ")
        print('*************************THANK YOU***************************')                           
                    
                
    