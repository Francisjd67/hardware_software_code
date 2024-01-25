def get_smallest(smallest, value):
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    return smallest

def main():
    smallest = None
    while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            num = float(num)
            smallest = get_smallest(smallest, num)
            print(f"Smallest number is: {smallest}")
        except ValueError:
            print("Invalid input.")

if __name__ == '__main__':
    main()
