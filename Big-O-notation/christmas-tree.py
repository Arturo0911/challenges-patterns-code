#!/usr/bin/python3



def christmas_tree(limit: int):

    



    for x in range(limit):
        print("\t\t"," "*(limit-1-x),"* "*x, " "*(limit-1-x))

    for x in range(5):
        print("\t\t\t\t     "," #"*7)

    print("""
          ____                                                                                                                                                 
        ,'  , `.                                                       ,---,                                    ___              ____                          
     ,-+-,.' _ |                                                     ,--.' |               ,--,               ,--.'|_          ,'  , `.                        
  ,-+-. ;   , ||           __  ,-.  __  ,-.                          |  |  :      __  ,-.,--.'|               |  | :,'      ,-+-,.' _ |                        
 ,--.'|'   |  ;|         ,' ,'/ /|,' ,'/ /|                          :  :  :    ,' ,'/ /||  |,      .--.--.   :  : ' :   ,-+-. ;   , ||             .--.--.    
|   |  ,', |  ':  ,---.  '  | |' |'  | |' |   .--,            ,---.  :  |  |,--.'  | |' |`--'_     /  /    '.;__,'  /   ,--.'|'   |  || ,--.--.    /  /    '   
|   | /  | |  || /     \ |  |   ,'|  |   ,' /_ ./|           /     \ |  :  '   ||  |   ,',' ,'|   |  :  /`./|  |   |   |   |  ,', |  |,/       \  |  :  /`./   
'   | :  | :  |,/    /  |'  :  /  '  :  /, ' , ' :          /    / ' |  |   /' :'  :  /  '  | |   |  :  ;_  :__,'| :   |   | /  | |--'.--.  .-. | |  :  ;_     
;   . |  ; |--'.    ' / ||  | '   |  | '/___/ \: |         .    ' /  '  :  | | ||  | '   |  | :    \  \    `. '  : |__ |   : |  | ,    \__\/: . .  \  \    `.  
|   : |  | ,   '   ;   /|;  : |   ;  : | .  \  ' |         '   ; :__ |  |  ' | :;  : |   '  : |__   `----.   \|  | '.'||   : |  |/     ," .--.; |   `----.   \ 
|   : '  |/    '   |  / ||  , ;   |  , ;  \  ;   :         '   | '.'||  :  :_:,'|  , ;   |  | '.'| /  /`--'  /;  :    ;|   | |`-'     /  /  ,.  |  /  /`--'  / 
;   | |`-'     |   :    | ---'     ---'    \  \  ;         |   :    :|  | ,'     ---'    ;  :    ;'--'.     / |  ,   / |   ;/        ;  :   .'   \'--'.     /  
|   ;/          \   \  /                    :  \  \         \   \  / `--''               |  ,   /   `--'---'   ---`-'  '---'         |  ,     .-./  `--'---'   
'---'            `----'                      \  ' ;          `----'                       ---`-'                                      `--`---'                 
                                              `--`                                                                                                             
    """)




def main():
    christmas_tree(limit=30)



if __name__ == "__main__":
    main()
