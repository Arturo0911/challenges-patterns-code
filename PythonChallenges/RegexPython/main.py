#!/usr/bin/python3

import re


TEXT = """The hackerrank team is on a mission to flatten the world by restructuring the DNA of every company on the planet
        We rank programmers based on their coding skills, helping companies source great programmers and reduce the time to 
        hire. As a result, we are revolutionizing the way companies discover and evaluate talented engineers. The hackerrank 
        platform is the destination for the best engineers to hone their skills and companies to find top engineers."""


def main():

    find = re.findall(r'\W*(hackerrank)\W*', TEXT)
    print(f"There are {len(find)} times of the word hackerrank")


if __name__ == "__main__":
    main()
