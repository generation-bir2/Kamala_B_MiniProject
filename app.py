import sys
#products =[]
# def product():
#     file=open("product.txt","r")
#     product_lines=file.readlines()
#     for line in product_lines:
#         print([line.rstrip()])
        
# product()   

# # def couriers():
# #     file=open("couriers.txt","r")
# #     couriers_lines=file.readlines()
# #     for line in couriers_lines:
# #         print(line)
# # couriers()    

def main_menu():
    print("Welcome to the CAfee!".center(125,  " "))
    print('''
                0.Save and Exit
                1.For Product
                2. For Couriers
                ''')
main_menu() 


while True:
    value = (int(input('''Select a option 0:Save and Exit |1 : Show the product items: ''')))

    if value == 0:
        sys.exit(0) 
                
    elif value == 1:
        print('''
            0. To return to Main menu.
            1.List Product.
            2.Create New Product.
            3.Update/ Replace product.
            4.Delete Product.
            ''')
        while True:
            value = (int(input("Select a option 0 |1 |2 |3 |4 : ")))
            if value==0:
                main_menu()
                break  
            
            if value==1:
                file=open("product.txt","r")
                product_lines=file.readlines()
                for line in product_lines:
                    print([line.rstrip()])
            elif value ==2:
                item=input("Enter your new item:- ")   
                with open('product.txt', 'a+') as file:
                    file.write(item +'\n')
                
            elif value==3:
                replace_item= int(input("Item index to replace(0 |1 |2 |3 |4 ) :" ))
                item_to_replace = input("Item to replace: ")
                product[replace_item]=item_to_replace
                print(product)
                
            elif value==4:
                print(products) 
                to_delete =int(input("select item index to delete(0 |1 |2 |3 |4 ): "))
                products.pop(to_delete)
                print(products)
                
            else:
                print("Thats look good to me")
  
    elif value==2:
        print('''
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
                file=open("couriers.txt","r")
                couriers_lines=file.readlines()
                for line in couriers_lines:
                    print(line)
                    
            elif value==3:
                # replace_item= int(input("Item index to replace(0 |1 |2 |3 |4 ) :" ))
                # item_to_replace = input("Item to replace: ")
                # product[replace_item]=item_to_replace
                # print(courier)
                
                
            
            
        
    # else:
    #     print("INVALID OPTION")
    #     print(" ")
    #     print('*************************THANK YOU***************************')