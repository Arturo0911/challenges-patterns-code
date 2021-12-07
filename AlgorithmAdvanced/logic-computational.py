#!/usr/bin/python3


if __name__ == "__main__":
    limit = 10
    for x in range(limit, 1, -2):
        print(" "*(limit-x+1), "* "*x, " "*(limit-x+1))
    print(" "*(limit), "*")

