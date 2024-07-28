# allowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'Ram 1500' ]
menu = f"""********************************
AutoCountry Vehicle Finder v0.5
********************************
Please Enter the following number below from the following menu:\n
1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit
********************************"""


def mainMenu(menu):
  print(menu)
  return menu


def selectChoice():
  choice = input("\nEnter Selection: ")
  return choice


def printCars(allowedVehiclesList):
  returnString = "\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
  print(returnString)
  returnString += "\n"
  for vehicle in allowedVehiclesList:
    print(vehicle)
    returnString += vehicle + "\n"
  return returnString


def searchVehicle(allowedVehiclesList):
  search = input("Please Enter the full Vehicle name: ")
  if search in allowedVehiclesList:
    print(f"{search} is an authorized vehicle")
  else:
    print(f"{search} is not an authorized vehicle, if you received this in error please check the spelling and try again")


def addCar(allowedVehiclesList):
  car = input("Please Enter the full Vehicle name you would like to add: ")
  if car not in allowedVehiclesList:
    allowedVehiclesList.append(car)
    with open("list.txt", "a") as vehiclesList:
      vehiclesList.write(car + "\n")
    print(f'You have added "{car}" as an authorized vehicle')
  else:
    print(f'"{car}" is already authorized')


def removeCar(allowedVehiclesList):
  delCar = input("Please Enter the full Vehicle name you would like to REMOVE: ")
  if delCar in allowedVehiclesList:
    confirm = input(f'Are you sure you want to remove "{delCar}" from the Authorized Vehicles List? \n').lower()
    if confirm == "yes":
      allowedVehiclesList.remove(delCar)
      print(f'You have REMOVED "{delCar}" as an authorized vehicle')
      with open("list.txt", "w") as vehiclesList:
        for car in allowedVehiclesList:
          vehiclesList.write(car + "\n")
    elif confirm == "no":
      None
    else:
      print("Please enter yes or no")
  else:
      print(f'"{delCar}" is not on the Authorized Vehicles List, if you received this in error please check the spelling and try again')


def main(allowedVehiclesList, menu):
  while True:
    mainMenu(menu)
    choice = selectChoice()
    if choice == "1":
      printCars(allowedVehiclesList)
    elif choice == "2":
      searchVehicle(allowedVehiclesList)
    elif choice == "3":
      addCar(allowedVehiclesList)
    elif choice == "4":
      removeCar(allowedVehiclesList)
    elif choice == "5":
      exitString = "\nThank you for using the AutoCountry Vehicle Finder, good-bye!"
      print(exitString)
      return exitString  
    else:
      print("\nPlease enter a number from the menu.\n")


if __name__ == "__main__":
  with open("list.txt","r") as vehiclesList:
    allowedVehiclesList = vehiclesList.read().splitlines()
  main(allowedVehiclesList, menu)