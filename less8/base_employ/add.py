import list_to_stroka_sy

def newstring(contacts):
    print(type(contacts))
    with open("employees.csv", "a",encoding = 'utf-8') as file:
        strok=list_to_stroka_sy.lst_to_str(contacts)
        file.writelines ( strok+ "\n")
        return strok
    
    
    
    
    
    
    
