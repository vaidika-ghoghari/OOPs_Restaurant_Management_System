# --------- Base Class ---------

class MenuItem:

    def __init__(self, item_id, name, price, category, is_available=True):
        self.item_id = item_id
        self.name = name
        self.__price = price
        self.category = category
        self.__is_available = is_available

    # Getter for price
    def get_price(self):
        return self.__price

    # Setter for price
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price can't be negative.")

    # Getter for availability
    def get_availability(self):
        return self.__is_available

    # Setter for availability
    def set_availability(self, status):
        self.__is_available = status

    # Getter for item ID
    def get_id(self):
        return self.item_id

    # Display method
    def display(self):
        status = "Available" if self.__is_available else "Not Available"

        print(
            "\nMenu Item Details:\n"
            f"\nID : {self.item_id}\n"
            f"Name : {self.name}\n"
            f"Price : ₹{self.__price:.2f}\n"
            f"Category : {self.category}\n"
            f"Availability : {status}"
        )

    def get_total_price(self):
        return self.__price * self.quantity
# --------- Food Item Class ---------

class FoodItem(MenuItem):

   def __init__(self, item_id, name, price, category, spice_level, is_vegetarian=True):
        super().__init__(item_id,name,price,category)
        self.spice_level = spice_level
        self.is_vegetarian = is_vegetarian

    # Method overriding
   def display(self):
        super().display()

        print(
            f"Spice Level : {self.spice_level}\n"
            f"Vegetarian : {'Yes' if self.is_vegetarian else 'No'}"
        )


# --------- Beverage Class ---------

class Beverage(MenuItem):

    def __init__(self,item_id,name,  price,  category, is_available=True, is_alcoholic=False,volume_ml=0 ):
        super().__init__(item_id,name,  price,category, is_available)
        self.is_alcoholic = is_alcoholic
        self.volume_ml = volume_ml

    # Method overriding
    def display(self):
        super().display()

        print(
            f"Alcoholic : {'Yes' if self.is_alcoholic else 'No'}\n"
            f"Volume : {self.volume_ml} ml"
        )



menu_items = {}
ordered_items = {}


# --------- Main Program ---------

