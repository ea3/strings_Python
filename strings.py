my_string = "Hello World"

my_string1 = my_string[0] 

print(my_string1)

my_string1 = 'abcdefghijk'
print(my_string1)
print (my_string1[2:])
print(my_string1[:3])

print(my_string1[3:6])
print(my_string1[3:9]) 
print(my_string1[::])     # prints the string from start to finish.
print(my_string1[::2])   # jump in step size # 2.
print(my_string1[2:7:2])   # prints index 2, up to but not including index 7, in steps of 2. 
print(my_string1[::-1])  # reverses the string. 


#immutability of strings. 

name = 'Sam'

# name [0] = 'P'   Won't work

last_letters = name [1:]

print(last_letters)

print('P' + last_letters)  # String concatenation. 

x = 'Hello World'
print(x + " it is beautiful outside")



 