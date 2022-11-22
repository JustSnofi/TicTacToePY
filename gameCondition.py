def check(ph1,ph2,ph3,ph4,ph5,ph6,ph7,ph8,ph9) -> bool:
    global WonOrTie
    WonOrTie = False


    if ph1 == "*****" and ph4 == "*****" and ph7 == "*****":
        WonOrTie = True
        print("***** Won")
    elif ph1 == "OOOOO" and ph4 == "OOOOO" and ph7 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")
    if ph2 == "*****" and ph5 == "*****" and ph8 == "*****":
        WonOrTie = True
        print("***** Won")
    elif ph2 == "OOOOO" and ph5 == "OOOOO" and ph8 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")

    
    if ph3 == "*****" and ph6 == "*****" and ph9 == "*****":
        WonOrTie = True
        print("***** Won")
    elif ph3 == "OOOOO" and ph6 == "OOOOO" and ph9 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")



    if ph1 == "*****" and ph2 == "*****" and ph3 == "*****":
        WonOrTie = True
        print("***** Won")
    elif ph1 == "OOOOO" and ph2 == "OOOOO" and ph3 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")

    if ph4 == "*****" and ph5 == "*****" and ph6 == "*****":
        WonOrTie = True
        print("***** Won")
    elif ph4 == "OOOOO" and ph5 == "OOOOO" and ph6 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")

    if ph7 == "*****" and ph8 == "*****" and ph9 == "*****":
        WonOrTie = True
        print("***** Won")
    elif ph7 == "OOOOO" and ph8 == "OOOOO" and ph9 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")



    if ph1 == "*****" and ph5 == "*****" and ph9 == "*****":
        WonOrTie = True
        print("***** Won")
    elif ph1 == "OOOOO" and ph5 == "OOOOO" and ph9 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")

    if ph3 == "*****" and ph5 == "*****" and ph7 == "*****":
        WonOrTie = True
        print("***** Won")
    elif ph3 == "OOOOO" and ph5 == "OOOOO" and ph7 == "OOOOO":
        WonOrTie = True
        print("OOOOO Won")


    return WonOrTie