class Car:
    def __init__(self, brand):
        self.brand = brand
        
    def start(self):
        print(f"My car brand name is {self.brand}")

# Create an object of the Car class
my_car = Car("Toyota")

# Print the brand
print(my_car.brand)

# Call the start method
my_car.start()
