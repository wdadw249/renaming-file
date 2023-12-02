import os

source = "C:/Users/Sayed/Downloads/spaceShipes.png"
destination = "C:/Users/Sayed/Downloads/newSpaceShip.png"

os.rename(source, destination)
print("File got renamed sucessfully!!")
