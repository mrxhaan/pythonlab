import sys
import calculator

command=sys.argv[1]

try:
   firstnum=int(sys.argv[2])   
   secondnum=int(sys.argv[3])
except ValueError:
   print("please only enter numbers")
   sys.exit(1)
if command == 'addition':
   result=calculator.addition(firstnum,secondnum)
   print(result)
elif command =='subtraction':
   result=calculator.subtraction(firstnum,secondnum)
   print(result)
elif command == 'multiplication':
   result=calculator.multiplication(firstnum,secondnum)
   print(result)
elif command == 'division':
   result=calculator.division(firstnum,secondnum)
   print(result)
else:
  print("invalid operation")