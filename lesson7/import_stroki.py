def im_strok():
    with open('telefone.csv', 'a') as file:
        name = input("Введите имя ")
        surname = input("Введите фамилию ")
        tel_num = input("Введите номер телефона ")
        comment = input("Комментарий ")
        file.writelines ( str(name)+";"+str(surname)+";"+str(tel_num)+";"+str(comment)+"\n")
        
#im_strok()

