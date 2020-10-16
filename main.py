# get two inputs
# run the formula until you get end_num
# output

command = "c"

while command.lower() != "q":
    startNum = int(input("Enter the start number: "))
    endNum = int(input("Enter the end number: "))
    maxSteps = 1
    for i in range(startNum, endNum):
        num = i
        step = 1
        while (num != 1):
            step += 1
            if num % 2 == 0:
                num /= 2
            else:
                num = num * 3 + 1

        if step > maxSteps: maxSteps = step

    print(startNum, endNum, maxSteps, sep=" ")
    command = input("C: To continue Q: to quit: ")
