"""
Program created to read a file that is assumed to contain words
"""
# filename: print_numbers.py
import sys
import time
import json


class Product():
    '''
    Class to store product information
    '''
    def __init__(self):
        self._title = None
        self._product_type = None
        self._description = None
        self._filename = None
        self._height = None
        self._width = None
        self._price = None
        self._rating = None

    def __str__(self):
        return (
            f"{self.title} {self.product_type} "
            f"{self.description} {self.filename} "
            f"{self.height} {self.width} "
            f"{self.price} {self.rating}"
        )

    @staticmethod
    def from_json(json_object):
        '''
        Static factory method to map json to object
        '''
        product = Product()

        product.title = json_object['title']
        product.product_type = json_object['type']
        product.description = json_object['description']
        product.filename = json_object['filename']
        product.height = json_object['height']
        product.width = json_object['width']
        product.price = json_object['price']
        product.rating = json_object['rating']

        return product

    @property
    def title(self):
        '''
        Method to get the title of the object
        '''
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def product_type(self):
        '''
        Method to get the product type of the object
        '''
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value

    @property
    def description(self):
        '''
        Method to get the description of the object
        '''
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def filename(self):
        '''
        Method to get the filename of the object
        '''
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    @property
    def height(self):
        '''
        Method to get the height of the object
        '''
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        '''
        Method to get the width of the object
        '''
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def price(self):
        '''
        Method to get the price of the object
        '''
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def rating(self):
        '''
        Method to get the rating of the object
        '''
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value


class Sale():
    '''
    Class to store product information
    '''
    def __init__(self):
        self._sale_id = None
        self._sale_date = None
        self._product = None
        self._quantity = None

    def __str__(self):
        return (
            f"{self.sale_id} {self.sale_date} "
            f"{self.product} {self.quantity}"
        )

    @staticmethod
    def from_json(json_object):
        '''
        Static factory method to map json to object
        '''
        sale = Sale()

        sale.sale_id = json_object['SALE_ID']
        sale.sale_date = json_object['SALE_Date']
        sale.product = json_object['Product']
        sale.quantity = json_object['Quantity']

        return sale

    @property
    def sale_id(self):
        '''
        Method to get the sale id of the object
        '''
        return self._sale_id

    @sale_id.setter
    def sale_id(self, value):
        self._sale_id = value

    @property
    def sale_date(self):
        '''
        Method to get the sale date of the object
        '''
        return self._sale_date

    @sale_date.setter
    def sale_date(self, value):
        self._sale_date = value

    @property
    def product(self):
        '''
        Method to get the product of the object
        '''
        return self._product

    @product.setter
    def product(self, value):
        self._product = value

    @property
    def quantity(self):
        '''
        Method to get the quantity of the object
        '''
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


class SalesArray(list):
    """
    Custom class which extends list and
    does required computation of it's elements
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._total_cost = None

    def __str__(self):
        return (
            f"TOTAL\n"
            f"{self.get_total_cost()}"
        )

    def calculate_total_cost(self, product_dict):
        """
        Method used to calculate the total cost
        Based on the provided product dictionary
        """
        total_cost = 0

        for sale in self:
            if sale.product not in product_dict:
                print(
                    f"El producto '{sale.product}' del archivo ventas "
                    f"no existe en el archivo de productos"
                )
            else:
                product = product_dict.get(sale.product)
                transaction_cost = product.price * sale.quantity
                total_cost = total_cost + transaction_cost

        self._total_cost = total_cost

    def get_total_cost(self):
        """
        Method used to get the word frequency dictionary of the class
        """
        return self._total_cost


def print_numbers(path_to_products_file, path_to_sales_file):
    """
    Method to print the numbers that the file contains
    """
    start_time = time.time()
    product_list_json = None
    sale_list_json = None
    try:
        with open(path_to_products_file, 'r', encoding="utf-8") as file:
            product_list_json = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{path_to_products_file}' not found.")

    try:
        with open(path_to_sales_file, 'r', encoding="utf-8") as file:
            sale_list_json = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{path_to_sales_file}' not found.")

    product_list = list(map(Product.from_json, product_list_json))
    sale_list = list(map(Sale.from_json, sale_list_json))

    product_dict = dict((product.title, product) for product in product_list)
    sale_array = SalesArray(sale_list)

    sale_array.calculate_total_cost(product_dict)

    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000

    print(sale_array)
    print("\n")
    execution_time_result = (
        f"Time of execution: {elapsed_time_ms:.6f} milliseconds"
    )
    print(execution_time_result)
    with open("SalesResults.txt", "w", encoding="utf-8") as file:
        # Print the object to the file using the print function
        print(sale_array, file=file)
        print("\n", file=file)
        print(execution_time_result, file=file)


if __name__ == "__main__":
    # Check if a file path is provided as a command line argument
    if len(sys.argv) != 3:
        print(
            "Usage: python computeSales.py "
            "priceCatalogue.json salesRecord.json"
        )
        sys.exit(1)

    # Get the file path from the command line argument
    path_to_products = sys.argv[1]
    path_to_sales = sys.argv[2]

    # Print the numbers from the file
    print_numbers(path_to_products, path_to_sales)
