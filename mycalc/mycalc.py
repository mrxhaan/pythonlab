import sys
import calculator

command=sys.argv[1]
firstnum=int(sys.argv[2])
secondnum=int(sys.argv[3])


if command == 'addition':
   result=calculator.addition(firstnum,secondnum)
   print(result)
elif command =='subtraction':
   result=calculator.subtraction(firstnum,secondnum)
   print(result)
else:
   print("invalid operation")