while True:


    print("\n\t=== RESTAURANT MANAGEMENT SYSTEM ===")
   

    print("\n1. Add a Food Item")
    print("2. Add a Beverage")
    print("3. Place an Order")
    print("4. Cancel an Order")
    print("5. Show Menu Details")
    print("6. Show All Orders")
    print("7. Update Item Availability")
    print("8. Generate Bill")
    print("9. Exit")

    choice = int(input("Enter your choice: "))


    # --------- Add food item ---------

    if choice == 1:

        print("\n--- Add Food Item ---")

        item_id = input("\nEnter Item ID: ")
        name = input("Enter Item Name: ")
        price = float(input("Enter Price: "))
        category = input("Enter Category: ")
        spice_level = input("Enter Spice Level: ")

        is_vegetarian = (
            input("Is Vegetarian (Yes/No): ")
            .strip()
            .lower() == "yes"
        )

        if item_id in menu_items:
            print("Item ID already exists!!!")

        else:

            food_item = FoodItem(item_id, name, price, category, spice_level, is_vegetarian)     
            menu_items[item_id] = food_item
            if isinstance(food_item, FoodItem):
                print("\nFood Item created successfully.")
                food_item.display()


    # --------- Add beverage ---------

    elif choice == 2:

        print("\n--- Add Beverage ---")

        item_id = input("\nEnter Item ID: ")
        name = input("Enter Item Name: ")
        price = float(input("Enter Price: "))
        category = input("Enter Category: ")

        is_alcoholic = (input("Is Alcoholic (Yes/No): ").strip().lower() == "yes")

        volume_ml = int(input("Enter Volume in ml: "))

        if item_id in menu_items:
            print("Item ID already exists!!!")

        else:

            beverage_item = Beverage( item_id, name, price,category,True, is_alcoholic, volume_ml)

            menu_items[item_id] = beverage_item

            if isinstance(beverage_item, Beverage):
                print("\nBeverage created successfully.")
                beverage_item.display()


    # --------- Place order ---------

    elif choice == 3:

        print("\n--- Place an Order ---")

        item_id = input("\nEnter Item ID to order: ")

        if item_id in menu_items:

            item = menu_items[item_id]

            if item.get_availability():

                quantity = int(input("Enter quantity: "))

                if item_id in ordered_items:
                    ordered_items[item_id].quantity += quantity
                else:
                    item.quantity = quantity
                    ordered_items[item_id] = item

                    print(
                        f"Order placed for "
                        f"{item.name} ({item.item_id})."
                    )

                print(
                    f"Added to bill. "
                    f"Price: ₹{item.get_total_price():.2f}"
                )

            else:
                print(
                    f"Sorry, {item.name} is currently not available."
                )

        else:
            print("Item ID not found in the menu.")


    # --------- Cancel Order ---------

    elif choice == 4:

        print("\n--- Cancel an Order ---")

        item_id = input("\nEnter Item ID to cancel: ")

        if item_id in ordered_items:

            item = ordered_items[item_id]
            item.quantity = quantity
            del ordered_items[item_id]

            print(
                f"Order for {item.name} "
                f"({item.item_id}) has been canceled."
                f"Refund Amount: ₹{item.get_total_price():.2f}"
                f"Number of items canceled: {item.quantity}"
            )

        else:
            print("This item is not currently ordered.")


    # --------- show Menu ---------

    elif choice == 5:

        print("\n--- Show Menu Details ---")


        if not menu_items:
            print("\nNo menu items available.")

        else:
            print("\n=== FOOD ITEMS ===")

            for item in menu_items.values():
                if isinstance(item, FoodItem):
                    item.display()
                    print("-" * 30)

            print("\n=== BEVERAGES ===")

            for item in menu_items.values():
                if isinstance(item, Beverage):
                    item.display()
                    print("-" * 30)

    # --------- Show all orders ---------

    elif choice == 6:

        print("\n--- Show All Orders ---")

        if not ordered_items:

            print("\nNo orders have been placed yet.")

        else:

            for item in ordered_items.values():

                item.display()

                print(f"\nQuantity : {item.quantity}")
                print(f"Total Price : ₹{item.get_total_price():.2f}")
                print("Order Status : Ordered")
                print("-" * 30)

    # --------- Update availability ---------

    elif choice == 7:

        print("\n--- Update Item Availability ---")

        item_id = input("\nEnter Item ID: ")

        if item_id in menu_items:

            item = menu_items[item_id]

            print("1. Available")
            print("2. Not Available")

            status_choice = int(input("Enter your choice: "))

            if status_choice == 1:

                item.set_availability(True)

                print(
                    f"{item.name} is now available."
                )

            elif status_choice == 2:

                item.set_availability(False)

                print(
                    f"{item.name} is now not available."
                )

            else:
                print("Invalid choice.")

        else:
            print("Item ID not found in the menu.")


    # --------- Generate bill ---------

    elif choice == 8:

        print("\n--- Generate Bill ---")

        if not ordered_items:

            print("\nNo orders have been placed.")
            print("Total Bill Amount: ₹0.00")

        else:

            total_amount = 0.0

            print("\n\t--- BILL ---")

            for item in ordered_items.values():

                print(f"\n{item.name} ({item.item_id}) - \t₹{item.get_price():.2f} * {item.quantity} = ₹{item.get_total_price():.2f}")

                total_amount += item.get_total_price()

            print("-" * 25)

            print(f"\nTotal Bill Amount: ₹{total_amount:.2f}")


    # --------- Exit ---------

    elif choice == 9:

        print("\nExiting the Restaurant Management System.")
        print("Thank you for using the system.")
        print("Goodbye!")

        break


    # --------- Invalid Choice ---------

    else:

        print("Invalid choice! Please enter a number from 1 to 9.")