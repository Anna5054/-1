
catalog = {
    "MacBook":{
        "name": "MacBook",
        "price" : 33460.99,
        "amount" : 2
    },
    "Iphone":{
        "name": "Iphone",
        "price" : 22199.99,
        "amount" : 4
    },
    "AirPods":{
        "name": "AirPods",
        "price" : 11500.00,
        "amount" : 3
    },
    "AppleWatch":{
        "name": "AppleWatch",
        "price" : 5200.00,
        "amount" : 6
    }
}

admin_password = '123'
login_type = int(input("Login as administrator - 1, as guest - 2: "))
number = 0
cart = []

def add_cart_product(*args, **kwargs):
    cart_append = input('What u wanna add to cart? (If nothing - type "Ready"): ')
    if cart_append == "Ready" and cart == []:
        print("Cart is empty!")
    elif cart_append == "Ready" and cart != []:
        print(cart)
    elif cart_append == catalog[product]:
        cart.append(product)
        print("Cart: ", cart)
        add_cart_product(product, catalog[product]["price"], catalog[product]["amount"])
    return

if login_type == 1:
    password = input("Enter admin password: ")
    if password == admin_password:
        print("Login successful!\n=======Catalog=======")
        for product in catalog:
            print(f"{number}. {product}: {catalog[product]['price']}UAH, ({catalog[product]['amount']} in stock)")
elif login_type == 2:
    print("=======Catalog=======")
    for product in catalog:
        number = number + 1
        print(f"{number}. {product}: {catalog[product]['price']}UAH")
    add_cart_product(catalog[product]["name"], catalog[product]["price"], catalog[product]["amount"])

