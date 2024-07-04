import sys

command=sys.argv[1]
firstnum=int(sys.argv[2])
secondnum=int(sys.argv[3])



def addition(num1,num2):
   result=(num1 + num2) 
   return result

if command == 'addition':
   result=addition(firstnum,secondnum)
   print(result)
