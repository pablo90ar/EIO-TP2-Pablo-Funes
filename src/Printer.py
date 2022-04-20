import os
from Exercise import Exercise
from TableMerger import tabulate
from pprint import PrettyPrinter

# Módulo PRINTER:
# Este módulo almacena funciones utilizadas para mostrar información en consola
# La información puede ser menús, diálogos, la tabla de un problema, etc.


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


# Muestra el menú principal y retorna la opción seleccionada
def print_main_menu():
    success = False
    menu_option = 0
    # Mientras no haya una selección exitosa...
    while not success:
        # Limpia consola, muestra el menú, y solicita ingresar opción
        clear_console()
        print("MENU PRINCIPAL:\n")
        print("1- Resolver un ejercicio de la práctica.")
        print("2- Salir del programa")
        selection = input('\nSeleccione una opción y presione "Enter" ')
        # Comprueba si el dato ingresado es un número...
        if selection.isnumeric() and selection.isdigit():
            menu_option = int(selection)
            # Si el número ingresado es "1" o "2"...
            if 0 < menu_option < 3:
                # La opción elegida es válida
                success = True
            else:
                # Si el número está fuera del rango permitido, informa al usuario
                input("Opción incorrecta")
        else:
            # Si el dato ingresado no es un número, informa al usuario
            input("Ingrese un número del 1 al 4")
    # Cuando el usuario ingresa una opción válida, retorna la misma
    return menu_option


# Solicita pulsar "Enter" para continuar con el siguiente paso
def press_enter_to(action="continuar"):
    input("\nPresione enter para " + action + ".")


# Imprime una tabla completa aceptando un objeto Exercise como parámetro
def print_full_dynamic_table(exercise: Exercise):
    # Inserta dest_type como título de destinos
    header1 = [" ", exercise.dest_type]
    for item in range(len(exercise.dest_name)):
        header1.append(" ")
    # Inserta la segunda linea de la tabla [orig_type | [dest_name] | offer_type]
    header2 = [exercise.orig_type]
    header2.extend(exercise.dest_name)
    header2.append(exercise.offer_type)
    headers = [header1, header2]
    # Inserta las filas con datos (cost)
    rows = exercise.cost
    # Inserta la columna con los nombres de origen(si existen) y la columna de oferta
    for row in range(len(rows)):
        if exercise.orig_name[row]:
            rows[row].insert(0, exercise.orig_name[row])
        else:
            rows[row].insert(0, "Origen " + str(row + 1))
        rows[row].append(exercise.offer[row])
    # Inserta la fila de valores de demanda con su título en la tabla
    demand_row = [exercise.demand_type]
    demand_row.extend(exercise.demand)
    demand_row.append(" ")
    rows.append(demand_row)
    # Imprime la tabla
    col_span = {(0, 1): len(exercise.dest_name)}
    row_span = {}
    tabulate(headers + rows, col_span, row_span)


# Imprime el ejercicio cargado, incluyendo el texto de la consigna y su tabla de datos
def print_exercise(ex: Exercise):
    pp = PrettyPrinter()
    clear_console()
    pp.pprint(ex.pre_prompt)
    print_full_dynamic_table(ex)
    pp.pprint(ex.post_prompt)
    press_enter_to("iniciar la resolución")


# Muestra mensaje de despedida
def say_goodbay():
    input("\n¡Hasta luego!")
