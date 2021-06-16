#!/usr/bin/python3

import random
from pprint import pprint


# credential prediction in Ecuador, using the algorithm of the 10 digits

class CredentialPrediction:

    def __init__(self):
        pass

    @staticmethod
    def generate_random_credentials(self):

        iterations = 9
        credential = "0"
        for i in range(0, iterations):
            credential += str(random.randint(0, 9))
        return credential

    def check_credential_valid(self, credential):

        try:
            # variables
            list_credential = list(credential)
            size = len(list_credential)
            third_digit = int(list_credential[2])
            verifier_digit = int(list_credential[9])
            final_sum = 0  # the conten sum will be contained the sum of the numbers
            check_digit = 0

            if size == 10 and third_digit < 6:

                for i in range(0, 9):

                    if i % 2 == 0:

                        if int(list_credential[i]) * 2 >= 10:

                            final_sum += (int(list_credential[i]) * 2) - 9
                        else:
                            final_sum += (int(list_credential[i]) * 2)
                    else:

                        final_sum += int(list_credential[i])

                check_digit = int(list(str(final_sum))[len(str(final_sum)) - 1])

                return 10 - check_digit == verifier_digit

            else:
                return False
        except Exception as e:
            print(str(e))
            return False

    def valid_credentials(self):

        list_valid_credentials = list()
        x = 2000
        while x > 0:

            credential = self.generate_random_credentials()

            if self.check_credential_valid(credential) and (credential not in list_valid_credentials):
                x -= 1
                list_valid_credentials.append(credential)

            else:
                continue

        return list_valid_credentials


credentials = CredentialPrediction()

pprint(credentials.valid_credentials())

# credential = "0918237421"
# print(check_credential_valid(credential))
# print(generate_random_credentials())
