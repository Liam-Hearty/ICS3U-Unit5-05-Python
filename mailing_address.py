#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: October 2019
# This program finds your mailing address.


def find_mailing_address(street, city, province, postal_code, apt=None):
    # returns mailing_address

    # process
    mailing_address = street

    if apt is not None:
        mailing_address = apt + "-" + mailing_address

    mailing_address = mailing_address + "\n" + city + " " + province + "  " \
                                      + postal_code

    return mailing_address


def main():
    # this function gets info from user.

    try:
        # input
        aptNum = str(input("Do you have an Apt. Number? Enter y or n: "))

        if aptNum == "y":
            aptNum_from_user = str(input("Enter your Apt. Number: "))
        elif aptNum == "n":
            aptNum_from_user = None
        else:
            print("Please enter a valid response.")
            exit()
    except ValueError:
        print("Please enter a valid response.")

    try:
        # input
        street_address_from_user = str(input("Enter your street address: "))
        city_from_user = str(input("Enter what city: "))
        province_from_user = str(input("Enter what province: "))
        postal_code_from_user = str(input("Enter postal code: "))
        print("")

        apt = aptNum_from_user
        street = street_address_from_user
        city = city_from_user
        province = province_from_user
        postal_code = postal_code_from_user

        # call functions
        if apt is not None:
            mailing_address = find_mailing_address(street, city, province,
                                                   postal_code, apt)
        else:
            mailing_address = find_mailing_address(street, city, province,
                                                   postal_code)

        # output
        print(mailing_address)

    except ValueError:
        print("Please enter a valid response.")


if __name__ == "__main__":
    main()
