#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 8, 2025
# Program that calculates the sum of 1+2+3...+n,
# where n is a positive integer given by the user.
# The sum will be calculated through the use of a while loop.


def main():
    # Get the user's input as a string
    user_input = input("Enter a positive integer: ")

    try:
        # Convert the user's input to an integer
        user_num = int(user_input)

        # Check if the user's number is positive
        if user_num > 0:
            # Initialize variables for the loop
            sum = 0
            counter = 0
            # Loop while counter is less than user_num
            while counter < user_num:
                # Increment counter by 1
                counter += 1
                # Add counter to sum
                sum += counter
            # Display the sum
            print(f"The sum of numbers from 0 to {user_num} = {sum}.")
        else:
            # Tell the user that the number must be positive
            print(f"Number must be a positive integer!")
    except ValueError:
        # Tell the user that their input wasn't an integer
        print(f"{user_input} is not an integer.")
    finally:
        # Program completion message
        print("Thanks for Playing!")


if __name__ == "__main__":
    main()
