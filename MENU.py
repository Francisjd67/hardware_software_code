def get_menu() : # used to display a menu
    menu_dict = {
        '1' : 'apples',
        '2' : 'bananas',
        '3' : 'cherries',
        '4' : 'pears',
        'x' : 'done_ordering'
    }
    return menu_dict


    def display_menu(menu_dict):
        for items, values in menu_dict.items() :
            print(items+"."+ values.replace('_','').capitalize())
        menu_selection = iput("What would you like to buy?").upper()

        print("You selected {}".format(menu_dict[menu_selection]))

        return menu_selection

    def display_purchases(item_list) :
        del items_list[-1]
        print("You purchases {} items".format(len(items_list)), end="")
        print(*items_list, sep=",", end=".\n")

def main():
    menu_selection = ''
    item_list = []
    while menu_selection != 'x':
        menu_dict = get_menu()
        menu_selection = display_menu(menu_dict)
        items_list.append(menu_dict[menu_selection])
        input("Hit enter to continue!!")

    display_purchases(items_list)

if __name__ == '__main__':
    main()
