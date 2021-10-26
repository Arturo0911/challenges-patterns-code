
"""Singleton design pattern
specially used to make the debugging
more understandable"""


# a simple solution to replace the print
# statements
def log_message(message: str) -> None:
    with open("filename.log", "a") as log_file:
        log_file.write(f"{message}\n")


