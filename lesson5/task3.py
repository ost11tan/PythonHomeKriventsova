#3. Создайте программу для игры в "Крестики-нолики"


def  PRINT(mass) :
    for row in mass:
        for elem in row:
            print(elem, end=' ')
        print()
               
a = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
PRINT(a)
    
def  imputForX(mass) :
    row=int(input("\n X! Введите номер строки "))
    row=row-1
    elem=int(input("\nX! Введите номер стoлбца "))
    elem=elem-1
    if row>2 or elem>2:
        print("Вы вышли за пределы поля,попробуйте еще раз")
        imputForX(mass)   
    elif mass[row][elem]=="*":
        mass[row][elem] = "X"   
    else:
        print("Этот элемент уже занят игроком " + str (mass[row][elem])+" введите координаты другого свободного места")
        imputForX(mass) 
    
def  imputForO(mass) :
    row=int(input("\n O! Введите номер строки "))
    row=row-1
    elem=int(input("\nO! Введите номер стoлбца "))
    elem=elem-1
    if row>2 or elem>2:
        print("Вы вышли за пределы поля,попробуйте еще раз")
        imputForO(mass)    
    elif mass[row][elem]=="*":
        mass[row][elem] = "O"
    else:
        print("Этот элемент уже занят игроком " + str (mass[row][elem])+" введите координаты другого свободного места")
        imputForO(mass) 
 


 
def WinO(mass):
    if mass[0][0]== "O" and mass[1][1]== "O" and mass[2][2]== "O" \
    or mass[2][0]== "O" and mass[1][1]== "O" and mass[0][2]== "O" \
    or mass[0][0]== "O" and mass[0][1]== "O" and mass[0][2]== "O" \
    or mass[1][0]== "O" and mass[1][1]== "O" and mass[1][2]== "O"\
    or mass[2][0]== "O" and mass[2][1]== "O" and mass[2][2]== "O"\
    or mass[0][0]== "O" and mass[1][0]== "O" and mass[2][0]== "O"\
    or mass[0][1]== "O" and mass[1][1]== "O" and mass[2][1]== "O"\
    or mass[0][2]== "O" and mass[1][2]== "O" and mass[2][2]== "O":
        print("Выиграл O!")
        exit()
         
      
    
        
    

def WinX(mass): 
    if mass[0][0]== "X" and mass[1][1]== "X" and mass[2][2]== "X"\
    or mass[2][0]== "X" and mass[1][1]== "X" and mass[0][2]== "X"\
    or mass[0][0]== "X" and mass[0][1]== "X" and mass[0][2]== "X"\
    or mass[1][0]== "X" and mass[1][1]== "X" and mass[1][2]== "X"\
    or mass[2][0]== "X" and mass[2][1]== "X" and mass[2][2]== "X"\
    or mass[0][0]== "X" and mass[1][0]== "X" and mass[2][0]== "X"\
    or mass[0][1]== "X" and mass[1][1]== "X" and mass[2][1]== "X"\
    or mass[0][2]== "X" and mass[1][2]== "X" and mass[2][2]== "X":
        print("Выиграл X!")
        exit()
        


        
    
        
        

count=0
for count in range (9):
    count=count+1
    if count%2==0:
        imputForO(a)
        PRINT(a)
        WinO(a)
            
    else:
        imputForX(a)
        PRINT(a)
        WinX(a)
            
    if count==9:
        print("Конец игры")
    



