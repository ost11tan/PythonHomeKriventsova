#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input("Для ввода значения False просто нажмите Enter \n Для ввода значения True введите любую букву или цифру \nВведите X "))
y = bool(input("Введите Y "))
z = bool(input("Введите Z "))

print (not(x or y or z)) #проверка левой части выражения
print (not x and not y and not z) #проверка правой части выражения
print ((not(x or y or z))==(not x and not y and not z))