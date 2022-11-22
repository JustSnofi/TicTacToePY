import gameCondition

player = 1 #this means starting player is "*"
input_number = 0
ph1 = "-----"
ph2 = "-----"
ph3 = "-----"
ph4 = "-----"
ph5 = "-----"
ph6 = "-----"
ph7 = "-----"
ph8 = "-----"
ph9 = "-----"
WonOrTie = False

top = ("      1        2        3")
A = ("A : %s    %s    %s")
B = ("B : %s    %s    %s")
C = ("C : %s    %s    %s")

print(top)
print(A%(ph1, ph2, ph3))
print(B%(ph4, ph5, ph6))
print(C%(ph7, ph8, ph9))

def main(player):
    global ph1,ph2,ph3,ph4,ph5,ph6,ph7,ph8,ph9
    playerinput = str(input(""))
    if player == 0:
        playerPH = "-----"
    elif player == 1:
        playerPH = "*****"
        print("***** It's you're turn")
    elif player == 2:
        playerPH = "OOOOO"
        print("OOOOO It's you're turn")
        
    if playerinput[0] == "A":
        if playerinput [1] == "1":
            ph1 = "{0}".format(playerPH)
        if playerinput [1] == "2":
            ph2 = "{0}".format(playerPH)
        if playerinput [1] == "3":
            ph3 = "{0}".format(playerPH)
    if playerinput[0] == "B":
        if playerinput [1] == "1":
            ph4 = "{0}".format(playerPH)
        if playerinput [1] == "2":
            ph5 = "{0}".format(playerPH)
        if playerinput [1] == "3":
            ph6 = "{0}".format(playerPH)
    if playerinput[0] == "C":
        if playerinput [1] == "1":
            ph7 = "{0}".format(playerPH)
        if playerinput [1] == "2":
            ph8 = "{0}".format(playerPH)
        if playerinput [1] == "3":
            ph9 = "{0}".format(playerPH)

    print(top)
    print(A%(ph1, ph2, ph3))
    print(B%(ph4, ph5, ph6))
    print(C%(ph7, ph8, ph9))

    playerPH = 2

while WonOrTie == False:
    main(1)
    WonOrTie = gameCondition.check(ph1,ph2,ph3,ph4,ph5,ph6,ph7,ph8,ph9)
    main(2)