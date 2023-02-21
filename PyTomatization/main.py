#!/usr/bin/python3

from requests import Session
from requests import (
    get,
    post
)
from typing import int


class XSSChecker:
    def __init__(self, url: str=None) -> None:
        self.url = url
        self.session = None
        self.payloads = None
    
    def _init_session(self):
        self.session = Session()
    
    
    def _check_status_code(self, method: str="GET",
                           payload=None) -> int:
        """
        giving the specific url, we can get 
        the status code from the url, to know if
        we forward to the requests or not!
        """
        if method == "POST":
            if payload is not None:
                return post(url=self.url, data=payload).status_code

        return get(url=self.url).status_code


    def _send_malicious_request(self):
        pass



def main():
    pass


if __name__ == "__main__":
    main()