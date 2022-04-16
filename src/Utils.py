

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
            print("Respuesta incorrecta.\nIngrese [s]í o [n]o para aceptar o cancelar la accion " + action + ".")
            response = ""


def check_int_input_range(var_name: str, min_value: int, max_value: int):
    msj = var_name + " entre " + str(min_value) + " y " + str(max_value) + ". "
    check_ok = False
    int_value = None
    while not check_ok:
        int_value = input(msj)
        if int_value.isdigit() and min_value <= int(int_value) <= max_value:
            check_ok = True
        else:
            print("Ingreso incorrecto.")
    return int(int_value)


def check_int_input(var_name: str, min_value: int = None, max_value: int = None):
    check_min_ok = False
    check_max_ok = False
    check_ok = False
    int_value = None
    while not check_ok:
        msj = var_name
        if min_value or min_value is 0:
            msj += " mayor a " + str(min_value)
        if (min_value or min_value is 0) and (max_value or max_value is 0):
            msj += " y"
        if max_value or max_value is 0:
            msj += " menor a " + str(max_value)
        msj += " "
        int_value = input(msj)
        if int_value.isdigit():
            int_value = int(int_value)
            if min_value:
                if min_value < int_value:
                    check_min_ok = True
                else:
                    check_min_ok = False
                    print("Ingreso incorrecto.")
            else:
                check_min_ok = True
            if max_value:
                if max_value > int_value:
                    check_max_ok = True
                else:
                    check_max_ok = False
                    print("Ingreso incorrecto.")
            else:
                check_max_ok = True
        else:
            print("Ingreso incorrecto.")
        if check_min_ok and check_max_ok:
            check_ok = True
    return int_value
