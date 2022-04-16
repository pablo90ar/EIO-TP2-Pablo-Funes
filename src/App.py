import Printer
import Utils
import Loader
import Resolver


Printer.print_welcome_msj()
menu_option = 0
while menu_option < 2:
    menu_option = Printer.print_main_menu()
    if menu_option is 1:
        # Carga ejercicio de la práctica
        Printer.clear_console()
        # Se lee el numero de ejercicio que se desea cargar
        print("1- Resolver un ejercicio de la práctica.\n")
        exercise_num = Utils.check_int_input_range("Ingrese el número de ejercicio", 1, 9)
        printable_ex = Loader.load_known_exercise(exercise_num)
        # Lo muestra en pantalla
        Printer.print_excercise(printable_ex)
        # Carga valores del ejercicio para calcular
        ex = Loader.load_known_exercise(exercise_num)
        # Resuelve el ejercicio
        Resolver.resolve(ex)
    elif menu_option is 2:
        confirm_exit = Utils.confirm_action("salir")
        if not confirm_exit:
            menu_option = 0
Printer.say_goodbay()
