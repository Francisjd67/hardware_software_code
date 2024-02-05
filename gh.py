
def menu_display():

    menu_dict = {
        '1'=="decimal_to_binary."
        '2'=="binary to decimal."
        '3'=="Exit"
    }
    while True:
        options=menu.keys()
        options.sort()
        for entry in options:
            print('entry, menu_dict[entry]')

        selection=raw_input("Please Select:")
        if selection =='1':
          print( 'Decimal to binary')
        elif selection == '2':
          print( 'Binary to decimal')
        elif selection == '3':
          break
        else:
          print ("Unknown entry!")
    return menu_dict

def main():
    sel, choice = menu_display()


if __name__ == '__main__':
    main()
