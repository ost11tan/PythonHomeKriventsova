import list_to_stroka_sy
def Edit_Entry(file,old_s,new):
    new_s=list_to_stroka_sy.lst_to_str(new)
    with open(file) as f:
        s=f.read()
    with open(file, 'w') as f:
        s=s.replace(old_s,new_s)
        f.write(s)