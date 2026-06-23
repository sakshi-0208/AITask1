def chatbot():
    print("Welcome to StyleHub Fashion Store Chatbot!")
    print("Type 'help' to see available commands.\n")

    # Product database
    products = {
        "tshirt": 500,
        "jeans": 1200,
        "jacket": 2500,
        "kurti": 800,
        "saree": 1500,
        "hoodie": 1800,
        "shirt": 700,
        "dress": 1400,
        "shorts": 600
    }

    cart = []

    while True:
        user = input("\nYou: ").lower().strip()

        # EXIT
        if user == "exit":
            print("StyleHub: Thanks for visiting! Stay Stylish")
            break

        # HELP
        elif user == "help":
            print("""
  Commands:
- categories
- men
- women
- kids
- search <item>
- add <item>
- remove <item>
- view cart
- bill
- offers
- checkout
- exit
""")

        # GREETING
        elif user in ["hi", "hello", "hey"]:
            print("StyleHub: Hi! Welcome to your Fashion Store")

        # CATEGORIES
        elif user == "categories":
            print("Categories: Men, Women, Kids")

        # MEN SECTION
        elif user == "men":
            print("Men Collection: Tshirt, Jeans, Shirt, Hoodie, Shorts")

        # WOMEN SECTION
        elif user == "women":
            print("Women Collection: Kurti, Saree, Dress")

        # KIDS SECTION
        elif user == "kids":
            print("Kids Collection: Tshirt, Shorts, Hoodie")

        # SEARCH PRODUCT
        elif user.startswith("search"):
            item = user.replace("search", "").strip()
            if item in products:
                print(f"{item.title()} available for ₹{products[item]}")
            else:
                print("Product not found!")

        # ADD TO CART
        elif user.startswith("add"):
            item = user.replace("add", "").strip()
            if item in products:
                cart.append(item)
                print(f"🛒 {item.title()} added to cart.")
            else:
                print("Item not available.")

        # REMOVE FROM CART
        elif user.startswith("remove"):
            item = user.replace("remove", "").strip()
            if item in cart:
                cart.remove(item)
                print(f"🗑️ {item.title()} removed from cart.")
            else:
                print("Item not in cart.")

        # VIEW CART
        elif user == "view cart":
            if cart:
                print("Your Cart:")
                for item in cart:
                    print(f"- {item.title()} (₹{products[item]})")
            else:
                print("Your cart is empty!")

        # BILL
        elif user == "bill":
            if cart:
                total = sum(products[item] for item in cart)
                print("Bill Summary:")
                for item in cart:
                    print(f"- {item.title()} : ₹{products[item]}")
                print(f"Total Amount: ₹{total}")
            else:
                print("Cart is empty!")

        # OFFERS
        elif user == "offers":
            print("""
 Fashion Offers:
- Buy 2 Tshirts get 1 free
- Flat 40% off on Jeans
- 20% discount on Sarees
- Free shipping above ₹1500
""")

        # CHECKOUT
        elif user == "checkout":
            if cart:
                total = sum(products[item] for item in cart)
                print("Order Placed Successfully!")
                print(f"Total Paid: ₹{total}")
                print("Your stylish outfits are on the way!")
                cart.clear()
            else:
                print("Your cart is empty!")

        # DEFAULT RESPONSE
        else:
            print("Sorry, I didn't understand. Type 'help' for commands.")

# RUN CHATBOT
chatbot()