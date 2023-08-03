firstNumber = int(input("Enter the first number: "))
calculationMethod = input("Enter the calculation method: ")
secondNumber = int(input("Enter the second number: "))
if(calculationMethod == "+"):
  print ("The answer is:" ,firstNumber+secondNumber)
if(calculationMethod == "-"):
  print ("The answer is:" ,firstNumber-secondNumber)
if(calculationMethod == "*"):
  print ("The answer is:" ,firstNumber*secondNumber)
if(calculationMethod == "/"):
  print ("The answer is:" ,firstNumber/secondNumber)