#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

VIPNames = ("Sam","Jordan","Chris","Jen","Doug","John","Owen")
name=input("Please enter your name")
if (name in VIPNames)==True:
    print("Hi " +str(name) +" You are VIP!")
else:
    print("You are not VIP.")