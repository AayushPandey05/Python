#................................
#TODO: Two print the sum of two dight number just buy asking any two digit number from user.....
#!...Ask the user to enter any two digit number..
two_digit_number = input("Type a two digit number: ")

#!.Opening new Variable "first_digit" & "second_digit"and then putting which number to add first digit to second i.e("0"&"1")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#?...putting the first_digit and the second_degit in "INT" because they are of type "int" not "str" 
result = int(first_digit) + int(second_digit)  

#!...Printing the result...
print(result)          
                         
                              