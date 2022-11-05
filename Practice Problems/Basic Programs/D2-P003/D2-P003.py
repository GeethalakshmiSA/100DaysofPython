 # PROBLEM STATEMENT - To find the ASCII value of the given input
  
  # Model 1 : Using In-built function ORD()
  
character = input("Enter the character to find its ASCII value : ")
if len(character) == 1:
    print("The ASCII value of the character", character, "is ", ord(character))
else:
    print("Invalid Input! Please enter only one character and not a sequence of characters")
