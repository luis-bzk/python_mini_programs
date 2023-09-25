def addition(a: int, b: int):
    answer = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(answer))


def subtraction(a: int, b: int):
    answer = a - b
    print(str(a) + ' - ' + str(b) + ' = ' + str(answer))


def multiplication(a: int, b: int):
    answer = a * b
    print(str(a) + ' x ' + str(b) + ' = ' + str(answer))


def division(a: int, b: int):
    answer = a / b
    print(str(a) + ' / ' + str(b) + ' = ' + str(answer))


menu = '''
a. Addition
b. Subtraction
c. Multiplication
d. Division
e. Exit
'''


def input_control():
    a: int = int(input('Enter the first value: '))
    b: int = int(input('Enter the second value: '))
    return a, b


while True:
    print(menu)

    choice = input('Input your choice: ').lower()

    if choice == 'a':
        print('Addition')
        [a, b] = input_control()
        addition(a, b)
    elif choice == 'b':
        print('Subtraction')
        [a, b] = input_control()
        subtraction(a, b)
    elif choice == 'c':
        print('Multiplication')
        [a, b] = input_control()
        multiplication(a, b)
    elif choice == 'd':
        print('Division')
        [a, b] = input_control()
        division(a, b)
    elif choice == 'e':
        print('End')
        quit()
