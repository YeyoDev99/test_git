import random
import os

def password_generator(num_car):
    nums = [str(i) for i in range(0,10)]
    letters = ["a","b","c","d","f","g","h","i","j","k","r","s","o","p","q","x","y","z","w","o","p","q","m","n","l"]
    symbols = ["-","_","Ç","^","*","(","!"]
    cars = nums + letters + symbols
    password_list = []
    for i in range(1,num_car + 1):
        election = random.choice(cars)
        password_list.append(election)
    password = "".join(password_list)
    print(f'tu nueva contraseña es: {password}')
    with open("./user-passwords.txt", "a", encoding="UTF=8") as list_of_passwords:
        list_of_passwords.write("\n" + password)




def run():
    while True:
        try:
            num_car= int(input(menu))
            os.system('cls')
            if num_car > 15:
                print("solo puedes digitar un limite de caracteres igual o menor a 15")
                continue_message_error = input("si quieres seguir con el programa digita la letra -y-, escribe cualquier otra cosa para salir del programa: ").replace(" ","").lower()
                os.system('cls')            
                if continue_message_error != "y":
                    break

            else:    
                password_generator(num_car)
                continue_message = input("si quieres generar otra contraseña digita la letra -y-, escribe cualquier otra cosa para salir del programa: ").replace(" ","").lower()
                os.system('cls') 
                if continue_message != "y":
                    break
        except ValueError:
            os.system('cls')
            print("no puedes digitar caracteres que no sean numeros")
            continue_error = input("si quieres seguir con el programa digita la letra -y-, escribe cualquier otra cosa para salir del programa: ").replace(" ","").lower()
            os.system('cls') 
            if continue_error != "y":
                break




menu = """
Bienvenido a password generator

a continuacion podra generar una contraseña


escriba el numero de caracteres que desea tener en su contraseña,
este numero no puede ser mayor a 15: """



if __name__ == "__main__":
    run()