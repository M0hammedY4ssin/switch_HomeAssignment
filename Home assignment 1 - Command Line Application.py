from colorama import Fore, Style, init
def IsPalindrom(str):
    if len(str) <= 1:
        return True
    i,j = 0, len(str)-1

    while i < j:
        if str[i] != str[j]:
            return False
        i+=1
        j-=1
    return True

max_len = 15
while True:
    print(Style.RESET_ALL +"The available operations are: ")
    print("1 - Palindrome: check if the input is palindrome\n"
          "2 - Lower: check if all characters in the input are lowercase\n"
          "3 - Digit: check if all the input are digit\n"
          f"4 - Long: check if the input length is longer than {max_len} \n"
          "5 - Empty: check if th input is empty\n"
          "6 - Exit: Exit successfully from the application\n\n")
    user_input = int(input("Please enter the number of the operation you choose: "))
    if user_input == 1:
        # palindrom
        str = input("Enter an input: ")
        print("The answer is: ", IsPalindrom(str))
    elif user_input == 2:
        #  Is Lowercase
        str = input("Enter an input: ")
        print("The answer is: ", str.islower())
    elif user_input == 3:
        str = input("Enter an input: ")
        print("The answer is: ", str.isdigit())
    elif user_input == 4:
        str = input("Enter an input: ")
        res = len(str) > max_len
        print("The answer is: ", res)
    elif user_input == 5:
         str = input("Enter an input: ")
         res = len(str)==0
         print("The answer is: ", res)
    elif user_input == 6:
        break
    else: print(Fore.RED + "input error, try again!")
print(Fore.GREEN + "Exit successfully!")

