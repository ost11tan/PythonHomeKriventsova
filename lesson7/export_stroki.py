
def ex_strok():
    global num_strok
    num_strok=int(input("Введите номер строки "))
    if num_strok<=0:
        num_strok=int(input("Введите номер строки больше 0 "))
        
    global table
    with open('telefone.csv', 'r') as file:
        table = [line.strip() for line in file]
    file.close()
    
    stroka=str(table[num_strok])
    #print(stroka) 
    
    lst=[]
    temp_element=""
    for i in range (len(stroka)):
        if stroka[i]!=";":
            temp_element=temp_element+stroka[i]
        elif stroka[i]==";":
            lst.append(temp_element)
            temp_element=""
    lst.append(temp_element)    

    #print(lst)
    return lst

#ex_strok()