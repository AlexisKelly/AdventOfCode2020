with open("Day1/day1input.txt") as f:
    day1Input = f.readlines()
found = False 
printedPart1 = False
printedPart2 = False

for i in range(len(day1Input)):
    for j in range(len(day1Input)):
        for k in range(len(day1Input)):
            input1 = int(day1Input[i])
            input2 = int(day1Input[j])
            input3 = int(day1Input[k])

            sumValue=0
            sumValue = input1 +input2
            
            part2SumValue = sumValue + input3

            if(sumValue==2020 and printedPart1 == False):
                multipliedValues = input1*input2
                print("Part 1 Sum is "+str(input1)+"+"+str(input2)+"="+str(sumValue))
                print("***********PART 1 ***"+str(multipliedValues)+"*************")
                printedPart1 = True


            if(part2SumValue==2020 and printedPart2 == False):
                part2MultipliedValues = input1*input2*input3
                print("Part 2 Sum is "+str(input1)+"+"+str(input2)+"+"+str(input3)+"="+str(part2SumValue))
                print("***********PART 2 ***"+str(part2MultipliedValues)+"*************")
                printedPart2 = True
