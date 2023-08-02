import readchar

# Proyecto integrador V.1
print("Por favor introduce tu nombre: ")
nombre = input ()
print (f"Hola, bienvenido a una nueva partida {nombre}.")

# Proyecto integrador V.2

def main():
    
    while True:
        tecla_presionada = readchar.readkey()
        print(f"Tecla presionada: {tecla_presionada}")
        if tecla_presionada == readchar.key.UP:  
            break
        
if __name__ == "__main__":
     print("Presiona la tecla que desees y solo presiona la tecla ↑ (UP) para terminar el programa.")
     main()
