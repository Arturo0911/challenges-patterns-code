
"""Singleton design pattern
specially used to make the debugging
more understandable"""

from typing import Any




# a simple solution to replace the print
# statements to see the behavior of code


def write_log(filename: str, level: str, msg: str):
    with open(filename) as log_file:
        log_file.write(f"[{level}] {msg}\n")


def critical(msg: str):
    write_log("CRITICAL", msg)



class Logger:
    """A file-based message logger with the following properties

    Attributes:
        file_name: a string representing the full path of th log file to which
        this logger will write its messages"""


    def __init__(self, file_name: str):
        """Return a logger object whote file_name is *file_name"""
        self.file_name = file_name

    def _write_log(self, level: str, msg: str):
        """Writes a message to the file_name for a specific Logger instance"""
        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")

    def critical(self, level: str, msg: str):
        self._write_log("CRITICAL", msg)
    
    def error(self, level: str,  msg: str):
        self._write_log("ERROR", msg)

    def warn(self, level: str, msg: str):
        self._write_log("WARN", msg)

    def info(self, level: str, msg: str):
        self._write_log("INFO", msg)

    def debug(self, level: str, msg: str):
        self._write_log("DEBUG", msg)

