import import_stroki 
import export_stroki
import changes_stroki
import list_to_stroka
import logger

indicator = int(input("Выберите действие \n1-Добавить строку в справочник\n2-Выбрать строку для дальнейшей работы\n3-Изменить значение \n"))
if indicator==1:
    import_stroki.im_strok()
    logger.import_logger(indicator)
elif indicator==2:
    export_stroki.ex_strok()
    logger.export_logger(indicator)
elif indicator==3:
    changes_stroki.ch_strok()
    logger.change_logger(indicator)