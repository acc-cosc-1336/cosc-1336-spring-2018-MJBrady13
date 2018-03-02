#write the import for function for assignment7 sum_list_values
from src.assignments.assignment7 import sum_list_values
'''
Create a function named process_list that calls the sum_list_values function.
Prints the list values and the sum of the element in the list as follows:
joe 10 15 20 30 40 sum: 115

Create a main function.
In the function loop as long as user wants to add another list.
Prompt the user for name and append to the list.
Prompt the user for number of numeric values in the list.
Iterate the number of times the user enters and prompt end-user for n numeric values.

Call the main function
--------------------
joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89

'''
def process_list(list1):
    sum_values = sum_list_values(list1)
    print(list1, 'sum: ', sum_values)

def main():
    
    keep_going = 'y'
    while keep_going == 'y' or keep_going == 'Y':
        new_list = []
        name = input('Enter a name for the list: ')
        new_list.append(name)
        #print(new_list)
        max_nums = int(input('Enter the total number of numeric values in the list: '))
        
        index = 0
        while index < max_nums:
            new_num = int(input('Enter the next value: '))
            new_list.append(new_num)
            #print(new_list)
            index += 1
        process_list(new_list)
        keep_going = input('Do you want to create another list?(y or Y): ')
        
main()
