import gameCondition

print("The XXXXX player starts. Type :quit to quit and :replay to restart the game.")

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
    global playerinput

    playerinput = str(input(""))
    
    if player == 0:
        playerPH = "-----"
    elif player == 1:
        playerPH = "XXXXX"
        print("OOOOO It's you're turn")
    elif player == 2:
        playerPH = "OOOOO"
        print("XXXXX It's you're turn") #"its you're turn" is reverses, so XXXXX is placed in OOOOO and OOOOO placed in XXXXX XXX
        
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
    
    if playerinput == ":quit":
        print("\n")
        print("Ending Game...")
        print("\n")
        exit()
    else: 
        print("\n")
        print("Invalid input, try again.")
        print("\n")

    print(top)
    print(A%(ph1, ph2, ph3))
    print(B%(ph4, ph5, ph6))
    print(C%(ph7, ph8, ph9))

    playerPH = 2

def startGame():
    global WonOrTie
    WonOrTie = False
    while WonOrTie == False:
        main(1)
        WonOrTie = gameCondition.check(ph1,ph2,ph3,ph4,ph5,ph6,ph7,ph8,ph9)
        main(2)

startGame()

