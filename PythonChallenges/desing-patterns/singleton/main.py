#!/usr/bin/python


import logger


def main():

    for i in range(4):
        logger.log_message(f"log message {i}")


if __name__ == "__main__":
    main()
