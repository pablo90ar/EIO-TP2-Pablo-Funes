import Printer
import Utils
import Loader
import Resolver

# Módulo APP
# Este es el archivo raíz del proyecto, y es el que debe ejecutarse para correr el programa

menu_option = 0
# Mientras no se seleccione la opción 1 ni la opción 2...
while menu_option < 2:
    # Imprime el menú principal en pantalla y espera la elección del usuario
    menu_option = Printer.print_main_menu()
    # Si la opción elegida es la 1...
    if menu_option is 1:
        # Borra la pantalla
        Printer.clear_console()
        # Se lee el número de ejercicio que se desea cargar
        print("Resolver un ejercicio de la práctica.\n")
        exercise_num = Utils.check_int_input_range("Ingrese el número de ejercicio que desea resolver ", 1, 9)
        # Se carga el ejercicio para ser presentado
        printable_ex = Loader.load_known_exercise(exercise_num)
        # Se muestra el ejercicio elegido en pantalla
        Printer.print_exercise(printable_ex)
        # Carga valores del ejercicio para calcular
        ex = Loader.load_known_exercise(exercise_num)
        # Resuelve el ejercicio y presenta los resultados
        Resolver.resolve(ex)
    # Si la opción elegida es la 2...
    elif menu_option is 2:
        # Solicita confirmar la acción
        confirm_exit = Utils.confirm_action("salir")
        # Si cancela la opcion...
        if not confirm_exit:
            # Vuelve al menú principal
            menu_option = 0
# Si confirma la acción de salir, el programa abandona el "while loop" y finaliza saludando al usuario
Printer.say_goodbay()
