'''
Instructions before using the program
1. Enter your MySQL username in line 13 where it says <Enter your username>
2. Enter your MySQL password in line 14 where it says <Enter your password>
3. Make a database named restaurant in your MySQL
4. If you want to add more items in the menu you can go to line 175 and use the function add_menu_item to add more items
Now you are good to run this program
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
    # Print the menu
    print_menu()
    # Get the user's input
    choice = input('Enter your choice: ')
    # Handle the user's choice
    handle_choice(choice)


# Function to print the menu
def print_menu():
    print('1. View the menu')
    print('2. Place an order')
    print('3. Exit')


# Function to handle the user's choice
def handle_choice(choice):
    # View the menu
    if choice == '1':
        view_menu()
    # Place an order
    elif choice == '2':
        place_order()
    # Exit the program
    elif choice == '3':
        exit()
    # Handle invalid input
    else:
        print('Invalid choice.')
        main()


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
def view_menu():
    # SQL query to select all items from the menu table
    query = "SELECT * FROM menu"

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Print the menu items
    print("--- Menu ---")
    for result in results:
        print(f"{result[1]}: ₹{result[2]}")

    # Call main to allow the user to continue using the program
    main()




# Function to add a menu item
def add_menu_item(id, name, price):
    # SQL query to insert the new menu item
    query = """
        INSERT INTO menu (id, name, price)
        VALUES (%s, %s, %s)
    """

    # Execute the query
    cursor.execute(query, (id, name, price))




# Function to place an order
def place_order():
    # Get the user's order
    order = input('Enter your order: ')
    order = order.capitalize()

    # Check if the user's input is valid
    if len(order.split()) < 2:
        print('Invalid input. Please enter a valid item and quantity.')
        main()
        return

    # Split the order into a list of items and quantities
    order_list = order.split()

    # Initialize the total cost of the order
    total_cost = 0

    # Iterate over the items in the order
    for i in range(0, len(order_list), 2):
        # Get the item and quantity
        item = order_list[i]
        quantity = order_list[i + 1]

        # Query the database to get the price of the item
        query = 'SELECT price FROM menu WHERE name = %s'
        cursor.execute(query, (item,))
        price = cursor.fetchone()[0]

        # Calculate the total cost of the item
        item_total = price * int(quantity)

        # Print the item details
        print('Item: ' + item)
        print('Quantity: ' + quantity)
        print('Total Cost: ₹' + str(item_total))

        # Add the item total to the overall total cost
        total_cost += item_total

    # Print the overall total cost of the order
    print('Total Cost: ₹' + str(total_cost))

    # Go back to the main menu
    main()




# Function to delete the menu table
def delete_menu_table():
    # SQL query to delete the table
    query = "DROP TABLE menu"

    # Execute the query
    cursor.execute(query)


# Delete the menu table
delete_menu_table()

# Create the menu table
create_menu_table()

# Add some menu items

add_menu_item(1,"Hamburger", 50)
add_menu_item(2,"Pizza", 100)
add_menu_item(3,"Salad", 30)

cnx.commit()



# Call the main function
main()

# Close the cursor and connection
cursor.close()
cnx.close()