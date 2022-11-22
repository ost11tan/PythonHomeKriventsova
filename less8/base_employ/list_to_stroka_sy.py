def lst_to_str(list):
    stroka=""
    for i in range (len(list)):
        if i==len(list)-1:
            stroka=stroka+list[i]+"\n"
        else:
            stroka=stroka+list[i]+";"
        
    return stroka
    
