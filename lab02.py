try:
#2) Check if number is ODD or even
    my_number =int(input("please input a number:"))
#Divide the number by two and save the remainder
    my_remainder = my_number % 2

    if my_remainder ==1:
        print ("the number is odd")
    else:
        print("the number is even")
except: ValueError

