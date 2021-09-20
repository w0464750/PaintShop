import math

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

  #Taking input from user
  firstWallWidth = int(input("How many feet wide is your first wall?: "))
  secondWallWidth = int(input("How many feet wide is your second wall?: "))
  wallHeight = int(input("How many feet tall is your room?: "))

  #Using a formatted string to calculate the square footage of all 4 walls, and then using math.ceil to always round up to the nearest full can
  print(f'Your room has {2*firstWallWidth*wallHeight + 2*secondWallWidth*wallHeight} square feet of wall which requires {math.ceil((2*firstWallWidth*wallHeight + 2*secondWallWidth*wallHeight)/150)} cans to paint')

main()
