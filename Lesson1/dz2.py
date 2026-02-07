number = int(input("Введите пятизначное число:"))

num = 10000
num1 = 1000
num2 = 100
num3 = 10

left, right = divmod(number, num)
left1, right1 = divmod(right, num1)
left2, right2 = divmod(right1, num2)
left3, right3 = divmod(right2, num3)

left, left1, left2, left3, right3 = right3, left3, left2, left1, left

print(left, left1, left2, left3, right3)



