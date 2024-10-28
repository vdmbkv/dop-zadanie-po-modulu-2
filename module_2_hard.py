# Основные операторы

stone_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("┃────────────────────────────────────────────────────────────────────────────────────────────────────────────────┃")
print(f'Необходимо найти пароль к каждому числу из списка на камне: {stone_1}')
print("""┃────────────────────────────────────────────────────────────────────────────────────────────────────────────────┃
Помните, что программа не любит выходы за пределы списка и повторение уже введенных чисел!
┃────────────────────────────────────────────────────────────────────────────────────────────────────────────────┃""")

def stones(x):
    stone_2 = []
    for i in range(1, x + 1):
        for w in range(i + 1, x + 1):
                sum_ = i + w
                if x % sum_ == 0:
                    stone_2.append(i)
                    stone_2.append(w)
    return stone_2

rep_num = set()

while True:
    x = int(input("Введите число с камня: "))
    if 3 <= x <= 20 and x not in rep_num:
        rep_num.add(x)
        stone_2 = stones(x)
        print("Пароль:", *stone_2)
        continue
    else:
        print("Введенное вами число не является элементом списка или уже было использовано. Увы, вы мертвы.")
        break



