'''
elena corpus
program 12
csci 161
'''

class BMW():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def startEngine(self):
        print("The engine is now on")

    def stopEngine(self):
        print("the engine is now off")


class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
    
    def display(self):
        if self.cruiseControlEnabled:
            print("Cruise Control is on")
        else:
            print("Cruise Control is off")
        
    def startEngine(self):
        super().startEngine()
        print("Buttom start is on." )


class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled 

    def display(self):
        if self.parkingAssistEnabled:
            print("Parking assist is on")
        else:
            print("Parking assist is off")
    

def print_three_series(car1):
    print()
    print("ThreeSeries...")
    print("This", car1.make, "is a", car1.model, "of", car1.year)
    car1.startEngine()
    car1.display()


def print_five_series(car2):
    print()    
    print("FiveSeries...")
    print("This", car2.make, "is a", car2.model, "of", car2.year)
    print('Starting engine...')    
    car2.startEngine()
    car2.display()
    


if __name__ == '__main__': 
    make = input("Enter The ThreeSeries Make: ")
    model = input('Enter Model: ')
    year = int(input("Enter Year: "))
    cruiseControl = input("Is cruise control on? (y/n): ")
    if cruiseControl == 'y':
        cruiseControlEnabled = True
    else:
        cruiseControlEnabled = False
    car1 = ThreeSeries(cruiseControlEnabled, make, model, year)
    
    print()
    make = input('Enter The FiveSeries Make: ')
    model = input('Enter Model: ')
    year = int(input("Enter Year: "))
    parkingAssist = input("Is cruise control on? (y/n): ")
    if parkingAssist == 'y':
        parkingAssistEnabled = True
    else:
        parkingAssistEnabled = False
    car2 = FiveSeries(parkingAssistEnabled, make, model, year)

    print_three_series(car1)
    print_five_series(car2)
