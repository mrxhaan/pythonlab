def addition(num1,num2):
   result=(num1 + num2) 
   return result

def subtraction(num1,num2):
   result=(num1 - num2) 
   return result

def multiplication(num1,num2):
   result=(num1 * num2) 
   return result

def division(num1,num2):
   try:
      result=(num1 / num2) 
      return result
   except ZeroDivisionError:
      print("Second number should be nonzero")
   except:
      print("Unexpected error")
   