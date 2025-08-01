# Lenght_pharse.py is a program that help to identify if user to input has exact number of characters 
def lenght_pharse(res): # this function return True or False.
    dict_alerts = dict(minor = "Hacen falta letras. Solo tiene {number_char} letras", major = "Sobran letras.Hay {number_char} caracteres", success = "Longitud correcta, contiene entre 4 a 8 letras.", number_find= "Porfavor ingresa solo letras, no se aceptan numeros.") # dict with message of alert
    min = 4 # number of char minor 
    max = 8 # number of char major
    number_char = len(res.replace(" ","")) # whit method replace(), replace the char " " this is to verify only the word into string, before count the char whit the function len and storage the result in number_char

    content_number = False # content_number is a bool for determinate if the string content number
    list_number = "" # list_number storage the number find in the original string
    for number in res: # iterate res
            if number.isdigit(): # verify if number iterate is digit
                    content_number = True # change the value of content_number
                    list_number = list_number + "," + number # add to string list_number the number find
    list_number = list_number.lstrip(",") # delete the first char "," into string list_number
    if content_number: # if content is true show the respect message alert
        print("_____________________________\n")
        print(dict_alerts.get("number_find") + list_number)        
        return False
    else:
        if number_char > 8: # if number_char is major to 8 char show the respect message alert
                print("_____________________________\n")
                print(dict_alerts.get("major").format(number_char=number_char)) # format() pass number_char to content in dict_alerts
                return False
        elif number_char < 4: # if number_char is minor to 4 char show the respect message alert
                print("_____________________________\n")
                print(dict_alerts.get("minor").format(number_char=number_char))
                return False
        else:# else show the respect message alert
                print("_____________________________\n")
                print(dict_alerts.get("success").format(number_char=number_char))
                return True