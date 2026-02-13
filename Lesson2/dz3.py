num = float(input("Введите первое число:"))
action = input("Выполните действие +, -, *, / :")
num1 = float(input("Введите второе число:"))

if action == '+':
    print(num + num1)
elif action == '-':
    print(num - num1)
elif action == '*':
    print(num * num1)
elif action == '/':
    if num1 != 0:
        print(num / num1)
    else:
        print("Неверная операция:")






