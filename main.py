from art import logo
#sum
def sum(n1,n2):
  return n1+n2
# subtract
def subtract(n1, n2):
  return n1-n2
# Multiply
def multiply(n1, n2):
  return n1*n2
# Divide
def divide(n1, n2):
  return n1/n2
operations={
  "+":sum,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calculator():
  print(logo)
  num1=float(input("Enter the first number: "))
  for symbols in operations:
      print(f"{symbols}")
  answer=""
  is_end=False
  while not is_end:
    operation_symbol=input(f"Which operations you want to perform from above: ") 
    num2=float(input("Enter the next number: "))
    calculation=operations[operation_symbol]
    answer=calculation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    is_continue=input(f"Do you want to continue to calculate with {answer}? type 'yes' for continue or 'no' to start again? ")
    if is_continue=="yes":
      num1=answer
      
    else:
      is_end=True
      calculator()
calculator()