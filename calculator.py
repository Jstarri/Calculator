import math

def add(x, y):
  return x + y
  
def subtract(x, y):
  return x - y
  
def multiply(x, y):
  return x * y
  
def divide(x, y):
  return x / y

def remainder(x, y):
  return x % y
 
def exponent(x, y):
  return x ** y

def square_root(x):
  return math.sqrt(x)

def cube_root(x):
  return x ** (1./3)

def nat_log(x):
  return math.log(x)

def base_log(x, y):
  return math.log(x, y)

def square_area(x):
  return x ** 2

def rectangle_area(x, y):
  return x * y

def triangle_area(x, y):
  return 0.5 * (x * y)

def circle_area(x):
  return 3.14 * (x **2)

def slope_intercept(x, y, z):
  return (x * y) + z

print("Welcome to AJ's Calculator")  
print("Select your operation.")
print("A: Add")
print("B: Subtract")
print("C: Multiply")
print("D: Divide")
print("E: Exponent")
print("F: Square Root")
print("G: Cube Root")
print("H: Natural Log")
print("I: Base Log")
print("J: Area of Square")
print("K: Area of Rectangle")
print("L: Area of Triangle")
print("M: Area of Circle")
print("N: Slope-Intercept Formula")

while True:
  choice = input("Enter choice(A/B/C/D/E/F/G/H/I/J/K/L/M/N): ")

  #Part for three-number calculations
  if choice in ('N'):
    num4 = float(input("Enter your first number: "))
    num5 = float(input("Enter your second number: "))
    num6 = float(input("Enter your third number: ")) 
  
  if choice == 'N':
    print("The answer to y = (", num4, "*", num5, ") +", num6, "=", slope_intercept(num4, num5, num6))

  #Part for two-number calculations
  if choice in ('A', 'B', 'C', 'D', 'E', 'I', 'K', 'L'):
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
  
  if choice == 'A':
    print(num1, "plus", num2, "=", add(num1, num2))
      
  elif choice == 'B':
    print(num1, "minus", num2, "=", subtract(num1, num2))
      
  elif choice == 'C':
    print(num1, "times", num2, "=", multiply(num1, num2))
      
  elif choice == 'D':
    print(num1, "divided by", num2, "=", divide(num1, num2), "with a remainder of", remainder(num1, num2))
    
  elif choice == 'E':
    print(num1, "to the power of", num2, "=", exponent(num1, num2))
  
  elif choice == 'I':
    print("The logarithm base", num2, "of", num1, "=", base_log(num1, num2))
  
  elif choice == 'K':
    print("The area of a rectangle with a length of", num1, "and a width of", num2, "=", rectangle_area(num1, num2))
  
  elif choice == 'L':
    print("The area of a triangle with a base length of", num1, "and a height of", num2, "=", triangle_area(num1, num2))

  #Part for one-number calculations
  elif choice in ('F', 'G', 'H', 'J', 'M'):
    num3 = float(input("Enter your number: "))

  if choice == 'F':
    print("The square root of", num3, "is", square_root(num3))

  elif choice == 'G':
    print("The cube root of", num3, "is", cube_root(num3))
  
  elif choice == 'H':
    print("The natural logarithm of", num3, "=", nat_log(num3))
  
  elif choice == 'J':
    print("The area of a square with a length of", num3, "and a width of", num3, "=", square_area(num3))
  
  elif choice == 'M':
    print("The area of a circle with a radius of", num3, "=", circle_area(num3))

    
  next_calculation = input("Let's do another calculation? (yes/no): ")
  if next_calculation == 'yes':
    continue
  if next_calculation == 'no':
    print("Goodbye!")
    break
      
  else:
    print("Invalid Input")