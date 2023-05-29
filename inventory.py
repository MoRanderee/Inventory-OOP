
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return int(self.quantity)

    # def get_code(self):

    #     return self.code

    # def get_product(self):

    #     return self.product
    
    def get_info(self):
        
        info = [self.country, self.code, self.product, self.cost, self.quantity]
        return info

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"""
Country: {self.country}
Code: {self.code}
Product: {self.product}
Cost: {self.cost}
Quantity: {self.quantity}"""


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open("inventory.txt") as file:

            for line in file:

                temp = line.strip()
                temp = temp.split(",")

                if temp[0] == "Country":
                    pass

                else:
                    shoe = Shoe(temp[0], temp[1], temp[2], temp[3], temp[4])
                    shoe_list.append(shoe)

    except Exception as error:
            print("There was an error:")
            print(f"{error}. Please check data.")

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    read_shoes_data()
    country = input("Country located:")
    code = input("Shoe code:")
    product = input("Name of shoe:")
    cost = input("Cost of shoe:")
    quantity = input("Quantity of shoe:")

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

    with open("inventory.txt", "a") as file:

        file.write(f"\n{country},{code},{product},{cost},{quantity}")

    print("\nNew shoe has been added.")

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    read_shoes_data()

    for shoe in shoe_list:
        print(shoe)


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    read_shoes_data()
    
    low_quantity = shoe_list[0].get_quantity() 
    low_idx = 0

    for idx in range(len(shoe_list)):

        if shoe_list[idx].get_quantity() < low_quantity:
            low_quantity = shoe_list[idx].get_quantity()
            low_idx = idx

    low_shoe = shoe_list[low_idx]
    add_quantity = input(f"{low_shoe.product} in {low_shoe.country} has the lowest quantity of {low_shoe.quantity}, would you like to increase the quantity? (Y/N)\n")

    if add_quantity.lower() == "y":
        new_quantity = int(input("How many pairs would you like to add?\n"))
        new_quantity = new_quantity + low_quantity
    
        # info = shoe_list[low_idx].get_info()
        # shoe_list[low_idx] = Shoe(info[0], info[1], info[2], info[3], new_quantity)

        shoe_list[low_idx] = Shoe(low_shoe.country, low_shoe.code, low_shoe.product, low_shoe.cost, new_quantity)

        for shoe in shoe_list:
            print(shoe)

        with open("inventory.txt", "w") as file:

            file.write("Country,Code,Product,Cost,Quantity")

            for shoe in shoe_list:
                file.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")

        print("\nStock has been updated.")

    elif add_quantity.lower() == "n":
        pass

    else: 
        print("You have entered an invalid answer.")

def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    read_shoes_data()
    
    search_code = input("Enter the code of the shoe: ").upper()

    for shoe in shoe_list:

        if shoe.code == search_code:
            print(shoe)

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    read_shoes_data()

    for shoe in shoe_list:

        name = shoe.get_info()[2]
        value = int(shoe.get_cost()) * int(shoe.get_quantity())

        print(f"{name}: R{value}")


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    read_shoes_data()

    hi_quantity = shoe_list[0].get_quantity() 

    for shoe in shoe_list:

        if shoe.get_quantity() > hi_quantity:
            hi_quantity = shoe.get_quantity()
            name = shoe.product

        
    print(f"\n{name} is for sale!")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

option = ""

while option != "Q":

    try:
        option = input('''
Please select an option below:
VIEW: View all shoe data
ADD: Add new shoe to data
SEARCH: Search for a shoe
RESTOCK: Restock shoe with lowest quantity
HI: View shoe with highest quantity
VALUE: View value of each shoe
Q: Quit

''').upper()

        # quit program
        if option == "Q":
            break

        # capture new shoe
        elif option == "ADD":
            capture_shoes()
        
        # view all shoe data
        elif option == "VIEW":
            print("VIEWING")
            view_all()

        # restock shoe
        elif option == "RESTOCK":
            re_stock()
        
        # search for a shoe
        elif option == "SEARCH":
            seach_shoe()
        
        # find value of each shoe
        elif option == "VALUE":
            print("")
            value_per_item()
        
        # find shoe with most quantity
        elif option == "HI":
            highest_qty()
        
        else:
            raise Exception("You have entered an invalid option")

    except Exception as error:
        print("There was an error:")
        print(f"{error}. Please try again.")

