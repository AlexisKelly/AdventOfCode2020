with open("Day1/day1input.txt") as f:
    day1Input = f.readlines()
found = False 

for i in range(len(day1Input)):
    for j in range(len(day1Input)):

        input1 = int(day1Input[i])
        input2 = int(day1Input[j])

        sumValue=0
        sumValue = input1 +input2
       # print("Sum is "+str(input1)+"+"+str(input2)+"="+str(sumValue))
        
        if(sumValue==2020):
            multipliedValues = input1*input2
            print("Sum is "+day1Input[i]+"+"+day1Input[j]+"="+str(sumValue))
            print("***********"+str(multipliedValues)+"*************")
            found=True
            break
    if found == True:
        break