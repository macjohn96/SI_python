from colorama import Fore, Back, Style, init
init()
# Fore.GREEN -> Color de la letra verde 
# Style.DIM -> El texto un poco mas tenue
# Back.RED -> Color fondo rojo
# Style.RESET_ALL -> Resetea los estilos
print(Fore.GREEN + 'OK: no errors') # Color de la letra verde 
print(Fore.YELLOW + 'Warning') # Color de la letra amarillo
print(Style.RESET_ALL + Style.DIM + Back.RED + 'Error' + Style.RESET_ALL) # Texto con fondo rolo, letra color blanco(normal) y letra mas tenue
print('back to normal now') #Texto sin estilo (normal)