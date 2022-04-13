def confirm_action(action: str = None):
    response = ""
    while response is "":
        if action:
            print("¿Confirma que desea " + action + "?")
        else:
            print("¿Confirma la acción?")
        response = input("\n[s]í / [n]o ")
        if (response is "s") or (response is "S"):
            return True
        elif (response is "n") or (response is "N"):
            return False
        else:
            print("Respuesta incorrecta.\nIngrese [s]í o [n]o para aceptar o cancelar.")
            response = ""
