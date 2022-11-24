def WinO(mass):
    if mass[0][0]== "🔘" and mass[1][1]== "🔘" and mass[2][2]== "🔘" \
    or mass[2][0]== "🔘" and mass[1][1]== "🔘" and mass[0][2]== "🔘" \
    or mass[0][0]== "🔘" and mass[0][1]== "🔘" and mass[0][2]== "🔘" \
    or mass[1][0]== "🔘" and mass[1][1]== "🔘" and mass[1][2]== "🔘"\
    or mass[2][0]== "🔘" and mass[2][1]== "🔘" and mass[2][2]== "🔘"\
    or mass[0][0]== "🔘" and mass[1][0]== "🔘" and mass[2][0]== "🔘"\
    or mass[0][1]== "🔘" and mass[1][1]== "🔘" and mass[2][1]== "🔘"\
    or mass[0][2]== "🔘" and mass[1][2]== "🔘" and mass[2][2]== "🔘":
        print("Выиграл 🔘!")
        exit()
         
      
    
        
    

def WinX(mass): 
    if mass[0][0]== "☑️" and mass[1][1]== "☑️" and mass[2][2]== "☑️"\
    or mass[2][0]== "☑️" and mass[1][1]== "☑️" and mass[0][2]== "☑️"\
    or mass[0][0]== "☑️" and mass[0][1]== "☑️" and mass[0][2]== "☑️"\
    or mass[1][0]== "☑️" and mass[1][1]== "☑️" and mass[1][2]== "☑️"\
    or mass[2][0]== "☑️" and mass[2][1]== "☑️" and mass[2][2]== "☑️"\
    or mass[0][0]== "☑️" and mass[1][0]== "☑️" and mass[2][0]== "☑️"\
    or mass[0][1]== "☑️" and mass[1][1]== "☑️" and mass[2][1]== "☑️"\
    or mass[0][2]== "☑️" and mass[1][2]== "☑️" and mass[2][2]== "☑️":
        print("Выиграл ☑️!")
        exit()
        


