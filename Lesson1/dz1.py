# number = int(input("Введите четырехзначное число:"))
#
# left = number // 1000
# left1 = number % 1000
# left2 = left1 // 100
# left3 = left1 % 100
# left4 = left3 // 10
# left5 = left3 % 10
#
# print(left)
# print(left2)
# print(left4)
# print(left5)

# Решение №2 с испоьзованием функции divmod

number = int(input("Введите четырехзначное число:"))

num = 1000
num1 = 100
num2 = 10

left, right = divmod(number, num)
left1, right1 = divmod(right, num1)
left2, right2 = divmod(right1, num2)

print(left)
print(left1)
print(left2)
print(right2)