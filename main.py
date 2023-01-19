nb1 = "1"
nb2 = "2"
nb3 = "3"
nb4 = "4"
nb5 = "5"
nb6 = "6"
nb7 = "7"
nb8 = "8"
nb9 = "9"
jeux = 0
placement = ""
gagnant = ""
X = "\033[1;34mX\033[0;00m"
O = "\033[1;31mO\033[0;00m"


def print_case():
    print("")
    print(nb1, "|", nb2, "|", nb3)
    print("-- --- --")
    print(nb4, "|", nb5, "|", nb6)
    print("-- --- --")
    print(nb7, "|", nb8, "|", nb9)
    print("")


def res_gagnant():
    print(gagnant + "YOU WIN !!!")
    print("")


def res_nul():
    print("\033[1;33mEQUALITY\033[0;0m")
    print("")


print_case()

while gagnant == "":

    if jeux % 2 == 0:
        placement = input("\033[1;34m Player X \033[0;0m Choose a place: ")
        if placement == "1" and nb1 == "1":
            nb1 = X
            jeux += 1
        
        elif placement == "2" and nb2 == "2":
            nb2 = X
            jeux += 1
        
        elif placement == "3" and nb3 == "3":
            nb3 = X
            jeux += 1
        
        elif placement == "4" and nb4 == "4":
            nb4 = X
            jeux += 1
        
        elif placement == "5" and nb5 == "5":
            nb5 = X
            jeux += 1
        
        elif placement == "6" and nb6 == "6":
            nb6 = X
            jeux += 1
        
        elif placement == "7" and nb7 == "7":
            nb7 = X
            jeux += 1
        
        elif placement == "8" and nb8 == "8":
            nb8 = X
            jeux += 1
        
        elif placement == "9" and nb9 == "9":
            nb9 = X
            jeux += 1
        
        else:
            print("\033[1;32m Choose a other case \033[0;0m")
        print_case()

    if nb1 == X and nb2 == X and nb3 == X or nb4 == X and nb5 == X and nb6 == X or nb7 == X and nb8 == X and nb9 == X or nb1 == X and nb4 == X and nb7 == X or nb3 == X and nb6 == X and nb9 == X or nb1 == X and nb5 == X and nb9 == X or nb3 == X and nb5 == X and nb7 == X:
        gagnant = X

    else:
        (nb1 != "1" and nb2 != "2" and nb3 != "3" and nb4 != "4" and nb5 != "5" and nb6 !=
         "6" and nb7 != "7" and nb8 != "8" and nb9 != "9") and gagnant == ""

    if jeux % 1 == 0:
        placement = input("\033[1;31m Player O \033[0;00m Choose a place: ")
        if placement == "1" and nb1 == "1":
            nb1 = O
            jeux += 1
        
        elif placement == "2" and nb2 == "2":
            nb2 = O
            jeux += 1
        
        elif placement == "3" and nb3 == "3":
            nb3 = O
            jeux += 1
        
        elif placement == "4" and nb4 == "4":
            nb4 = O
            jeux += 1
        
        elif placement == "5" and nb5 == "5":
            nb5 = O
            jeux += 1
        
        elif placement == "6" and nb6 == "6":
            nb6 = O
            jeux += 1
        
        elif placement == "7" and nb7 == "7":
            nb7 = O
            jeux += 1
        
        elif placement == "8" and nb8 == "8":
            nb8 = O
            jeux += 1
        
        elif placement == "9" and nb9 == "9":
            nb9 = O
            jeux += 1
        
        else:
            print("\033[1;32m Choose a other case \033[0;0m")
        print_case()

    if nb1 == O and nb2 == O and nb3 == O or nb4 == O and nb5 == O and nb6 == O or nb7 == O and nb8 == O and nb9 == O or nb1 == O and nb4 == O and nb7 == O or nb3 == O and nb6 == O and nb9 == O or nb1 == O and nb5 == O and nb9 == O or nb3 == O and nb5 == O and nb7 == O:
        gagnant = O

    else:
        (nb1 != "1" and nb2 != "2" and nb3 != "3" and nb4 != "4" and nb5 != "5" and nb6 !=
         "6" and nb7 != "7" and nb8 != "8" and nb9 != "9") and gagnant == ""


if gagnant == "":
    res_nul()
else:
    res_gagnant()
