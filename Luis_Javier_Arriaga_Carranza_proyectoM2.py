import lenght_pharse, Point # import the two scripts to use

if __name__ == "__main__":
    execute = True # execute is for determinate the bucle
    tries = 0 # counter try if tries is major to two then finish the program
    while execute == True: # if execute is True then execute the next block code
        option = input("Elige que programa deseas ejecutar.\n1.Lenght_pharse.\n2.Location_point.\n3.Salir\n") # storage input in option
        if option == "3": # if option is equal to 3 then finish the program
            execute = False
            break
        if option != "1" or option != "2": # if opton is different of 1 or 2 then show a respect message in the screen
            tries += 1 # add one to count tries
            print("_____________________________\n")
            print("Elige una de las 2 opciones. Digita el numero que deseas ejecutar.\nEjemplo: 1")
        if tries > 2: # if tries is major to two then finish the program
            print("_____________________________\n")
            print("Intentalo de nuevo más tarde.")
            execute = False
        else: # else show the count in tries on the screen
            print("_____________________________\n")
            print(f"Te quedan {3 - tries} intentos")
            print("_____________________________\n")
        if option == "1": # if option is equal to one then execute the program lenght_pharse
            tries = 0 # tries change again to 0
            print("_____________________________\n")
            lenght_pharse_count = False # lenght_pharse_count is for determinate if the block code into the while have be execute
            while lenght_pharse_count == False: # while lenght_pharse_count is equal to False execute the next block code
                res = input("Ingresa una palabra que contenga entre 4 y 8 palabras.\n") # input
                lenght_pharse_count = lenght_pharse.lenght_pharse(res) # execute the function on lenght_pharse recall lenght_pharse, pass the params res and storage the answer in lenght_pharse_count
                print("_____________________________\n")
        if option == "2": #if option is equal to two then execute the program Point
            tries = 0 # tries change again to 0
            location_point_count = False # location_point_count is for determinate if the block code into the while have be execute
            while location_point_count == False: # while location_point_count is equal to False execute the next block code
                print("_____________________________\n")
                request = input("Ingresa las coordenadas donde deseas ingresar el punto en el plano, separalas por una coma.Y te dire en que cuadrante te encuentras.\nEjemplo: 8,10\n") # input
                location_point_count = Point.location_point(request)  # execute the function on Point recall location_point, pass the params request and storage the answer in location_point_count
print("Hasta pronto.")