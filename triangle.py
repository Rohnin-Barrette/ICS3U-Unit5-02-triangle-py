#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# this program calculates fahrenheit


def calculate_area(base, height):
    # calculate area

    # process
    area = (base * height) / 2

    # output
    print("The area of the triangle is {} cm²".format(area))


def main():
    # this function gets base and height

    # input
    try:
        base_from_user_string = input("Enter the base length of a triangle (cm): ")
        height_from_user_string = input("Enter the height of a triangle (cm): ")
        print("")
        base_from_user = float(base_from_user_string)
        height_from_user = float(height_from_user_string)

        # call functions
        calculate_area(base_from_user, height_from_user)

    except Exception:
        print("Invalid input.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
