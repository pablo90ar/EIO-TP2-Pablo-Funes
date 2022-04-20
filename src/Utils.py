# Módulo UTILS:
# Este módulo almacena funciones utilizadas para validar información y ejecutar flujos de navegación
# La información a validar proviene del ingreso por teclado del usuario.

# Esta función consulta al usuario si está seguro de la acción que seleccionó y devuelve un booleano
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


# Esta función solicita el ingreso de un número entero y \
# corrobora que se encuentre dentro de un rango válido parametrizado
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
