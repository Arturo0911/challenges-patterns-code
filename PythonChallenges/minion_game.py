#!/usr/bin/python3



def minion_game(string):

    key_word = "BANA"
    counter = 0
    for x in range(len(string)+1):
        for y in range(len(string)+1):
            if string[x:y] == key_word:
                counter += 1

    print(counter)

if __name__ == "__main__":
    s = raw_input()

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print "Kevin", kevsc
    elif kevsc < stusc:
        print "Stuart", stusc
    else:
        print "Draw"
