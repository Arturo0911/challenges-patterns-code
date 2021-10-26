
"""Singleton design pattern
specially used to make the debugging
more understandable"""


# a simple solution to replace the print
# statements to see the behavior of code

def criticla(msg: str):
    with open("filename.log", "a") as log_file:
        log_file.write(f"[CRITICAL] {msg}\n")


def error(msg: str):
    with open("filename.log", "a") as log_file:
        log_file.write(f"[ERROR] {msg}\n")


def warn(msg: str):
    with open("filename.log", "a") as log_file:
        log_file.write(f"[WARN] {msg}\n")


def info(msg: str):
    with open("filename.log", "a") as log_file:
        log_file.write(f"[INFO] {msg}\n")


def debug(msg: str):
    with open("filename.log", "a") as log_file:
        log_file.write(f"[DEBUG] {msg}\n")




def log_message(msg: str) -> None:
    with open("filename.log", "a") as log_file:
        log_file.write(f"{msg}\n")


