#pylint:disable=W0621
#pylint:disable=W0301
#pylint:disable=W0311


# Python program to check if a year is leap year or not.
def CheckLeap(Year): 
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  else:  
    print ("Given Year is not a leap Year")    
Year = int(input("Enter the Year: "))  
CheckLeap(Year)