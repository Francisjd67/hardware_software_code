def check_selelction(inputs): # verify if its a valid input
    hex_list = ["Binary to decimal", "Decimal to binary"]
    for input in inputs :
        if input.upper() not in hex_list: #check if the input is not on the hex hex_list
            print("Not a valid option")
            return(False)
    return(True)
def decimal_to_binary(number):
    if selection == "Binary to decimal":
        result = ""
        number = int(number)
        while number > 0:                         #keep dividing until at 0
            remainder = number % 2
            number = number // 2
            result = str(remainder) + result  #place string in reverse order
    else:
        def binary_to_decimal(number):
            result = 0
            if len(number) > 0:
                power = len(str(number)) - 1 # determine greatest power
                for num in str(number) :
                    result += int(num) * 2 ** power
                    power -= 1    # decrease by 1
        return result


def main():
    good_selection = False
    while not good_selection:
        selection = input("Do you want a Binary to decimal, or Decimal to binary calculator:")
        good_selection = check_selelction(selection)
    print("You chose", selection, input("Please input a number"))
