import datetime
from itertools import product
import json


# from requests import JSONDecodeError


class GameRental:
    def __init__(self, storename):
        self.storename = storename

    def register_gamer(self, user_json, name, phone, email, password):
        user = {'id': 1,
                'name': name,
                'phone': phone,
                'email': email,
                'password': password,
                'cart': {},
                'wishlist': {},
                'order_history': {}
                }

        try:
            file = open(user_json, "r+")
            content = json.load(file)

            for i in range(len(content)):
                if content[i]['phone'] == phone:
                    print("User already exists.")
                    break
            else:
                user['id'] = len(content) + 1
                content.append(user)
                print("success")
        except JSONDecodeError:
            content = []
            content.append(user)
            print("success")
        file.seek(0)
        file.truncate()
        json.dump(content, file, indent=4)
        file.close()

    def register_seller(self, seller_json, name, password):
        seller = {'id': 1,
                'name': name,
                'password': password,
                }
        try:
            file = open(seller_json, "r+")
            content = json.load(file)

            for i in range(len(content)):
                if content[i]['name'] == name:
                    print("User already exists.")
                    break
            else:
                seller['id'] = len(content) + 1
                content.append(seller)
                print("success")
        except JSONDecodeError:
            content = []
            content.append(seller)
            print("success")
        file.seek(0)
        file.truncate()
        json.dump(content, file, indent=4)
        file.close()



    def user_order_history(self, user_json, user_id):
        file = open(user_json, "r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["id"] == user_id:
                print(f"Hi {content[i]['name']}, Your Order History:")
                print("Date | Order, Quantity, Paid Ammount")
                for i, j in content[i]["order_history"].items():
                    print(f"{i} | {j}")
                file.close()
                return True
        file.close()
        return False

    def user_wishlist(self, user_json, products_json, user_id, products_name, quantity):
        date = datetime.datetime.today().strftime('%m-%d-%Y')
        file = open(user_json, "r+")
        content = json.load(file)
        file1 = open(products_json, "r+")
        content1 = json.load(file1)
        for i in range(len(content1)):
            if content1[i]["Product Title"] == products_name:
                if content1[i]["STOCK"] >= quantity:
                    for j in range(len(content)):
                        if content[j]["id"] == user_id:
                            if date not in content[j]["wishlist"]:
                                content[j]["wishlist"][date] = []
                                content[j]["wishlist"][date].extend([content1[i]["Product Title"], quantity])
                            else:
                                (content[j]["wishlist"][date]).extend([content1[i]["Product Title"], quantity])
                                break
        file.seek(0)
        file.truncate()
        json.dump(content, file, indent=4)
        file.close()

        file1.seek(0)
        file1.truncate()
        json.dump(content1, file1, indent=4)
        file1.close()

    def user_view_wish_list(self, user_json, user_id):
        file = open(user_json, "r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["id"] == user_id:
                print(f"Hi {content[i]['name']}, Your Wish List:")
                print("Date | Order, Quantity, Final Ammount")
                for i, j in content[i]["wishlist"].items():
                    print(f"{i} | {j}")
                file.close()
                return True
        file.close()
        return False

    def user_cart(self, user_json, products_json, user_id, product_name, quantity):
        date = datetime.datetime.today().strftime('%m-%d-%Y')
        file = open(user_json, "r+")
        content = json.load(file)
        file1 = open(products_json, "r+")
        content1 = json.load(file1)
        for i in range(len(content1)):
            if content1[i]["Product Title"] == product_name:
                if content1[i]["STOCK"] >= quantity:
                    for j in range(len(content)):
                        if content[j]["id"] == user_id:
                            if date not in content[j]["cart"]:
                                content[j]["cart"][date] = []
                                content[j]["cart"][date].extend([content1[i]["Product Title"], quantity])
                            else:
                                (content[j]["cart"][date]).extend([content1[i]["Product Title"], quantity])
                                break
        file.seek(0)
        file.truncate()
        json.dump(content, file, indent=4)
        file.close()

        file1.seek(0)
        file1.truncate()
        json.dump(content1, file1, indent=4)
        file1.close()

    def user_view_cart(self, user_json, user_id):
        file = open(user_json, "r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["id"] == user_id:
                print(f"Hi {content[i]['name']}, Your Cart:")
                print("Date | Order, Quantity, Final Ammount")
                for i, j in content[i]["cart"].items():
                    print(f"{i} | {j}")
                file.close()
                return True
        file.close()
        return False

    def user_place_order(self, user_json, products_json, user_id, product_name, quantity):
        date = datetime.datetime.today().strftime('%m-%d-%Y')
        file = open(user_json, "r+")
        content = json.load(file)
        file1 = open(products_json, "r+")
        content1 = json.load(file1)
        for i in range(len(content1)):
            if content1[i]["Product Title"] == product_name:
                if content1[i]["STOCK"] >= quantity:
                    for j in range(len(content)):
                        if content[j]["id"] == user_id:
                            print(f"Price: {content1[i]['price']}")
                            print(f"Discount: {content1[i]['discount']}")
                            final_price = (((content1[i]['price']) - (content1[i]['discount'])) * quantity)
                            print(f'Final Price: {final_price}')
                            payment = int(input('Pay the Ammount: '))
                            if (payment == final_price):
                                content1[i]["STOCK"] -= quantity
                                print('success')
                                if date not in content[j]["order_history"]:
                                    content[j]["order_history"][date] = []
                                    content[j]["order_history"][date].extend(
                                        [content1[i]["Product Title"], quantity, final_price])
                                else:
                                    (content[j]["order_history"][date]).extend(
                                        [content1[i]["Product Title"], quantity, final_price])
                                    break
                            else:
                                print('Complete the Payment')
                else:
                    print("Pls Enter less quantity")
                    break

        file.seek(0)
        file.truncate()
        json.dump(content, file, indent=4)
        file.close()

        file1.seek(0)
        file1.truncate()
        json.dump(content1, file1, indent=4)
        file1.close()

    def create_product(self, product_json, product_name, no_products, price, discount, product_type):
        product = {
            "Product ID": 1,
            "Product Title": product_name,
            "STOCK": no_products,
            "price": price,
            "discount": discount,
            'Product_Type': product_type
        }
        try:
            fp = open(product_json, "r+")
            content = json.load(fp)
            for i in range(len(content)):
                if content[i]["Product Title"] == product_name:
                    print("product Already Available")
                    break
            else:
                product["Product ID"] = len(content) + 1
                for i in range(len(content)):
                    if content[i]['Product ID'] == product['Product ID']:
                        while True:
                            product['Product ID'] += 1
                            if content[i]['Product ID'] != product['Product ID']:
                                break
                content.append(product)
                print("Success")

        except json.JSONDecodeError:
            content = []
            content.append(product)
            print("Success")

        fp.seek(0)
        fp.truncate()
        json.dump(content, fp, indent=4)
        fp.close()

    def update_product(self):  # no_plates=-1, price=-1):
        file = open('products.json', "r+")
        content = json.load(file)
        product_id = int(input('Enter the Product ID: '))
        no_products = int(input('Enter the No. of products: '))
        new_price = int(input('Enter the New Price: '))
        new_discount = int(input('Enter the New Discount: '))
        for i in range(len(content)):
            if (content[i]["Product ID"] == product_id):
                content[i]["STOCK"] += no_products
                content[i]["price"] = new_price
                content[i]["discount"] = new_discount
                print("success")
                break
        file.seek(0)
        file.truncate()
        json.dump(content, file, indent=4)
        file.close()

    def remove_product(self, product_json, product_id):
        file = open(product_json, "r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["Product ID"] == product_id:
                print("success")
                del content[i]
                file.seek(0)
                file.truncate()
                json.dump(content, file, indent=4)
                file.close()
                break
        else:
            print("Pls Enter Valid ID")

    def view_product(self, product_json):
        file = open(product_json)
        content = json.load(file)
        print("Menu:")
        for i in range(len(content)):
            print("Id: ", content[i]["Product ID"])
            print(f"---> Name: {content[i]['Product Title']}")
            print(f"---> Number of Products: {content[i]['STOCK']}")
            print(f"---> Price: {content[i]['price']}")
            print(f"---> Type: {content[i]['Product_Type']}")
        file.close()
        return True

    def update_profile(self, user_json, id, choice):
        file = open(user_json, "r+")
        content = json.load(file)

        for i in range(len(content)):
            if content[i]['id'] == id:
                if (choice == '1'):
                    new_name = input('Enter the New Name: ')
                    content[i]['name'] = new_name
                elif (choice == '2'):
                    new_phone = input('Enter the New Phone Number: ')
                    content[i]['phone'] = new_phone
                elif (choice == '3'):
                    new_email = input('Enter the New E-Mail ID: ')
                    content[i]['email'] = new_email
                elif (choice == '4'):
                    new_password = input('Enter the New Password: ')
                    content[i]['password'] = new_password
                elif (choice == '5'):
                    break
                print("Id: ", content[i]["id"])
                print(f"---> Name: {content[i]['name']}")
                print(f"---> Phone: {content[i]['phone']}")
                print(f"---> Email: {content[i]['email']}")
                print(f"---> Password: {content[i]['password']}")
                break
        else:
            print('Enter Valid ID')
        file.seek(0)
        file.truncate()
        json.dump(content, file, indent=4)
        file.close()
        return "success"


try:
    def main():
        obj = GameRental("Gamer's Zone")
        print(f"*^*^*^*^*^*^*^*^*^EATZZ*^*^*^*^*^*^*^*^*^*\n")
        print(f"__/\__  Welcome To {obj.storename}  __/\__\n")
        print("!!**********************************************************************")
        val = input("Do you Want to order Games and Accessories Y/n: ")
        print("***********************************************************************!!\n")
        while val.lower() == "y":
            print("Menu: ")
            print("1) Register")
            print("2) Login")
            print("3) Exit")
            val1 = input("Choose one value from the above: ")
            if val1 == "1":
                # --------------Register----------------#
                print("1. Seller\n2. Gamer\n3. Exit\n")
                valk = input('Enter your choice: ')
                if valk == '1':
                    name = input("Enter the name: ")
                    password = input("Enter the password: ")
                    obj.register_seller('sellers.json', name, password)
                elif valk == '2':
                    print()
                    name = input("Enter the name: ")
                    phone = input("Enter the Phone number: ")
                    email = input("Enter your E-Mail: ")
                    password = input("Enter the password: ")
                    obj.register_gamer('Users.json', name, phone, email, password)
            elif val1 == "2":
                while True:
                    print("1. Seller\n2. Gamer\n3. Exit\n")
                    x = input('Enter You Choice: ')
                    if x == "1":
                        print("$--------Seller------$")
                        user = input("Enter name: ")
                        password = input("Enter Password: ")
                        file = open("Sellers.json", "r+")
                        content = json.load(file)
                        for i in range(len(content)):
                            if content[i]["name"] == user:
                                if content[i]["password"] == password:
                                    while True:
                                        print()
                                        print("1) Create Product")
                                        print("2) Update Product")
                                        print("3) View all Products")
                                        print("4) Remove product")
                                        print("5) View Users")
                                        print("6) Exit")
                                        val3 = input("Enter Your Choice Seller!!")
                                        if val3 == "1":
                                            product_name = input("Enter Product Name: ")
                                            no_products = int(input("Enter the Number of Products: "))
                                            price = int(input("Enter Price: "))
                                            discount = int(input("Enter discount: "))
                                            product_type = input("Enter Product Type: ")
                                            obj.create_product('Products.json', product_name, no_products, price, discount,
                                                               product_type)
                                            break
                                        elif val3 == "2":
                                            obj.update_product()
                                            break
                                        elif val3 == '3':
                                            obj.view_product('Products.json')
                                        elif val3 == '4':
                                            product_id = int(input("Enter The Product ID: "))
                                            obj.remove_product('Products.json', product_id)
                                        elif val3 == '5':
                                            file = open('Users.json')
                                            content = json.load(file)
                                            for i in range(len(content)):
                                                print(f"---> Names: {content[i]['name']}")
                                            break
                                        else:
                                            file.close()
                                            print("%%%%Bye Bye%%%%%")
                                            break
                                else:
                                    print("Wrong Username or Password!!")


                    elif x == "2":
                        print("---------GAMER--------")
                        user = input("Enter name: ")
                        password = input("Enter Password: ")
                        file = open("Users.json", "r+")
                        content = json.load(file)
                        for i in range(len(content)):
                            if content[i]["name"] == user:
                                if content[i]["password"] == password:
                                    while True:
                                        print()
                                        print("1) View All Products")
                                        print("2) Manage Wish List")
                                        print("3) Manage Cart")
                                        print("4) Place New Order")
                                        print("5) Show History of order")
                                        print("6) Update Profile")
                                        print("7) View Profile")
                                        print("8) Exit")
                                        val3 = input("Enter your Choice User!! ")
                                        if val3 == "1":
                                            obj.view_product("Products.json")
                                        elif val3 == "2":
                                            print('A] Add to Wishlist\nB] View Wishlist\nC] Delete from Wishlist')
                                            val_a = input("Enter Your Choice")
                                            if val_a == 'A':
                                                user_id = int(input("Enter User Id:"))
                                                product_name = input("Enter the Product You want to Purchase: ")
                                                quantity = int(input("Enter the quantity of Products: "))
                                                obj.user_wishlist("Users.json", "Products.json", user_id, product_name,
                                                                  quantity)
                                            else:
                                                user_id = user_id = int(input("Enter User Id:"))
                                                obj.user_view_wish_list('Users.json', user_id)
                                        elif val3 == "3":
                                            print('A] Add to Cart\nB] View Cart')
                                            val_a = input("Enter Your Choice")
                                            if val_a == 'A':
                                                user_id = int(input("Enter User Id:"))
                                                product_name = input("Enter the Product You want to Purchase: ")
                                                quantity = int(input("Enter the quantity of Products: "))
                                                obj.user_cart("Users.json", "Products.json", user_id, product_name,
                                                              quantity)
                                            elif val_a == 'B':
                                                user_id = int(input("Enter User Id:"))
                                                obj.user_view_cart('Users.json', user_id)

                                        elif val3 == "4":
                                            user_id = int(input("Enter User Id:"))
                                            product_name = input("Enter the Product You want to Purchase: ")
                                            quantity = int(input("Enter the quantity of Products: "))
                                            obj.user_place_order("Users.json", "Products.json", user_id, product_name,
                                                                 quantity)
                                        elif val3 == "5":
                                            user_id = int(input("Enter User Id:"))
                                            obj.user_order_history('Users.json', user_id)
                                        elif val3 == "6":
                                            id = int(input('Enter ID: '))
                                            print('Menu:\n')
                                            print("1) change New Name")
                                            print("2) change Phone Number")
                                            print("3) change E-Mail")
                                            print("4) change Password")
                                            print("5) Exit")
                                            choice = input('Enter Your Choice: ')
                                            obj.update_profile('Users.json', id, choice)
                                        elif val3 == '7':
                                            Usr_id = int(input('Enter Your User ID: '))
                                            file = open('Users.json')
                                            content = json.load(file)
                                            for i in range(len(content)):
                                                if (content[i]['id'] == Usr_id):
                                                    print("Id: ", content[i]["id"])
                                                    print(f"---> Name: {content[i]['name']}")
                                                    print(f"---> Phone: {content[i]['phone']}")
                                                    print(f"---> Email: {content[i]['email']}")
                                                    print(f"---> Password: {content[i]['password']}")
                                                    break

                                        else:
                                            print("Thanks FOr Your Visit")
                                            break
                        else:
                            print('Wrong Username or Password')
                    elif x == "3":
                        break
                    else:
                        print("Invalid Number")
except Exception as e:
    print("something went wrong please give input carefully")

    # calling the main function

if __name__ == '__main__':
    main()