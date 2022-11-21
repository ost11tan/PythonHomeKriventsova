import list_to_stroka
def print_all_to_console(file_name):
    file = open(file_name, "r", encoding='utf-8')
    lst = file.read().split('\n')
    print(lst)
    stroka=list_to_stroka.lst_to_str(lst)
    return stroka