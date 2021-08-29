#!usr/bin/python3


LIST = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def pattern(size):
    pattern = int(size) * 1 + (size - 2)
    return pattern, size


def generate(position, upto):
    counter = 0
    while upto > 0:
        
        if counter >= 1:
            
            for x in range(position-1, position+1): print(LIST[x]+"-", end="")

        else:
    
            print(LIST[position-1])
        
        counter += 1
        upto -= 1
        position -= 1





def print_rangoli(size):

    import string
    alpha = string.ascii_lowercase

    l = []

    for x in range(size):
        s = '-'.join(alpha[x:size])
        l.append((s[::-1]+s[1:]).center(size* 4 - 3,"-"))

    print('\n'.join(l[:0:-1]+l))
    



    #print(char)



if __name__ == '__main__':
    # n = int(input())
    print_rangoli(10)
    #generate(5,5)
