def check(ph1,ph2,ph3,ph4,ph5,ph6,ph7,ph8,ph9) -> bool:
    global WonOrTie
    WonOrTie = False


    if ph1 == "XXXXX" and ph4 == "XXXXX" and ph7 == "XXXXX":
        WonOrTie = True
        print("XXXXX Won")
    elif ph1 == "OOOOO" and ph4 == "OOOOO" and ph7 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")
    if ph2 == "XXXXX" and ph5 == "XXXXX" and ph8 == "XXXXX":
        WonOrTie = True
        print("XXXXX Won")
    elif ph2 == "OOOOO" and ph5 == "OOOOO" and ph8 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")

    
    if ph3 == "XXXXX" and ph6 == "XXXXX" and ph9 == "XXXXX":
        WonOrTie = True
        print("XXXXX Won")
    elif ph3 == "OOOOO" and ph6 == "OOOOO" and ph9 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")



    if ph1 == "XXXXX" and ph2 == "XXXXX" and ph3 == "XXXXX":
        WonOrTie = True
        print("XXXXX Won")
    elif ph1 == "OOOOO" and ph2 == "OOOOO" and ph3 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")

    if ph4 == "XXXXX" and ph5 == "XXXXX" and ph6 == "XXXXX":
        WonOrTie = True
        print("XXXXX Won")
    elif ph4 == "OOOOO" and ph5 == "OOOOO" and ph6 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")

    if ph7 == "XXXXX" and ph8 == "XXXXX" and ph9 == "XXXXX":
        WonOrTie = True
        print("XXXXX Won")
    elif ph7 == "OOOOO" and ph8 == "OOOOO" and ph9 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")



    if ph1 == "XXXXX" and ph5 == "XXXXX" and ph9 == "XXXXX":
        WonOrTie = True
        print("XXXXX Won")
    elif ph1 == "OOOOO" and ph5 == "OOOOO" and ph9 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")

    if ph3 == "XXXXX" and ph5 == "XXXXX" and ph7 == "XXXXX":
        WonOrTie = True
        print("XXXXX Won")
    elif ph3 == "OOOOO" and ph5 == "OOOOO" and ph7 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")

    
    return WonOrTie