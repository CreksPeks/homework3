# Урок #5. Логические условные операторы


# Задание #1


word = int(input("введи целое число: "))
if word > 0 and word % 2 == 0:
    print("Положительное четное число.")
elif word > 0 and word % 2 == 1:
    print("Положительное нечетное число")
elif word == 0:
    print("Нулевое число")
elif word < 0 and word % 2 == 1 :
    print("Отрицательное нечетное число")
elif word < 0 and word % 2 == 0:
    print("Отрицательное четное число")
else:
    print("попробуй ввести число! еще раз )))")


# Задание №2


word = input("Напиши слово латинскими буквами: ")
vowels = "aeiouAEIOU"
vow = 0
consonans = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
con = 0
aaa = 0
eee = 0
iii = 0
ooo = 0
uuu = 0
yyy = 0
for i in word:
    if i in vowels:
        vow += 1
        if i == "a":
            aaa += 1
        elif i == "e":
            eee += 1
        elif i == "i":
            iii += 1
        elif i == "o":
            ooo += 1
        elif i == "u":
            uuu += 1

    elif i in consonans:
        con += 1
    elif i == "y":
        yyy += 1
    else:
        print("False")
        break
print("гласных: ", vow)
print("согласных: ", con)
print(" a:", aaa, " e:", eee, " i:", iii, " o:", ooo, " u:", uuu,)


# Задание №3


a = int(input("Cколько денег у Майкла? : "))
b = int(input("Сколько денег у Ивана? : "))
x = int(input("Минимальна сумма инвестиции : "))

if a >= x and b >= x:
    print(2)
elif b >= x and a < x:
    print("Ivan")
elif a >= x and b < x:
    print("Mike")
elif a + b >= x:
    print(1)
elif a + b < x:
    print(0)





