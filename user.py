import getpass


list1 = []

class Seller():
    
    def __init__(self,Name,City,Vehicle_type):
        self.name = Name
        self.city = City
        self.vehicle_type = Vehicle_type
        
    def user(self):
       print(f"Enter your {self.name}: ")
       print(f"Enter the {self.city}")
       print(f"Enter the {self.vehicle_type}")
       
def Register():
        
    username = input("\nCreate your Username: ")    
    password = input("Create your Password: ") 
    data = username,password 
    list1.append(data) 
        
    print("\n****** Register Successfully ******\n")
        
        
        
def Login():
        
    # while True:
        User = input("\nEnter your Username: ")
        Password = input("Enter your Password: ")
        for i in list1:
            if User == i[0]:
                if Password == i[1]:
                    print("\n****** Login Successful ******\n")
                else:
                    print("\nInvalid Password or not Exist:\n")
            else :
                print("\nUser not exist or invalid Username\n")
                break
        else:
            return Register
        
                    
        
            
        

obj1 =Seller(input("Enter your Name: "),input("Enter your City: "),input("Write the Vehicle type: "))
print(obj1)



