import export_stroki as ex
import list_to_stroka as to_stroka
     

def ch_strok():
    lst=ex.ex_strok()
    print(lst)

    num_elem=int(input("Введите цифру,соответствующую столбцу\n0-Имя\n1-Фамилия\n2-Телефон\n3-Комментарий  \n"))

    elem=lst[num_elem]
    #print(ex.num_strok)
    
    elem=input("Введите значение, на которoе вы хотите заменить "+ str(elem)+"  " )
    lst[num_elem]=elem
    
    new_str=to_stroka.lst_to_str(lst)
    old_str=ex.table[ex.num_strok]
    
    
    
    with open("telefone.csv") as f:
        s=f.read()
    with open("telefone.csv", 'w') as f:
        s=s.replace(old_str,new_str)
        f.write(s)
    


#ch_strok()