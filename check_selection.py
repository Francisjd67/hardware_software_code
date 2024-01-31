def check_selelction(numbers): # verify if it is a hexadecomal
    hex_list = ["A","B","C","D","E","F","O","1","2","3","4","5","6","7","8","9"]
    for number in numbers :
        if number.upper() not in hex_list: #check if the number is not on the hex hex_list
            print("Not a hexadecimal number")
            return(False)
    return(True)
def main():
    good_selection = False
    while not good_selection:
        selection = input("Provide a hexadecimal number:")
        good_selection = check_selelction(selection)
    print("Good job", selection, "is a hexadecimal number!!!")

if __name__ == '__main__':
    main()
