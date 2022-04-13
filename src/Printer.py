import os


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

    press_to_continue()


# Muestra el menú principal y retorna la opcion seleccionada
def print_main_menu():
    success = False
    menu_option = 0
    while not success:
        clear_console()
        print("MENU PRINCIPAL:\n")
        print("1- Resolver un ejercicio de la práctica.")
        print("2- Resolver un ejercicio ingresado manualmente.")
        print("3- Resolver un ejercicio con valores aleatorios.")
        print("4- Salir del programa")
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
def press_to_continue():
    print("\nPresione enter para continuar.")


# Muestra mensaje de despedida
def say_goodbay():
    input("\n¡Hasta luego!")
