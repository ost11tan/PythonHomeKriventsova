from datetime import datetime



def import_logger(data1):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{}         {} \n". format(time, data1))
        
def export_logger(data1):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{}         {}  \n". format(time, data1))
        
def change_logger(data1):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{}         {}  \n". format(time, data1))