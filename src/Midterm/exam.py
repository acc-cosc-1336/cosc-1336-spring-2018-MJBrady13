'''
5 points
Create a function named get_miles_per_hour with parameters kilometers and minutes that returns
the miles per hour.
Use .621371 as conversion ratio.
Return the string error 'Invalid arguments' if negative kilometers or minutes are given.
RUN THE PROVIDED TEST CASES TO VALIDATE YOUR CODE
'''
def get_miles_per_hour(kilometers, minutes):
    if kilometers < 0 or minutes < 0:
        return 'Invalid arguments'

    hours = minutes / 60
    mph = kilometers / hours * 0.621371
    return mph



'''
10 points
Create a function named get_bonus_pay_amount with parameter sales that returns the bonus pay amount.

Sales Range          Percentage
0    to  499             5%
500  to  999             6%
1000 to 1499             7%
1500 to 1999             8%

Return the string error 'Invalid arguments' if sales amount less than 0 or greater than 1999

Sample Data sales amount:
1000

Return Value:
70

'''
def get_bonus_pay_amount(sales):
    bonus = 0
    if sales < 0 or sales > 1999:
        return 'Invalid arguments'
    elif sales >= 0 and sales <= 499:
        bonus = sales * 0.05
    elif sales >= 500 and sales <= 999:
        bonus = sales * 0.06
    elif sales >= 1000 and sales <= 1499:
        bonus = sales * 0.07
    else:
        bonus = sales * 0.08

    return bonus



'''
10 points
Create a function named reverse_string that has one parameter named string1 that returns the
reverse of the string.

MUST USE A WHILE LOOP
DO NOT USE STRING SLICING!!!

Sample Data string1 argument:
My String Data

Returns:
ataD gnirtS yM

CREATE A TEST CASE IN THE exam_test.py file.
'''
def reverse_string(string1):
    rev_string = ''
    index = len(string1)
    while index:
        index -= 1
        rev_string += string1[index]
    return rev_string




'''
10 points
Create a function named get_list_min_max with a list1 parameter that returns the min and max values
in a list.

Sample Data list1 value:
['joe', 10, 15, 20, 30, 40]

Returns:
[10, 40]

CREATE A TEST CASE IN THE exam_test.py file.
'''
def get_list_min_max(list1):
    val_list = []
    
    del list1[0]
    min_val = min(list1)
    max_val = max(list1)
    
    val_list.append(min_val)
    val_list.append(max_val)
    
    return val_list

'''
25 points
Create a function named get_list_min_max_file with no parameters that reads the attached quiz.dat file
that returns all the min and max values from multiple lists.

You can use the get_list_min_max to get the min max for each list.

Sample quiz.dat file data:

joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10 11
john 14 32 25 16 89

Return Value:
[2,89]

'''
def get_list_min_max_file():
    file = open('quiz.dat', 'r')
    return_list = []
    old_min = 999999
    old_max = 0
    for line in file:
        list1 = line.split()
        i = 0
        while i < len(list1):
            if list1[i].isdigit():
                list1[i] = int(list1[i])
            i += 1
        
        min_max_list = get_list_min_max(list1)
        
        new_min = int(min_max_list[0])
        
        new_max = int(min_max_list[1])
        
        if new_min < old_min:
            old_min = new_min
            
        if new_max > old_max:
            old_max = new_max
            
    return_list.append(old_min)
    return_list.append(old_max)
    file.close()
    return return_list
    


        
