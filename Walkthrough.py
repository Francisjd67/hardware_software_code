def conversation() :
    print("Do you like coding in Python? Answer yes or no")
    answer = input()
    if answer.lower() == "yes" :
        print("That's good - the United States needs more coders!!")
    elif answer.lower() == "no" :
        print("Thats a shame.")
    else :
        print("I do not understand?")
    print("Goodbye.")
def main() :
    print("Welcome to my conversation progress")
    conversation()
    print("Thanks for chatting with me")
if __name__ == '__main__':
    main()
