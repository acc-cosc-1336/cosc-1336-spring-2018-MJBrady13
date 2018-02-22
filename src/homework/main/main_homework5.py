#write the import statements for homework5 functions
from homework5 import write_sales_data
from homework5 import read_sales_data
#With the functions created in homework5...
#Prompt user for number of sales records to input.
#Open a file for text writing.
#Iterate and prompt user for item name and price.
#Save item name and price to file in one line
#Calculate sum of price and write to file
#Calculate average price and write to file

#Open a file for text reading.
#Read the saved file and output table

def main():
    num_sales = int(input("Enter number of sales: "))

    file_object = open('sales_table.txt', 'w')

    total = 0.0
    avg_price = 0.0
    item = ''

    for index in range(1, num_sales+1):
        print ('Enter the name for item #',index)
        item = input(':')
        print ('Enter the price for item #', index)
        price = input(':')
        price = str(price)
        write_sales_data(file_object, item, price)
        price = float(price)
        total += price

    item = "Total"
    write_sales_data(file_object, item, total)

    item = "Avg Price"
    avg_price = total/num_sales
    avg_price = str(round(avg_price, 2))
    write_sales_data(file_object, item, avg_price)

    file_object.close()

    file_object = open('sales_table.txt', 'r')
    read_sales_data(file_object)

main()
