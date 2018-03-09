#write import statement for reverse string function
import unittest

from src.Midterm.exam import reverse_string
'''
10 points
Write a main function to ....
Loop as long as user types y.
Prompt user for a string (assume user will always give you good data).
Pass the string to the reverse string function and display the reversed string

'''
def main():
    again = 'y'
    while again == 'y' or again == 'Y':
        string1 = input('Enter a string')
        print(reverse_string(string1))
        again = input('Would you like to continue?')
main()
