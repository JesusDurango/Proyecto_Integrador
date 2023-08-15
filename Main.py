import readchar
import os
import msvcrt 
#msvcrt se utiliza en Windows para obtener una tecla presionada sin necesidad de presionar Enter

# Proyecto integrador V.1
print("Por favor introduce tu nombre: ")
nombre = input ()
print (f"Hola, bienvenido a una nueva partida {nombre}.")

# Proyecto integrador V.2

def main():
    print("Presiona la tecla que desees y solo presiona la tecla ↑ (UP) para terminar el programa.")
    while True:
        tecla_presionada = readchar.readkey()
        
        if tecla_presionada == readchar.key.UP:  
            break
        print(f"Tecla presionada: {tecla_presionada}")
    
if __name__ == "__main__":
    main()
        
#  Proyecto integrador V.3   

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
        
def contar_n():
    numero = 0
    
    while numero <= 50:
        print(f"Número actual: {numero}")
        print("Presiona 'n' para continuar o cualquier otra tecla para salir...")
        
        caracter = msvcrt.getch()
        
        if caracter == b'b':
            numero += 1
            clear_terminal()
        else:
            break

if __name__ == "__main__":
    contar_n()