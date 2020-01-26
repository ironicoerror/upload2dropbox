#!/usr/bin/python3
"""
Programm converts plain text files to binary
to upload them on dropbox
"""

# initializing string  
test_str = "Hello World"
  
# printing original string  
print("The original string is : " + str(test_str)) 
  
# using join() + ord() + format() 
# Converting String to binary 
res = ''.join(format(ord(i), 'b') for i in test_str) 
  
# printing result  
print("The string after binary conversion : " + str(res)) 
