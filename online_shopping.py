# Online Shopping Cart (Basic Version)

products = {
    "1": {"name": "Laptop", "price": 50000},
    "2": {"name": "Phone", "price": 20000},
    "3": {"name": "Headphones", "price": 2000},
    "4": {"name": "Keyboard", "price": 1500}
}

cart = []

while True:
    print("\n===== ONLINE SHOPPING CART =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove from Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # View Products
    if choice == "1":
        print("\nAvailable Products:")
        for key, value in products.items():
            print(f'{key}. {value["name"]} - ₹{value["price"]}')

    # Add to Cart
    elif choice == "2":
        product_id = input("Enter Product ID to add: ")
        if product_id in products:
            cart.append(products[product_id])
            print("Product added to cart ✅")
        else:
            print("Invalid Product ID ❌")

    # View Cart
    elif choice == "3":
        if len(cart) == 0:
            print("Your cart is empty 🛒")
        else:
            print("\nItems in Cart:")
            total = 0
            for item in cart:
                print(f'{item["name"]} - ₹{item["price"]}')
                total += item["price"]
            print("Total Amount: ₹", total)

    # Remove from Cart
    elif choice == "4":
        name = input("Enter product name to remove: ")
        found = False
        for item in cart:
            if item["name"].lower() == name.lower():
                cart.remove(item)
                print("Product removed ✅")
                found = True
                break
        if not found:
            print("Product not found in cart ❌")

    # Checkout
    elif choice == "5":
        if len(cart) == 0:
            print("Cart is empty 🛒")
        else:
            total = 0
            for item in cart:
                total += item["price"]
            print("Total Bill: ₹", total)
            print("Thank you for shopping 🛍")
            cart.clear()

    # Exit
    elif choice == "6":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice ❌ Try again.")