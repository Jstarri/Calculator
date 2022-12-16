import math

def add(x, y):
  return x + y
  
def subtract(x, y):
  return x - y
  
def multiply(x, y):
  return x * y
  
def divide(x, y):
  return x / y
 
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
  return 0.5(x * y)

def circle_area(x):
  return 3.14(x **2)

def slope_intercept(x, y, z):
  return (x * y) + z

print("Welcome to AJ's Calculator")  
print("Select your operation.")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")
print("5: Exponent")
print("6: Square Root")
print("7: Cube Root")
print("8: Natural Log")
print("9: Base Log")
print("10: Area of Square")
print("11: Area of Rectangle")
print("12: Area of Triangle")
print("13: Area of Circle")
print("14: Slope-Intercept Formula")

while True:
  choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14): ")

  #Part for three-number calculations
  if choice in ('14'):
    num4 = float(input("Enter your first number: "))
    num5 = float(input("Enter your second number: "))
    num6 = float(input("Enter your third number: ")) 
  
  if choice == '14':
    print("The answer to y = (", num4, "*", num5, ") +", num6, "=", slope_intercept(num4, num5, num6))

  #Part for two-number calculations
  if choice in ('1', '2', '3', '4', '5', '9', '11', '12'):
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
  
  if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
      
  elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
      
  elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
      
  elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
    
  elif choice == '5':
    print(num1, "to the power of", num2, "=", exponent(num1, num2))
  
  elif choice == '9':
    print("The logarithm base", num2, "of", num1, "=", base_log(num1, num2))
  
  elif choice == '11':
    print("The area of a rectangle with a length of", num1, "and a width of", num2, "=", rectangle_area(num1, num2))
  
  elif choice == '12':
    print("The area of a triangle with a base length of", num1, "and a height of", num2, "=", triangle_area(num1, num2))

  #Part for one-number calculations
  elif choice in ('6', '7', '8', '10', '13'):
    num3 = float(input("Enter your number: "))

  if choice == '6':
    print("The square root of", num3, "is", square_root(num3))

  elif choice == '7':
    print("The cube root of", num3, "is", cube_root(num3))
  
  elif choice == '8':
    print("The natural logarithm of", num3, "=", nat_log(num3))
  
  elif choice == '10':
    print("The area of a square with a length of", num3, "and a width of", num3, "=", square_area(num3))
  
  elif choice == '13':
    print("The area of a circle with a radius of", num3, "=", circle_area(num3))

    
  next_calculation = input("Let's do another calculation? (yes/no): ")
  if next_calculation == 'yes':
    continue
  if next_calculation == 'no':
    print("Goodbye!")
    break
      
  else:
    print("Invalid Input")