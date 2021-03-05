#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
num1=int(input("Enter the first integar: "))
num2=int(input("Enter the second integar: "))
num4=int(input("Enter the third integar: "))
if num1>num2> and num1>num3 and num2>num3:

    gNum=num1
    nNum=num2
    sNum=num3
elif num1>num2 and num1>num3 and num3>num2:

    gNum=num1
    nNum=num2
    sNum=num3
elif num2>num1 and num2>num3 and num1>num3:

    gNum=num2
    nNum=num1
    sNum=num3
elif num2>num1 and num2>num3 and num3>num1:

    gNum=num2
    nNum=num3
    sNum=num1
elif num3>num1 and num3>num2 and num1>num2:

    
    gNum=num3
    nNum=num1
    sNum=num2
elif num3>num1 and num3>num2 and num2>num1:
    gNum=num3
    nNum=num2
    sNum=num1

if (nNum-num**2 + sNum**2)==(gNum**2):
    print(str(sNum)+ ","+ str(nNum)+ ","+ str(gNum)+ :"make the pythogorean triple" )

else:
     print(str(sNum)+ ","+ str(nNum)+ ","+ str(gNum)+ :"Do not make it" )