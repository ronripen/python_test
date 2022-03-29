def dogs():
    name = input("please enter dog's name: ")
    age = int(input("please enter dog's age: "))
    print(f'the dog {name} is {age*7} dog years old')


def friends():
    friend = [input(f'friend number {i}: ') for i in range(1, 4)]
    other = input("please enter other friend's name: ")
    if other in friend:
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