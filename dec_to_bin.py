def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:                         #keep dividing until at 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result  #place string in reverse order
    return result
def getInput():
    num = input("Enter a decimal number")
    while not num.isnumeric():
        print("Not a decimal number")
        num = input("enter again")

    print("Decimal {} to Binary: {}" .format(num, decimal_to_binary(num)))
        

if __name__ == '__main__':
    getInput()
