from main import Products

try:
    product_price = input("Enter price of product \n")
    product_quantity = input("Enter quantity of the product \n")
    product_description = input("Enter description \n")
    product_colour = input("Add a colour \n")

    Products.create(prod_price=product_price, prod_quantity=product_quantity, prod_description=product_description, prod_colour=product_colour)
    print("Product saved successfully")
except:
    print("Faild to save product")