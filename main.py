class vehicle:

    def setmake(self, make):
        self.make = make

    def setmodel(self, model):
        self.model = model

class car(vehicle):
  
    def setdoors(self, doors):
        self.doors = doors

    def displayOptionOne(self):
        print()
        print(F"The make of the vehicle is: {self.make}")
        print(f"The model of the vehicle is: {self.model}")
        print(f"The number of doors are: {self.doors}")
        print("The car has been added to the garage")
        print()

class truck(vehicle):

    def setbed_length(self, bedlength):
        self.bed_length = bedlength

    def displayOptionTwo(self):
        print()
        print(F"The make of the vehicle is: {self.make}")
        print(f"The model of the vehicle is: {self.model}")
        print(f"The length of the bed is: {self.bed_length}")
        print("The truck has been added to the garage")
        print()

vehicle_choice = int(input("Please enter 1 for Car, 2 for Truck, or 3 to quit:"))

print()
#testing this out for GitHub

while vehicle_choice == 1 or 2:
  
  if vehicle_choice == 1:
    
    input_make = input("Please enter make of your car: ")
    input_model = input("Please enter the model of your car: ")
    input_doors = input("Pleae enter the number of doors on the car: ")

    new_car = car()
    new_car.setmake(input_make)
    new_car.setmodel(input_model)
    new_car.setdoors(input_doors)
    new_car.displayOptionOne()

    vehicle_choice = int(input("Please enter 1 for Car, 2 for Truck, or 3 to quit:"))
    
  elif vehicle_choice == 2:

    input_make = input("Please enter make of your truck: ")
    input_model = input("Please enter the model of your truck: ")
    input_bed_length = input("Please enter the length of the truck bed: ")

    new_truck = truck()
    new_truck.setmake(input_make)
    new_truck.setmodel(input_model)
    new_truck.setbed_length(input_bed_length)
    new_truck.displayOptionTwo()

    vehicle_choice = int(input("Please enter 1 for Car, 2 for Truck, or 3 to quit:"))

  elif vehicle_choice == 3:
      quit()
    
  