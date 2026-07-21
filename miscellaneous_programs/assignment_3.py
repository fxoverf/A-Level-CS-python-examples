class Bird: #(a)(i)
    # DistancePerHour : float
    # Species : str
    # XPosition : float
    # YPosition : float

    def __init__(self, species, distancePerHour):
        self.__Species = species
        self.__DistancePerHour = distancePerHour
        self.__XPosition = 500.0
        self.__YPosition = 500.0

    def GetSpecies(self): #(a)(ii)
        return self.__Species

    def GetPosition(self): #(a)(iii)
        return "X = " + str(self.__XPosition) + " Y = " + str(self.__YPosition)

    def Move(self, direction, minutes): #(a)(iv)
        distance = (self.__DistancePerHour / 60) * minutes

        if direction == "N":
            self.__YPosition += distance
        elif direction == "S":
            self.__YPosition -= distance
        elif direction == "E":
            self.__XPosition += distance
        elif direction == "W":
            self.__XPosition -= distance

#main program

bird1 = Bird("Cockatiel", 71.0) #(b)
bird2 = Bird("Macaw", 56.0) #(b)

print(bird1.GetSpecies(), bird1.GetPosition()) #(c)(i)
print(bird2.GetSpecies(), bird2.GetPosition())

while True:
    choice = input("Select bird 1 or 2: ")
    if choice in ["1", "2"]:
        break

if choice == "1":
    selectedBird = bird1
else:
    selectedBird = bird2

while True:
    direction = input("Enter direction (N, S, E, W): ").upper()
    if direction in ["N", "S", "E", "W"]:
        break

while True:
    minutes = input("Enter minutes flown: ")
    if minutes.isdigit():
        minutes = int(minutes)
        break

selectedBird.Move(direction, minutes)

print("Updated position:", selectedBird.GetPosition())

