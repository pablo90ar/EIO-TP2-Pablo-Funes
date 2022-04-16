import os

from Exercise import Exercise
from TableMerger import tabulate
from pprint import PrettyPrinter

pp = PrettyPrinter()


# Borra la pantalla de la consola
def clear_console():
    os.system('cls')


# Muestra mensaje de bienvenida
def print_welcome_msj():
    clear_console()
    print("Cátedra: Elementos de la Investigación Operativa")
    print("Alumno: Pablo Funes")
    print("Profesora: Ingeniera Melina Denardi")
    print("Trabajo Práctico Nº2: Resolución de problemas de transporte")
    print("Carrera: Tecnicatura universitaria en programación - UTN FRRaf")

    press_enter_to("ir al menú principal")


# Muestra el menú principal y retorna la opcion seleccionada
def print_main_menu():
    success = False
    menu_option = 0
    while not success:
        clear_console()
        print("MENU PRINCIPAL:\n")
        print("1- Resolver un ejercicio de la práctica.")
#        print("2- Resolver un ejercicio ingresado manualmente.")
        print("2- Salir del programa")
        selection = input("\nSeleccione una opción ")

        if selection.isnumeric() and selection.isdigit():
            menu_option = int(selection)
            if 0 < menu_option < 5:
                success = True
            else:
                input("Opción incorrecta")
        else:
            input("Ingrese un número del 1 al 4")
    return menu_option


# Solicita pulsar enter para continuar
def press_enter_to(action="continuar"):
    input("\nPresione enter para "+action+".")


# Imprime una tabla completa aceptando un objeto Exercise como parámetro
def print_full_dynamic_table(exercise: Exercise):
    # Inserta dest_type como título de destinos y casilleros en blanco
    header1 = [" ", exercise.dest_type]
    for item in range(len(exercise.dest_name)):
        header1.append(" ")
    # Inserta la segunda linea de la tabla orig_type | [dest_name] | offer_type
    header2 = [exercise.orig_type]
    header2.extend(exercise.dest_name)
    header2.append(exercise.offer_type)
    headers = [header1, header2]
    # Inserta las filas con datos (value)
    rows = exercise.cost
    # Inserta la columna con los nombres de origen y la columna de oferta
    for row in range(len(rows)):
        if exercise.orig_name[row]:
            rows[row].insert(0, exercise.orig_name[row])
        else:
            rows[row].insert(0, "Origen " + str(row+1))
        rows[row].append(exercise.offer[row])
    # Inserta la fila de valores de demanda con su titulo en la tabla
    demand_row = [exercise.demand_type]
    demand_row.extend(exercise.demand)
    demand_row.append(" ")
    rows.append(demand_row)
    # Imprime la tabla
    colspan = {(0, 1): len(exercise.dest_name)}
    rowspan = {}
    tabulate(headers + rows, colspan, rowspan)


# Imprime una tabla genérica para graficar la ubicación de cada variable a cargar
def print_generic_table():
    print("+-------------------------------------------------------------------+------------+")
    print("|           |             dest_type                                 |            |")
    print("+-------------------------------------------------------------------+------------+")
    print("|origin_type| dest_name 0   dest_name 1   dest_name 2   dest_name n | offer_type |")
    print("|-------------------------------------------------------------------|------------+")
    print("|orig_name0 |    v 00          v 01          v 02          v 0n     |   offer 0  |")
    print("|orig_name1 |    v 10          v 11          v 12          v 1n     |   offer 1  |")
    print("|orig_name2 |    v 20          v 21          v 22          v 2n     |   offer 2  |")
    print("|orig_name3 |    v n0          v n1          v n2          v nn     |   offer n  |")
    print("+-------------------------------------------------------------------+------------+")
    print("|demand_type|   demand 0      demand 1      demand 2      demand 3  |            |")
    print("+-------------------------------------------------------------------+------------+")


def print_excercise(ex: Exercise):
    clear_console()
    pp.pprint(ex.pre_prompt)
    print_full_dynamic_table(ex)
    pp.pprint(ex.post_prompt)
    press_enter_to("iniciar la resolución")


# Muestra mensaje de despedida
def say_goodbay():
    input("\n¡Hasta luego!")
