#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: Apr 14, 2025
# This program calculate and display the “square” (power of 2) starting from 0 until this number.


def main():
    # The main function displays squares of numbers using a for loop.
    try:
        # Ask the user to enter a whole number and store it as 'user_input'
        user_input = int(input("Enter a whole number: "))

        # Check if the user entered a negative number
        if user_input < 0:
            print("Please enter a non-negative whole number.")
        else:
            # process & output
            # The for loop iterates from 0 to user_input (inclusive)
            counter = 0
            # Display the number and its square
            for counter in range(
                user_input + 1
            ):  # range from 0 to user_input (inclusive)
                print(counter, " ^ 2 = " + str(counter**2))

    except Exception:
        # If the input is not a valid number, show an error message.
        print("Invalid input. Please enter a whole number.")

    # Thank the user after the program runs
    print("Thank you for using!")


if __name__ == "__main__":
    main()
