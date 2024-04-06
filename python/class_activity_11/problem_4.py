# Importing the required libraries
import datetime
import os

# Creating a class for an inventory item which has the name, quantity and date that it is added on the last time
class InventoryItem:
    # Constructor for the inventory item class
    def __init__(self, name, quantity, added_on) -> None:
        self.name = name
        self.quantity = quantity
        self.added_on = added_on

# Creating a class for an inventory, which stores the inventory items
class Inventory:
    # Initializing a list which keeps track of all the items in the inventory
    def __init__(self) -> None:
        self.all_items:list[InventoryItem] = []

# Method to add an item in the inventory
    def add_item(self, name, quantity):
        # Verifying quantity is greater than 0
        if quantity <0:
            raise Exception("Quantity must be positive integer !")
        else:
            flag = False
            # Iterating through the items
            for item in self.all_items:
                # Checking if the item matches the name in the inventort, if yes, we are incrementing the quantity
                if item.name == name:
                    flag = True
                    item.quantity += quantity
                    # Updating the added time
                    added_on = datetime.datetime.now()
                    item.added_on = added_on
            if flag == False: # if the item doesn't already exist in the inventory, we initialize an item and add the quantity    
                added_on = datetime.datetime.now()
                self.all_items.append(InventoryItem(name, quantity, added_on))
        
        return f"The addition of {quantity} {name} is successful at {added_on} "

    # Method to remove the item
    def remove_item(self, name, quantity):
        # verifying quantity is greater than 0
        if quantity <0:
            raise Exception("Quantity must be positive integer !")
        else:
            flag = False
            # Checking if the item matches the name in the inventort, if yes, we are decrementing the quantity
            for item in self.all_items:
                if item.name == name:
                    flag = True
                    # Verifying the quantity
                    if item.quantity > quantity:
                        item.quantity -= quantity
                        # handling exception
                    elif item.quantity < quantity:
                        raise Exception("You can't remove more items than that exist !!!!!")
                    # if the requested quantity matches the quantity of the item, we can remove it completely
                    else:
                        self.all_items.remove(item)
            # handling exception
            if flag == False:
                raise Exception("The item you're suggesting to remove doesn't exist !!!!")
        
        return f"Removal of {quantity} {name} is successful !!"
    
    # method to search for an item
    def search_item(self,name):
        flag = False
        # iterating through all the items in the inventory
        for item in self.all_items:
            if item.name == name:
                flag = True
                print(f"The {item.name} is available in {item.quantity} quantity and was last added on {item.added_on}")
        # If the item isn't present:
        if not flag:
            print(f"{name} is not found in the inventory !!!")

# method to get the summary of the inventory
    def get_total_inventory(self):
        total_items = 0
        # Iterating through the items
        for item in self.all_items:
            print(f"There are {item.quantity} number of {item.name} which was last added on {item.added_on}")
            total_items+= item.quantity
        
        print(f"\nSo, the total number of items in the inventory are: {total_items}\n\n")


# Creating a menu for the user
def menu():
    os.system("clear")
    print("\nHello, welcome user, press enter to create an inventory !!!")
    a = input()
    my_inventory = Inventory()
# Creating a loop
    while True:
        try:
            # displaying the message
            os.system("clear")
            print("""Use the following manual:
                1. Add a new item
                2. Remove an existing item
                3. search item
                4. display inventory summary
                q: quit""") 
            # Selecting a choice and selecting as per the choices   
            choice = input()
            if choice == "q":
                break
            elif choice == "1":
                name = input("Enter the name of the item you wish to add: ")
                quantity = int(input("Enter the quantity of the item you wish to add: "))
                print(my_inventory.add_item(name, quantity))
            elif choice == "2":
                name = input("Enter the name of the item you wish to remove: ")
                quantity = int(input("Enter the quantity of the item you wish to remove: "))
                print(my_inventory.remove_item(name , quantity))
            elif choice == "3":
                name = input("Enter the name of the item you wish to search for: ")
                my_inventory.search_item(name)
            elif choice == "4":
                my_inventory.get_total_inventory()
            else:
                print("Please choose a valid number")
        
        # Handling exceptions
        except Exception:
            print(f"Error: {str(Exception)}")

        # Holding the program for the users to view the output
        a = input("\n\t\tPress enter to continue")

# Main driver code
if __name__ == "__main__":
    menu()