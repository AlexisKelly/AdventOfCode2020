import re
#1-3 a: abcde
amountOfValidPasswords = 0
day2Input = open("Day2/day2input.txt", "r")
amountOfValidCharPasswords = 0

# for each row
for line in day2Input:
    day2InputSplit = re.split('-| |\:|  ',line)
    lengthOfSplitList = len(day2InputSplit)
    print("Length of list split"+str(lengthOfSplitList))
    print("first:"+day2InputSplit[0])
    print("2nd:"+day2InputSplit[1])
    print("3rd:"+day2InputSplit[2])
    print("4th:"+day2InputSplit[3])
    print("5th:"+day2InputSplit[4])

    # get min, get max, get letter
    minChars = int(day2InputSplit[0])
    maxChars = int(day2InputSplit[1])
    letterToFind = str(day2InputSplit[2])
    password = day2InputSplit[4]
    # get count of times char appears in string
    instancesOfCharInString = password.count(letterToFind)
    # if char appears between min and max then it's valid so add to count
    if(instancesOfCharInString in range(minChars,maxChars+1)):
        amountOfValidPasswords += 1
        print("valid")

    charAtMin = password[(minChars-1)]
    charAtMax = password[(maxChars-1)]
    if(charAtMin == letterToFind):
        if(charAtMax != letterToFind):
            amountOfValidCharPasswords +=1
            print("valid for chars")

    if(charAtMax == letterToFind):
        if(charAtMin != letterToFind):
            amountOfValidCharPasswords +=1
            print("valid for chars")


day2Input.close
print("Amount of Valid Passwords:"+str(amountOfValidPasswords))
print ("Amount of Valid CHAR Passwords:"+str(amountOfValidCharPasswords))
