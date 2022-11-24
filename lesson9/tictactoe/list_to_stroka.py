
def lst_to_str(list,num):
    new_list=[]
    for i in list:
        new_list.append(i)
    
    lst=(sum(new_list, []))
    stroka=""
    if num==0:
        for i in range (0,3):
            stroka=stroka+lst[i]+" "
    if num==1:
        for i in range (3,6):
            stroka=stroka+lst[i]+" "
    if num==2:
        for i in range (6,9):
            stroka=stroka+lst[i]+" "
        
            
    return stroka
