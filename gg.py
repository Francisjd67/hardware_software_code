def decimal_to_binary(number):
    return bin(int(number))[2:]

def main():
    num = input("Enter Decimal Number: ")
    print("Decimal {} to Binary: {}" .format(num, decimal_to_binary(num)))

if __name__ == '__main__':
    main()
