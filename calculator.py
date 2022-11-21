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
  
print("Select operation.")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")
print("5: Exponent")
print("6: Square Root")
print("7: Cube Root")

while True:
  choice = input("Enter choice(1/2/3/4/5/6/7): ")

  #Part for two-number calculations
  if choice in ('1', '2', '3', '4', '5'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
  
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

  #Part for one-number calculations
  elif choice in ('6', '7'):
    num3 = float(input("Enter number: "))

    if choice == '6':
      print("The square root of", num3, "is", square_root(num3))

    elif choice == '7':
      print("The cube root of", num3, "is", cube_root(num3))
    
  next_calculation = input("Let's do another calculation? (yes/no): ")
  if next_calculation == 'yes':
    continue
  if next_calculation == 'no':
    print("Goodbye!")
    break
      
else:
  print("Invalid Input")