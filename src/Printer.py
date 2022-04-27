import os
from copy import deepcopy
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
    print("Trabajo Práctico Nº2: Resolución de problemas de transporte\n")
    print("Cátedra: Elementos de la Investigación Operativa")
    print("Alumno: Pablo Funes")
    print("Profesora: Ingeniera Melina Denardi")
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
        print_truck()
        print("------------- MENU PRINCIPAL -------------\n")
        print("1- Resolver un ejercicio de la práctica (Ejercicios del 1 al 9)")
        print("2- Resolver un ejercicio ingresando los datos manualmente")
        print("3- Salir del programa")
        selection = input('\nSeleccione una opción y presione "Enter" ')
        # Comprueba si el dato ingresado es un número...
        if selection.isnumeric() and selection.isdigit():
            menu_option = int(selection)
            # Si el número ingresado es "1" o "2"...
            if 0 < menu_option < 4:
                # La opción elegida es válida
                success = True
            else:
                # Si el número está fuera del rango permitido, informa al usuario
                input("Opción incorrecta. Ingrese un número del 1 al 3")
        else:
            # Si el dato ingresado no es un número, informa al usuario
            input("Opción incorrecta. Ingrese un número del 1 al 3")
    # Cuando el usuario ingresa una opción válida, retorna la misma
    return menu_option


# Solicita pulsar "Enter" para continuar con el siguiente paso
def press_enter_to(action="continuar"):
    input('\nPresione "Enter" para ' + action + ".")


# Imprime una tabla completa aceptando un objeto Exercise como parámetro
def print_dynamic_table(ex: Exercise):
    # Inserta dest_type como título de destinos
    ex = deepcopy(ex)
    header1 = [" ", ex.dest_type]
    for item in range(len(ex.dest_name)):
        header1.append(" ")
    # Inserta la segunda linea de la tabla [orig_type | [dest_name] | offer_type]
    header2 = [ex.orig_type]
    header2.extend(ex.dest_name)
    header2.append(ex.offer_type)
    headers = [header1, header2]
    # Inserta las filas con datos (cost)
    rows = ex.cost
    # Inserta la columna con los nombres de origen(si existen) y la columna de oferta
    for row in range(len(rows)):
        if ex.orig_name[row]:
            rows[row].insert(0, ex.orig_name[row])
        else:
            rows[row].insert(0, "Origen " + str(row + 1))
        rows[row].append(ex.offer[row])
    # Inserta la fila de valores de demanda con su título en la tabla
    demand_row = [ex.demand_type]
    demand_row.extend(ex.demand)
    demand_row.append(" ")
    rows.append(demand_row)
    # Imprime la tabla
    col_span = {(0, 1): len(ex.dest_name)}
    row_span = {}
    tabulate(headers + rows, col_span, row_span)


# Imprime una tabla con los nombres de referencia para la carga manual de datos
def print_generic_table():
    print("""\
+--------------+------------------------------------------------------------+-------------+
|              |                     Destinos                               |             |
+--------------+------------------------------------------------------------+-------------+
|   Orígenes   |  Destino-1      Destino-2      Destino-3      Destino-N    |   Oferta    |
+--------------+------------------------------------------------------------+-------------|
|   Origen-1   |  costo(1,1)     costo(1,2)     costo(1,3)     costo(1,n)   |  Oferta-1   |
|   Origen-2   |  costo(2,1)     costo(2,2)     costo(2,3)     costo(2,n)   |  Oferta-2   |
|   Origen-3   |  costo(3,1)     costo(3,2)     costo(3,3)     costo(3,n)   |  Oferta-3   |
|   Origen-n   |  costo(n,1)     costo(n,2)     costo(n,3)     costo(n,n)   |  Oferta-n   |
+--------------+------------------------------------------------------------+-------------+
|   Demanda    |  Demanda-1      Demanda-2      Demanda-3      Demanda-n    |             |
+--------------+------------------------------------------------------------+-------------+\

""")


# Imprime el ejercicio cargado, incluyendo el texto de la consigna y su tabla de datos
def print_exercise(ex: Exercise):
    pp = PrettyPrinter()
    clear_console()
    print_exercise_title(ex.number)
    pp.pprint(ex.pre_prompt)
    print_dynamic_table(ex)
    pp.pprint(ex.post_prompt)


# Imprime el número del ejercicio
def print_exercise_title(ex_num: int):
    if ex_num != 0:
        print("------------------------------ Ejercicio Nº", ex_num, "------------------------------")
    else:
        print("------------------------------ Ejercicio Personalizado ------------------------------")


# Imprime un camión
def print_truck():
    print("""     
              ___________________
         ___  |  OPTIMIZACIÓN   |
        /_| | |  DE TRANSPORTE  |
       |    |_|_________________|
       "-O----O-O' `      `O`O'-'\

""")


# Muestra mensaje de despedida
def say_goodbay():
    input("\n¡Hasta luego!")

