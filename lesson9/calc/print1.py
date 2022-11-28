import list_to_stroka
def print_all_to_console():
    file = open('log.csv', "r", encoding='utf-8')
    lst = file.read().split('\n')
    print(lst)
    stroka=list_to_stroka.lst_to_str(lst)
    return stroka