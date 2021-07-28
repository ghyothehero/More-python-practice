July 12, 2021
#Passoword/STRING CHECKER

#Return True if the the string has a length
#of 10 or greater
def checksLength(userString):
    if(len(userString)>=10):
        return True
    else:
        return False

#Return True if the string has no spaces
def noSpaces(userString):
    countSpaces=0
    for i in range(0, len(userString)):
        if(userString[i]==" "):
            countSpaces+=1
    if(countSpaces>0):
        return False
    return True

#Returns True if the string has at least 2
#uppercase letters
def twoUC(userString):
    countUpper=0
    for i in range(0, len(userString)):
        if(userString[i].isupper()):
            countUpper+=1
    if(countUpper>=2):
        return True
    else:
        return False
            
#Returns True if the string has at least 3
#lowercase letters
def threeLC(userString):
    countLower=0
    for i in range(0, len(userString)):
        if(userString[i].islower()):
            countLower+=1
    if(countLower>=3):
        return True
    else:
        return False

#Returns true if ing (sequential)is present at least once in the string
def hasING(userString):
    countING=0
    for i in range(0, len(userString)-2):
        if(userString[i].lower()=="i" and userString[i+1].lower()=='n' and userString[i+2].lower()=='g'):
            countING+=1
    if(countING>0):
        return True
    else:
        return False
        

#Returns True if the string has both a % and a #
def hasPercentHash(userString):
    countPercent=0
    countHash=0
    for i in range(0, len(userString)):
        if(userString[i]=="%"):
            countPercent+=1
        elif(userString[i]=="#"):
            countHash+=1
    if(countHash>0 and countPercent>0):
        return True
    else:
        return False

#Returns True if the string has at least 1 number
def hasNum(userString):
    countNum=0
    for i in range(0, len(userString)):
        if(userString[i].isdigit()):
            countNum+=1
    if(countNum >= 1):
        return True
    else:
        return False

#Main function allows user to enter strings until quit
#Returns valid or invalid to user
#Also keep track of valid and invalid string and print these for the user when they quit
def main():
    print("Welcome to the string checker! Your string must have at least 10 characters, 2 UC letter, 3 LC letters, and at least 1 number. It must contain both a % and a #. It cannot contain spaces.")
    print()
    validInputsString=""
    invalidInputsString=""
    valid = []
    invalid = []

    #set
    userContinue=input("Would you like to enter a string (y/n)? ")
    #check
    while(userContinue.lower() == "y"):
        uI=input("Enter a string: ")
        testLength = checksLength(uI)
        testSpaces = noSpaces(uI)
        testUpper = twoUC(uI)
        testLower = threeLC(uI)
        testPercentHash = hasPercentHash(uI)
        testNum = hasNum(uI)

        if(testLength and testSpaces and testUpper and testLower and testPercentHash and testNum):
            print("Valid String")
            validInputsString = validInputsString + uI + " "
            valid.append(uI)
        else:
            print("String not valid")
            invalidInputsString = invalidInputsString + uI + " "
            invalid.append(uI)

        #update
        userContinue=input("Would you like to enter another string (y/n)? ")
        
    #Print valid and invalid strings entered
    print("You entered the following valid strings: " + validInputsString)
    print("You entered the following invalid strings: " + invalidInputsString)

    print("You entered the following valid strings: ")
    for i in range(0, len(valid)):
        print(valid[i])
    print("You entered the following invalid strings: ")
    for j in range(0, len(invalid)):
        print(invalid[j])
    
    print("Have a nice day!")
main()

