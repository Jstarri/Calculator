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

def square_perimeter(x):
  return x * 4

def cube_volume(x):
  return x **3

def cube_s_area(x):
  return 6 * (x ** 2)

def rectangle_area(x, y):
  return x * y

def rectangle_perimeter(x, y):
  return (x + y) * 2

def r_prism_volume(x, y, z):
  return x * y * z

def r_prism_s_area(x, y, z):
  return 2 * ((y * x) + (z * x) + (z * y))

def triangle_area(x, y):
  return 0.5 * (x * y)

def pyramid_volume(x, y, z):
  return (1/3) * (x * y) * z

def circle_area(x):
  return 3.14 * (x **2)

def circle_circumference(x):
  return (3.14 * 2) * x

def sphere_volume(x):
  return (4/3) * 3.14 * (x **3)

def sphere_s_area(x):
  return (4 * 3.14) * (x ** 2)

def bill_split(x, y):
  return x / y

def bill_tip(x, y):
  return x * (y * 0.01)

def point_slope(w, x, y, z):
  return (z-x)/(y-w)
  
print("Welcome to AJ's Calculator")
print("Choose your Calculator Style: ")
while True:
  style_choice = input("Enter choice: A - Basic Calculations; B - Exponents, Roots & Logs; C - Shapes & Slopes; D - Bill Calculator: ")
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
    print("A: 2d Shapes")
    print("B: 3d Shapes")

    shape_choice = input("Enter choice(A/B): ")

    if shape_choice == 'A':
      print("A: Area of Square")
      print("B: Perimeter of Square")
      print("C: Area of Rectangle")
      print("D: Perimeter of Rectangle")
      print("E: Area of Triangle")
      print("F: Area of Circle")
      print("G: Circumference of Circle")
      print("H: Point Slope Equation")

      basic_choice_1 = input("Enter choice(A/B/C/D/E/F/G/H): ")

      if basic_choice_1 == 'A':
        num1 = float(input("Enter side length: "))
        unit = input("Enter unit of measurement: ")
        print("The area of a square with a length of", num1, unit,", and a height of", num1, unit," =", square_area(num1), unit)
      
      elif basic_choice_1 == 'B':
        num1 = float(input("Enter side length: "))
        unit = input("Enter unit of measurement: ")
        print("The perimeter of a square with a length of", num1, unit,", and a height of", num1, unit," =", square_perimeter(num1), unit)
      
      elif basic_choice_1 == 'C':
        num1 = float(input("Enter length: "))
        num2 = float(input("Enter height: "))
        unit = input("Enter unit of measurement: ")
        print("The area of a rectangle with a length of", num1, unit,", and a height of", num2, unit," =", rectangle_area(num1, num2), unit)

      elif basic_choice_1 == 'D':
        num1 = float(input("Enter length: "))
        num2 = float(input("Enter height: "))
        unit = input("Enter unit of measurement: ")
        print("The perimeter of a rectangle with a length of", num1, unit,", and a height of", num2, unit," =", rectangle_perimeter(num1, num2), unit)
        
      elif basic_choice_1 == 'E':
        num1 = float(input("Enter base length: "))
        num2 = float(input("Enter height: "))
        unit = input("Enter unit of measurement: ")
        print("The area of a triangle with a base length of", num1, unit,", and a height of", num2, unit," =", triangle_area(num1, num2), unit)
        
      elif basic_choice_1 == 'F':
        num1 = float(input("Enter radius: "))
        unit = input("Enter unit of measurement: ")
        print("The area of a circle with a radius of", num3, unit," =", circle_area(num3), unit)
      
      elif basic_choice_1 == 'G':
        num1 = float(input("Enter radius: "))
        unit = input("Enter unit of measurement: ")
        print("The area of a circle with a radius of", num3, unit," =", circle_circumference(num3), unit)

      elif basic_choice_1 == 'H':
        num1 = float(input("Enter value for x1: "))
        num2 = float(input("Enter value for y1: "))
        num3 = float(input("Enter value for x2: "))
        num4 = float(input("Enter value for y2: "))
        print("The slope of the line between (", num1, ",", num2, ") and (", num3, ",", num4, ") =", point_slope(num1, num2, num3, num4))

    if shape_choice == 'B':
      print("A: Volume of Cube")
      print("B: Surface Area of Cube")
      print("C: Volume of Rectangular Prism")
      print("D: Surface Area of Rectangular Prism")
      print("E: Volume of Pyramid")
      print("F: Volume of Sphere")
      print("G: Surface Area of Sphere")

      basic_choice_2 = input("Enter choice(A/B/C/D/E/F/G): ")

      if basic_choice_2 == 'A':
        num1 = float(input("Enter side length: "))
        unit = input("Enter unit of measurement: ")
        print("The volume of a cube with a length of", num1, unit,", a height of", num1, unit,", & a width of", num1, unit," =", cube_volume(num1), unit)
      
      if basic_choice_2 == 'B':
        num1 = float(input("Enter side length: "))
        unit = input("Enter unit of measurement: ")
        print("The volume of a cube with a length of", num1, unit,", a height of", num1, unit,", & a width of", num1, unit," =", cube_s_area(num1), unit)
    
      if basic_choice_2 == 'C':
        num1 = float(input("Enter length: "))
        num2 = float(input("Enter height: "))
        num3 = float(input("Enter width: "))
        unit = input("Enter unit of measurement: ")
        print("The volume of a rectangular prism with a length of", num1, unit,", a height of", num2, unit,", & a width of", num3, unit," =", r_prism_volume(num1, num2, num3), unit)
      
      if basic_choice_2 == 'D':
        num1 = float(input("Enter length: "))
        num2 = float(input("Enter height: "))
        num3 = float(input("Enter width: "))
        unit = input("Enter unit of measurement: ")
        print("The surface area of a rectangular prism with a length of", num1, unit,", a height of", num2, unit,", & a width of", num3, unit," =", r_prism_s_area(num1, num2, num3), unit)
    
      if basic_choice_2 == 'E':
        num1 = float(input("Enter base length: "))
        num2 = float(input("Enter base width: "))
        num3 = float(input("Enter height: "))
        unit = input("Enter unit of measurement: ")
        print("The volume of a pyramid with a base length of", num1, unit,", a base width of", num2, unit,", & a height of", num3, unit," =", pyramid_volume(num1, num2, num3), unit)
    
      if basic_choice_2 == 'F':
        num1 = float(input("Enter radius: "))
        unit = input("Enter unit of measurement: ")
        print("The volume of a sphere with a radius of", num1, unit," =", sphere_volume(num1), unit)
      
      if basic_choice_2 == 'G':
        num1 = float(input("Enter radius: "))
        unit = input("Enter unit of measurement: ")
        print("The surface area of a sphere with a radius of", num1, unit," =", sphere_s_area(num1), unit)
    

  if style_choice == 'D':
    print("Select operation.")
    print("A: Splitting the Bill")
    print("B: Tipping by Percentage")

    basic_choice = input("Enter choice(A/B): ")

    if basic_choice == 'A':
      num1 = float(input("Enter the number of people: "))
      num2 = float(input("Enter the price of the bill: "))
      print("If you go to a restaurant with", num1 - 1, "other people and the bill is worth $", num2, ", then each person will pay $", bill_split(num2, num1))
        
    elif basic_choice == 'B':
      num1 = float(input("Enter the price of the bill: "))
      num2 = float(input("Enter the percentage you want to tip: "))
      print("If you go to a restaurant and the bill is worth $", num1, ", and you want to tip,", num2, "%, then the tip will be worth $", bill_tip(num1, num2))

  next_calculation = input("Let's do another calculation? (yes/no): ")
  if next_calculation == 'yes':
    continue
  if next_calculation == 'no':
    print("Goodbye!")
    break