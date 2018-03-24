x = 1
sum = 0
for x in range(1,1000000):
    string = str(x)
    myList = []
    for digit in string:
        if digit is not '0':
            myList.append(int(digit))
    result = 1
    for element in myList:
        result *= element
    sum += result
#     print(result)
print(sum)