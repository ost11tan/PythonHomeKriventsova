import list_to_stroka_sy
def Edit_Entry(old_s,new):
    new_s=list_to_stroka_sy.lst_to_str(new)
    with open('employees.csv', encoding="utf-8") as f:
        s=f.read()
    with open('employees.csv', 'w', encoding="utf-8") as f:
        s=s.replace(old_s,new_s)
        f.write(s)
        
        
        
        