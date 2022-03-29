def dogs():
    name = input("please enter dog's name: ")
    age = int(input("please enter dog's age: "))
    print(f'the dog {name} is {age*7} dog years old')


def friends():
    friends = [input(f'friend number {i}: ') for i in range(1,4)]
    other = input("please enter other friend's name: ")
    if other in friends:
        print('in list')
    else:
        print('not in list')


def factorial():
    num = int(input('please enter a number: '))
    result = 1
    while num != 0:
        result = num *result
        num -= 1
    print(result)


con = 'y'


while con == 'y':
    choice = int(input('menu:\n1. Dogs Details\n2. Friends List\n3. Factorial\n'))
    match choice:
        case 1:
            dogs()
        case 2:
            friends()
        case 3:
            factorial()
        case _:
            print('please enter a value between 1-3')
    con = input('\ndo you wish to continue? y/n\n')