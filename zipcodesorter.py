import random
from banner import banner
banner("Zip Code Sorter", "Ciera")

name = input("what is your name? ")
print("")

while True:
    zip_number = int(input("What is your zip code?"))

    if zip_number == 49412:
        print("The zip code 49412 is for Fremont")
    elif zip_number == 49349:
        print("The zip code for 49349 is for White Cloud")
    elif zip_number == 49309:
        print("The zip code for 49309 is for Bitely")
    elif zip_number == 49312:
        print("The zip code 49312 is for Brohman")
    elif zip_number == 49337:
        print("The zip code 49337 is for Croton and Newaygo")
    elif zip_number == 49413:
        print("The zip code 49413 is for Fremont")
    elif zip_number == 49327:
        print("The zip code 49327 is for Grant")
    else:
        print(f"The zip code for {zip_number} is not in Newaygo County {name}")

    go_again = input("Would you like to enter another zip code (Y/N)?")
    if go_again.lower()[0] == "n":
        break
print(f"Thank you for using the Newaygo County zip code sorter. Goodbye {name}!")