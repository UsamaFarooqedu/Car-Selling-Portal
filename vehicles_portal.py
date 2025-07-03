import getpass



class Store:
    def __init__(self):
        
        self.details_list = []  # Renamed to avoid confusion with method name

    def add_details(self, name, model, color, price):
        # Store vehicle details in a dictionary and add it to the list
        detail = {
            "name": name,
            "model": model,
            "color": color,
            "price": price
        }
        self.details_list.append(detail)

    def Show(self):
        
        print("\n***** Welcome in Store *****\n")
        
        for detail in self.details_list:
            
            print(f"Vehicle: {detail['name']}")
            print(f"Model: {detail['model']}")
            print(f"Color: {detail['color']}")
            print(f"Price: {detail['price']}\n")
            
class Sell(Store):
    def __init__(self):
        super().__init__()
        self.username = getpass.getuser()
        self.password = getpass.getpass("Enter your password: ")
        print(f"Welcome {self.username} to the Vehicle Store!")

    


class Buy(Store):
    # Inherits from Store, no additional properties needed
    def __init__(self):
        super().__init__()
        self.username = getpass.getuser()
        self.password = getpass.getpass("Enter your password: ")
        print(f"Welcome {self.username} to the Vehicle Store!")



# Main program to run the vehicle portal
print("\n Welcome to the Vehicle Portal!")
print("Please choose an option:")
print("1. Buy Vehicle")
print("2. Sell Vehicle")
choice = input("Enter your choice (1 or 2): ")
if choice == '1':
    store1 = Buy()
elif choice == '2':
    store1 = Sell()
else:
    print("Invalid choice. Exiting the program.")
    exit()

# Prompt for user credentials
store1.username = getpass.getuser()
store1.password = getpass.getpass("\n Enter your password: ")
print(f"\n Welcome {store1.username} to the Vehicle Store!")

# Create instances and add details
store1 = Sell()

# Add details for vehicles
store1.add_details(
    name=input("\n Enter Vehicle Name: "),
    model=input("Enter Model: "),
    color=input("Enter Color: "),
    price=input("Enter Price: ")
)

# Show details for each store
store1.Show()

