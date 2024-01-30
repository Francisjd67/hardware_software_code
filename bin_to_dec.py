def binary_to_decimal(number):
    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1 # determine greatest power
        for num in str(number) :
            result += int(num) * 2 ** power
            power -= 1    # decrease by 1
    return result

def main():
    num = input("Enter Binary Number:")
    message = "The decimal value is {0} and the binary value is {1}.".format(binary_to_decimal(num), num)
    print(message)
if __name__ == '__main__':
    main()
