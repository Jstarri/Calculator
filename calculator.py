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

def cube_volume(x):
  return x **3

def rectangle_area(x, y):
  return x * y

def r_prism_volume(x, y, z):
  return x * y * z

def triangle_area(x, y):
  return 0.5(x * y)

def pyramid_volume(x, y, z):
  return (1/3) * (x * y) * z

def circle_area(x):
  return 3.14(x **2)

def sphere_volume(x):
  return (4/3) * 3.14 * (x **3)

def bill_split(x, y):
  return x / y

def bill_tip(x, y):
  return x * (y * 0.01)
  
print("Welcome to AJ's Calculator")
print("Choose your Calculator Style: ")
while True:
  style_choice = input("Enter choice: A - Basic Calculations; B - Exponents, Roots & Logs; C - Areas of Shapes; D - Bill Calculator: ")
  if style_choice == 'A':
    print("Select operation.")
    print("A: Add")
    print("B: Subtract")
    print("C: Multiply")
    print("D: Divide")

    basic_choice = input("Enter choice(A/B/C/D): ")

    if basic_choice == 'A':
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      print(num1, "+", num2, "=", add(num1, num2))
      
    elif basic_choice == 'B':
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      print(num1, "-", num2, "=", subtract(num1, num2))
      
    elif basic_choice == 'C':
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      print(num1, "*", num2, "=", multiply(num1, num2))
      
    elif basic_choice == 'D':
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      print(num1, "/", num2, "=", divide(num1, num2))

  if style_choice == 'B':
    print("Select operation.")
    print("A: Exponent")
    print("B: Square Root")
    print("C: Cube Root")
    print("D: Natural Log")
    print("E: Base Log")

    basic_choice = input("Enter choice(A/B/C/D): ")

    if basic_choice == 'A':
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      print(num1, "to the power of", num2, "=", exponent(num1, num2))
        
    elif basic_choice == 'B':
      num3 = float(input("Enter number: "))
      print("The square root of", num3, "is", square_root(num3))
        
    elif basic_choice == 'C':
      num3 = float(input("Enter number: "))
      print("The cube root of", num3, "is", cube_root(num3))
        
    elif basic_choice == 'D':
      num3 = float(input("Enter number: "))
      print("The natural logarithm of", num3, "=", nat_log(num3))
    
    elif basic_choice == 'E':
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      print("The logarithm base", num2, "of", num1, "=", base_log(num1, num2))

  if style_choice == 'C':
    print("Select operation.")
    print("A: Area of Square")
    print("B: Area of Rectangle")
    print("C: Area of Triangle")
    print("D: Area of Circle")
    print("E: Volume of Cube")
    print("F: Volume of Rectangular Prism")
    print("G: Volume of Pyramid")
    print("H: Volume of Sphere")

    basic_choice = input("Enter choice(A/B/C/D/E/F/G/H): ")

    if basic_choice == 'A':
      num1 = float(input("Enter side length: "))
      print("The area of a square with a length of", num1, "inches, and a height of", num1, "inches =", square_area(num1))
      
    elif basic_choice == 'B':
      num1 = float(input("Enter length: "))
      num2 = float(input("Enter height: "))
      print("The area of a rectangle with a length of", num1, "inches, and a height of", num2, "inches =", rectangle_area(num1, num2))
        
    elif basic_choice == 'C':
      num1 = float(input("Enter base length: "))
      num2 = float(input("Enter height: "))
      print("The area of a triangle with a base length of", num1, "inches, and a height of", num2, "inches =", triangle_area(num1, num2))
        
    elif basic_choice == 'D':
      num1 = float(input("Enter radius: "))
      print("The area of a circle with a radius of", num3, "inches =", circle_area(num3))

    if basic_choice == 'E':
      num1 = float(input("Enter side length: "))
      print("The volume of a cube with a length of", num3, ", a height of", num3, ", & a width of", num3, "=", cube_volume(num3))
    
    if basic_choice == 'F':
      num1 = float(input("Enter length: "))
      num2 = float(input("Enter height: "))
      num3 = float(input("Enter width: "))
      print("The volume of a rectangular prism with a length of", num1, ", a height of", num2, ", & a width of", num3, "=", r_prism_volume(num1, num2, num3))
    
    if basic_choice == 'G':
      num1 = float(input("Enter base length: "))
      num2 = float(input("Enter base width: "))
      num3 = float(input("Enter height: "))
      print("The volume of a cube with a base length of", num1, ", a base width of", num2, ", & a height of", num3, "=", pyramid_volume(num1, num2, num3))
    
    if basic_choice == 'H':
      num1 = float(input("Enter radius: "))
      print("The volume of a sphere with a radius of", num1, "=", sphere_volume(num1))

  if style_choice == 'D':
    print("Select operation.")
    print("A: Splitting the Bill")
    print("B: Tipping by Percentage")

    basic_choice = input("Enter choice(A/B): ")

    if basic_choice == 'A':
      num1 = float(input("Enter the number of people: "))
      num2 = float(input("Enter thee price of the bill: "))
      print("If you go to a restaurant with", num1 - 1, "other people and the bill is worth", num2, "dollars, then each person will pay", bill_split(num2, num1), "dollars")
        
    elif basic_choice == 'B':
      num1 = float(input("Enter the price of the bill: "))
      num2 = float(input("Enter the perecentage you want to tip: "))
      print("If you go to a restaurant and the bill is worth", num1, "dollars, and you want to tip,", num2, "%, then the tip will be worth", bill_tip(num1, num2), "dollars")

  next_calculation = input("Let's do another calculation? (yes/no): ")
  if next_calculation == 'yes':
    continue
  if next_calculation == 'no':
    print("Goodbye!")
    break