import sys
import os
import csv


product = []      
courier = []
order=[]

def clear():
    os.system( 'cls' )
    
    #Main menu 
def main_menu():
    clear()
    print("Welcome to the CAfee!".center(125,  " "))
    print('''
                0.Save and Exit
                1.For Product
                2. For Couriers
                3.For Orders
                 ''')
    

while True:
    value = int(input('''Select a option 0:Save and Exit |1 : Show the product items: '''))
             
    if value == 0:
        sys.exit(0) 
                
    elif value == 1:
        clear()
        print('''
                                                    Welcome to Product menu                                      
              0. To return to Main menu.
              1.List Product.
              2.Create New Product.
              3.Update/ Replace product.
              4.Delete Product.
             ''')
        while True:
            value = int(input("Select a option 0 |1 |2 |3 |4 : "))
            if value==0:
                main_menu()
                break  
            
            if value==1:
                print("displaying product")
               
            
            elif value ==2:
               print("adding product")    
                                    
                        
            elif value==3:
                print("updating product")
                
                
                
            elif value==4:
               print("deleting product")
                    
                        
            else:
                print("Invalid option.Please select option from 0-4")
                
    elif value==2:
        clear()
        print('''
                                                        Welcome to Courier menu
                                                        
              0. To return to Main menu.
              1.List Couriers.
              2.Create New Couriers.
              3.Update/ Replace Couriers.
              4.Delete Couriers.
             ''')
        while True:
            value = (int(input("Select a option 0 |1 |2 |3 |4 : ")))
            if value==0:
                main_menu()
                break   
            
            elif value==1:
                print("displaying couriers")
                
                
            elif value==2:
                 print("adding couriers")
                
                
                
                                   
            elif value==3:
                print("updating couriers")
               
            elif value ==4:             
               print("deleting couriers")
                
            else:
                print("Invalid option Select option 0-4")    
            
    elif value==3:
        clear()
        print('''
                                                        Welcome to order menu
                                                        
              0. To return to Main menu.
              1.List Orders.
              2.Create New Order.
              3.Update/ Replace Order.
              4.Delete order.
             ''')
        
        while True:
            value =int(input("Select a option 0 |1 |2 |3 |4 : "))
            if value==0:
                main_menu()
                break   
            
            elif value==1:
                print("displaying orders")
              
                        
            elif value==2:
                print("adding orders")
                
            elif value ==3:
                print("updating orders")
                    
            elif value==4:
               print("deleting orders") 

            else:
                print("Invalid Option")
                          
    else:
        print('''
                            INVALID OPTION | Select Option from 0-3
                            ''')
        print(" ")
        print('*************************THANK YOU***************************')
                    
#Main menu function