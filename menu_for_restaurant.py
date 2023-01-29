'''
Instructions before using the program
1. Enter your MySQL username in line 13 where it says <Enter your username>
2. Enter your MySQL password in line 14 where it says <Enter your password>
3. Make a database named restaurant in your MySQL
Now you are good to run this program
Enjoy!
'''

import mysql.connector

# Connection
cnx = mysql.connector.connect(user='<Enter your username>',
                              password='<Enter your password>',
                              host='localhost',
                              database='restaurant') # IMP - Make a database named restaurant in your MySQl
# Cursor
cursor = cnx.cursor()


# Main function
def main():
    print('1. If you are the owner')
    print('2. If you are a customer')
    print('3. Exit the program')
    # choose between owner and customer
    ch = input('Enter your choice:')
    if ch == '1':
        check_owner()
    elif ch == '2':
        customer()
    elif ch == '3':
        exit()
    else:
        print('Invalid choice.')


#check for owner
def check_owner():
    password = 'mypassword'
    p = input('Ener password')
    if p == password:
        owner()
    else:
        print('Wrong password')
        main()


# Choices for owner
def owner():
    print('1. View the menu')
    print('2. Add new item in menu')
    print('3. Remove an item from menu')
    print('4. Exit the owner tab')
    choice = input('enter your choice:')
    # View the menu
    if choice == '1':
        view_menu_owner()
    # Add an item in the menu
    elif choice == '2':
        add_menu_item()
    #Remove an item
    elif choice == '3':
        remove_item()
    # Exit the program
    elif choice == '4':
        main()
    # Handle invalid input
    else:
        print('Invalid choice.')
        owner()


# Choices for customer
def customer():
    print('1. View the menu')
    print('2. Place an order')
    print('3. Exit the customer tab')
    choice = input('Enter your choice:')
    # View the menu
    if choice == '1':
        view_menu_customer()
    # Place an order
    elif choice == '2':
        place_order()
    # Exit the program
    elif choice == '3':
        main()
    # Handle invalid input
    else:
        print('Invalid choice.')
        customer()



# Function to crate menu table
def create_menu_table():
    # SQL query to create the table
    query = """
        CREATE TABLE IF NOT EXISTS menu (
            id INT(100) PRIMARY KEY,
            name VARCHAR(255),
            price DECIMAL(5,2)
        
        )
    """

    # Execute the query
    cursor.execute(query)





# Function to view the menu
def view_menu_owner():
    # SQL query to select all items from the menu table
    query = "SELECT * FROM menu"

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Print the menu items
    print("-------- Menu --------")
    for result in results:
        print(f"{result[0]}:{result[1]}: ₹{result[2]}")
    print('----------------------')

    owner()

def view_menu_customer():
    # SQL query to select all items from the menu table
    query = "SELECT * FROM menu"

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Print the menu items
    print("-------- Menu --------")
    for result in results:
        print(f"{result[0]}:{result[1]}: ₹{result[2]}")
    print('----------------------')

    customer()


# Function to add a menu item
def add_menu_item():
    while True:
        id = int(input('Enter the id:'))
        name = input('Enter the name:')
        price = int(input('Enter the price'))
        # SQL query to insert the new menu item
        query = """
            INSERT INTO menu (id, name, price)
            VALUES (%s, %s, %s)
        """

        # Execute the query
        cursor.execute(query, (id, name, price))
        cnx.commit()
        if input("press n to stop adding items: ") == "n":
            owner()

def remove_item():
    while True:
        itemn = int(input("\nenter the item id that you want to be remove:"))
        cursor.execute("delete from menu where id='%d'" % itemn)
        print("data removed successfully")
        cnx.commit()
        if input("press n to stop removing items: ") == "n":
            owner()


# Function to place an order
def place_order():
    total_cost = 0
    while True:
        item_id = input('Enter the id of food item:')
        quantity = input('Enter the quantity:')
        # Query the database to get the price of the item
        query = 'SELECT price FROM menu WHERE id = %s'
        cursor.execute(query, (item_id,))
        price = cursor.fetchone()[0]

        # Calculate the total cost of the item
        item_total = price * int(quantity)

        # Print the item details
        print('Item_id: ' + item_id)
        print('Quantity: ' + quantity)
        print('Total Cost: ₹' + str(item_total))

        # Add the item total to the overall total cost
        total_cost += item_total
        if input("\npress n to stop ordering") == "n":
            # Print the overall total cost of the order
            print('Total Cost: ₹' + str(total_cost))
            customer()


# Create the menu table
create_menu_table()

# Call the main function
main()

# Close the cursor and connection
cursor.close()
cnx.close()
