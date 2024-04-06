# Importing the required libraries
import datetime
import os

# creating a global variable to track all items in the inventory and last operation
all_items = []
last_operation = {"type":'', "name":"", "quantity":0, "date":datetime.datetime.now()}

# function to add an item in the inventory
def add_item(name, quantity):
    # Verifying quantity is greater than 0
    if quantity <0:
        raise Exception("Quantity must be positive integer !")
    else:
        flag = False
        # Iterating through the items
        for item in all_items:
            # Checking if the item matches the name in the inventory, if yes, we are incrementing the quantity
            if item[0] == name:
                flag = True
                item[1] += quantity
                # Updating the added time
                added_on = datetime.datetime.now()
                item[2] = added_on
        if flag == False: # if the item doesn't already exist in the inventory, we initialize an item and add the quantity    
            added_on = datetime.datetime.now()
            all_items.append([name, quantity, added_on])

    #  updating last operation
    last_operation["type"] = "Addition"
    last_operation["name"] = name
    last_operation["quantity"] = quantity
    last_operation["date"] = added_on

    return f"The addition of {quantity} {name} is successful at {added_on} "

    # function to remove the item
def remove_item(name, quantity):
    # verifying quantity is greater than 0
    if quantity <0:
        raise Exception("Quantity must be positive integer !")
    else:
        flag = False
        # Checking if the item matches the name in the inventort, if yes, we are decrementing the quantity
        for item in all_items:
            if item[0] == name:
                flag = True
                # Verifying the quantity
                if item[1] > quantity:
                    item[1] -= quantity
                    # handling exception
                elif item[1] < quantity:
                    raise Exception("You can't remove more items than that exist !!!!!")
                # if the requested quantity matches the quantity of the item, we can remove it completely
                else:
                    all_items.remove(item)
        # handling exception
        if flag == False:
            raise Exception("The item you're suggesting to remove doesn't exist !!!!")
    
    #  updating last operation
    last_operation["type"] = "Removal"
    last_operation["name"] = name
    last_operation["quantity"] = quantity
    last_operation["date"] = datetime.datetime.now()

    return f"Removal of {quantity} {name} is successful !!"

# function to search for an item
def search_item(name):
    flag = False
    # iterating through all the items in the inventory
    for item in all_items:
        if item[0] == name:
            flag = True
            print(f"The {item[0]} is available in {item[1]} quantity and was last added on {item[2]}")
    # If the item isn't present:
    if not flag:
        print(f"{name} is not found in the inventory !!!")

#  updating last operation
    last_operation["type"] = "Search"
    last_operation["name"] = name
    last_operation["date"] = datetime.datetime.now()

# function to get the summary of the inventory
def get_total_inventory():
    total_items = 0
    # Iterating through the items
    for item in all_items:
        print(f"There are {item[1]} number of {item[0]} which was last added on {item[2]}")
        total_items+= item[1]
    
    last_operation["type"] = "Summary of inventory"
    last_operation["name"] = ""
    last_operation["quantity"] = total_items
    last_operation["date"] = datetime.datetime.now()

    print(f"\nSo, the total number of items in the inventory are: {total_items}\n\n")


# Function to display the last update on the user operation
def display_last_update():
    print(f"The last operation that occurred was {last_operation['type']} on {last_operation['quantity']} {last_operation['name']} at {last_operation['date']}")


# Creating a menu for the user
def menu():
    os.system("clear")
    print("\nHello, welcome user, press enter to create an inventory !!!")
    a = input()
# Creating a loop
    while True:
        try:
            # displaying the message
            os.system("clear")
            print("""Use the following manual:
                1. Add a new item
                2. Remove an existing item
                3. Search item
                4. Display inventory summary
                5. Display last update date and time
                6: quit""") 
            # Selecting a choice and selecting as per the choices   
            choice = input()
            if choice == "6":
                break
            elif choice == "1":
                name = input("Enter the name of the item you wish to add: ")
                quantity = int(input("Enter the quantity of the item you wish to add: "))
                print(add_item(name, quantity))
            elif choice == "2":
                name = input("Enter the name of the item you wish to remove: ")
                quantity = int(input("Enter the quantity of the item you wish to remove: "))
                print(remove_item(name , quantity))
            elif choice == "3":
                name = input("Enter the name of the item you wish to search for: ")
                search_item(name)
            elif choice == "4":
                get_total_inventory()
            elif choice == "5":
                display_last_update()
            else:
                print("Please choose a valid number")
        
        # Handling exceptions
        except Exception as e:
            print(f"Error: {e.__str__()}")

        # Holding the program for the users to view the output
        a = input("\n\t\tPress enter to continue")

# Main driver code
if __name__ == "__main__":
    menu()