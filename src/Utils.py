import Printer
from Exercise import Exercise


# Módulo UTILS:
# Este módulo almacena funciones utilizadas para validar información y ejecutar flujos de navegación
# La información a validar proviene del ingreso por teclado del usuario.

# Esta función consulta al usuario si está seguro de la acción que seleccionó y devuelve un booleano
def confirm_action(action: str = None):
    response = ""
    while response == "":
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
# Corrobora que se encuentre dentro de un rango válido parametrizado
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


# comprueba si los datos de un ejercicio obedecen a una matriz rectangular
def check_data_completeness(ex: Exercise):
    rows = ex.get_row_num()
    row_len = []
    for row in range(rows):
        row_len.append(len(ex.cost[row]))
    if all(x == row_len[0] for x in row_len):
        return True
    else:
        print("Error: La tabla de costos de transporte está incompleta.")
        Printer.press_enter_to("volver al menu")
        return False


# Corrobora que la suma de las ofertas sea igual a la suma de las demandas
def check_data_balance(ex: Exercise):
    # Suma toda la oferta
    total_offer = 0
    for i in range(ex.get_row_num()):
        total_offer += ex.offer[i]
    # Suma toda la demanda
    total_demand = 0
    for i in range(ex.get_column_num()):
        total_demand += ex.demand[i]
    # Si la función no está balanceada...
    if not (total_offer == total_demand):
        # Muestra la cantidad total de oferta y la de demanda para evidenciar la falta de balanceo
        print("\nFunción NO balanceada.\nOferta total: " + str(total_offer) + "\nDemanda total: " + str(total_demand))
        # Ante la imposibilidad de calcular, vuelve al menú principal
        Printer.press_enter_to("volver al menú")
        return False
    # Si la función está balanceada...
    else:
        # Muestra la cantidad total de oferta/demanda
        print("\nFunción balanceada. Cantidad total: " + str(total_offer) + "\n")
        return True
