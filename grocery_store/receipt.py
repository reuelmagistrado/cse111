# import csv module to read csv file
import csv
# import the datetime class from the datetime module so that it can be used in this program
from datetime import datetime

def main():
    
    try:
        # Index of the product number column in the products.csv file.
        PRODUCT_NUM_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        PRODUCT_PRICE_INDEX = 2
        # Read the contents of the products.csv into a compound dictionary named products_dict. Use the product numbers as the keys in the dictionary.
    
        products_dict = read_dict("grocery_store\products.csv", PRODUCT_NUM_INDEX)  
    
        # Print products_dict
        print(products_dict)

    

        REQUESTED_QUANTITY_INDEX = 1
        # Open requests.csv file for reading
        with open("grocery_store/request.csv", "rt") as csv_file:

            # Use the csv module to create a reader object that will read from the opened CSV file.
            reader = csv.reader(csv_file)

            # Use the requested product number to find the corresponding item in the products_dict.
            # Print the product name, requested quantity, and product price.


            next(reader)

            num_of_items = 0
            sub_total = 0.0

            SALES_TAX_RATE = 0.06
            DISCOUNT_PRICE = .1
            STORE_NAME = "Inkom Emporium"

            current_date_and_time = datetime.now()

            

            # Print the name of the store
            print()
            print(f"{STORE_NAME}")
            print()
            for row_list in reader:

                # Get the product number in the request.csv file
                product_num = row_list[PRODUCT_NUM_INDEX]

                # Get the product name in the products dictionary
                product_name = products_dict[product_num][PRODUCT_NAME_INDEX]

                # Get the requested quantity in the request.csv file
                requested_quantity = int(row_list[REQUESTED_QUANTITY_INDEX])

                # Get the product price in the products dictionary
                product_price = float(products_dict[product_num][PRODUCT_PRICE_INDEX])

                
                # Apply 10% discount if the day is Tuesday or Wednesday
                if current_date_and_time.weekday() == 1 or 2:
                    product_price -= (product_price * DISCOUNT_PRICE)

                # Compute the number of ordered items
                num_of_items += requested_quantity

                # Sum the subtotal due
                sub_total += (product_price * requested_quantity)

                # Print the list of ordered items
                print(f"{product_name}: {requested_quantity} @ {product_price}")
            
            # Compute the sales tax amount
            sales_tax_amount = sub_total * SALES_TAX_RATE

            # Compute the total amount due
            total = sub_total + sales_tax_amount

            print()
            # Print the number of ordered items
            print(f"Number of Items: {num_of_items}")

            # Print the subtotal due
            print(f"Subtotal: {sub_total:.2f}")

            # Print the sales tax amount
            print(f"Sales Tax: {sales_tax_amount:.2f}")

            # Print the total amount due
            print(f"Total: {total:.2f}")
            print()

            # Print a thank you message
            print(f"Thank you for shopping at the {STORE_NAME}.")

            # Print the current day of the week and the current time.
            print(f"{current_date_and_time:%a %b  %d %I:%M:%S %Y}")
            print()
            
    # Prints error message if csv files aren't found 
    except FileNotFoundError as file_err:
        print()
        print("Error: missing file")
        print(file_err)
        print()
    
    # Prints error message if user has no permission to view the file
    except PermissionError as permission_err:
        print()
        print("Error: you don't have permission")
        print(permission_err)
        print()

    # Prints error message if key is not found in the dictionary
    except KeyError as key_err:
        print()
        print("Error: unknown product ID in the request.csv file")
        print(key_err)
        print()


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Create an empty dictionary that will store the data from the CSV file.
    products_dictionary = {}

    # Open the CSV file for reading and store a reference to the opened file in a variable named csv_file

    with open(filename, "rt") as csv_file:
        
        # Use the csv module to create a reader object that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]
                
                # Store the data from the current
                # row into the dictionary.
                products_dictionary[key] = row_list

    return products_dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()