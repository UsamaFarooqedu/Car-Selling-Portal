from user import Seller,Register,Login
from vehicles_portal import Store,Sell,Buy






def main():
    
    print("\n******** Welcome in Car's Store ********\n")
    while True:
        print("Select (1) for Register:")
        print("Select (2) for Login:")
        print("Select (3) for Visit Store:")
        print("Select (4) for Buy:")
        print("Select (5) for Sell:")
        print("Select (6) for Exit:")
        
        choice = input("\nSelect the Number: ")
        
        if (choice == "1"):
            Register()
        elif (choice == "2"):
            Login()
        elif (choice == "3"):
            Store.Show()
        elif (choice == "4"):
            Buy.Visit()
        elif (choice == "5"):
            Sell.Visit()
        elif (choice == "6"):
            break
        else:
            print("Invalid Selection; Please try again: ")
            
    

if __name__=='__main__':
    main()