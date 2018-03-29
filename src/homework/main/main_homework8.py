import pickle
from src.homework.homework8 import add_inventory, remove_inventory_widget
'''
Write a main function to create an empty dictionary and
a user-controlled loop to prompt for a widget name and quantity.
Add the values to the dictionary as key(widget name) and value(quantity) pairs.

After user decides to exit write data to file .

'''
def main():

    inventory = {}

    again = 'y'

    while again == 'y' or again == 'Y':
        widget_name = input("Enter widget name: ")
        quantity = int(input("Enter quantity: "))
        add_inventory(inventory, widget_name, quantity)
        again = input("Would you like to add another widget?(y or Y) ")

    file_object = open('homework8data.dat', 'wb')

    pickle.dump(inventory, file_object)

    file_object.close()


main()


