def menu():
    con = 'y'
    while con == 'y':
        choice = input('menu:\na. IP System\nb. DNS System\n')
        match choice:
            case 'a':
                menuA()
            case 'b':
                menuB()
            case _:
                print('please choose a or b!!')
                continue
        con = input('\ndo you wish to continue? y/n\n')


def searchIP():
    pass


def addIP():
    pass


def deleteIP():
    pass


def printIP():
    pass


def menuA():
    choice = int(input('menu:\n1. search ip\n2. add ip\n3. delete ip\n4. print ip\n'))
    match choice:
        case 1:
            searchIP()
        case 2:
            addIP()
        case 3:
            deleteIP()
        case 4:
            printIP()
        case _:
            print('please enter a value between 1-4')
            menuA()


def searchURL():
    pass


def addURL():
    pass


def deleteURL():
    pass


def updateURL():
    pass


def printURL():
    pass


def menuB():
    choice = int(input('menu:\n1. search url\n2. add url\n3. delete url\n4. update url dict\n5. print url dict\n'))
    match choice:
        case 1:
            searchURL()
        case 2:
            addURL()
        case 3:
            deleteURL()
        case 4:
            updateURL()
        case 5:
            printURL()
        case _:
            print('please enter a value between 1-5')
            menuA()
