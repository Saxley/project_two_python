# Point.py is a script that calculate the location in one plane cartesian 
def location_point(request): # this function return true or False
    dict_location_plain = {"{x},{y}":"Te encuentras en el primer cuadrante","-{x},{y}":"Te encuentras en el segundo cuadrante","{x},-{y}":"Te encuentras en el tercer cuadrante","-{x},-{y}":"Te encuentras en el cuarto cuadrante", "aviso_cantidad":"Solo puedes ingresar 2 coordenadas x, y. Intentalo de nuevo.", "origen":"{variable} no se puede encontrar en el origen.Intentalo de nuevo."} # dictionary whit the possible answer for the user
    request = request.split(",") # split the string whit ,
    x = request[0] # select he coordenate x
    y = request[1] # select the coordenate y
    origen = False # origin is for identify if one coordenate has location in the origen into plane
    if int(x) == 0 : # if x is equal to 0, show in the screen the respect message ans change to value on origin, return origin
            print("Tu coordenada x=" + dict_location_plain.get("origen").format(variable = x))
            origen = True
            return origen
    if int(y) == 0 : # if y is equal to 0, show in the screen the respect message ans change to value on origin, return origin
            print("Tu coordenada x=" + dict_location_plain.get("origen").format(variable = y))
            origen=True
            return origen
    if len(request) > 2: # if request have more of two elements , show in the screen the respect message and return False
        print(dict_location_plain.get("aviso_cantidad"))
        return False
    elif origen != True: # if origen is different to 0 then execute the next block code
        key_value = "{x},{y}" # key_value is a string, conformed for coordenate x and y
        if int(x) < 0: # if coordenated x is minor to 0 then add one minus last coordenate x in the strting key_value
            key_value = "-{x},{y}"
        if int(y) < 0: # if coordenated y is minor to 0 then add one minus last coordenate y in the strting key_value
            key_value = "{x},-{y}"
        if int(y) < 0 and int(x) < 0: # if both coordenates be minor to 0 add one minor last x and y
            key_value = "-{x},-{y}"
        print("_________________________________\n")
        print(dict_location_plain.get(key_value).format(x=x , y=y)) # the method format, allow format the string into key in the dictionary
        print("_________________________________")
        return True # return True because all is success