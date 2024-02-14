def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:                         #keep dividing until at 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result  #place string in reverse order
    return result

def binary_to_decimal(number):
    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1 # determine greatest power
        for num in str(number) :
            result += int(num) * 2 ** power
            power -= 1    # decrease by 1
    return result

def main():
    print("Choose a calculator:")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        number = input("Enter a binary number: ")
        try:
            decimal_result = binary_to_decimal(number)
            message = "The decimal value is {0} and the binary value is {1}.".format(binary_to_decimal(number), number)
            print(message)
        except ValueError:
            print("Invalid input. Please enter a binary number.")
    elif choice == "2":
        try:
            number = int(input("Enter a decimal number: "))
            binary_result = decimal_to_binary(number)
            print("Decimal {} to Binary: {}" .format(number, decimal_to_binary(number)))
        except ValueError:
            print("Invalid input. Please enter a decimal number.")
    else:
        print("Invalid input. Please enter 1 or 2.")
        return main()
if __name__ == "__main__":
    main()
