###################################################
#                                                 #
#  @autor: Payload                                #
#                                                 #
#                                                 #
#                                                 #
#                                                 #
###################################################

import getopt
import sys



class Initializr:

    def __init__(self):

        self.list_arguments = []
        self._presentation()
    
    def _presentation(self):


        print("################################################################")
        print("#                                                              #")
        print("#                WELCOME TO ECUATORIAN TRACKER                 #")
        print("#                @Payload                                      #")
        print("#                                                              #")
        print("################################################################")
        
    
    def print_on_screen(self):

        try:
            opts, args = getopt.getopt(sys.argv[2:], "ho:v", ["help", "output"])
        except getopt.GetoptError as err:
            print(str(err))
            sys.exit(2)
    
        output = None
        verbose = False

        for o, a in opts:

            print(" %s and  %s"%(o,a))




init = Initializr()

init.print_on_screen()



