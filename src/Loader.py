import json
import Printer
from Exercise import Exercise


# Carga ejercicio de la práctica para ser resuelto
def load_known_exercise(ex_num):
    # Se abre el archivo .json que contiene los ejercicios de la práctica
    with open('./src/Problems.json', encoding="utf-8") as file:
        exercise = json.load(file)["data"][ex_num - 1]

    # Se crea un objeto "Exercise" y se lo llena con los valores del ejercicio elegido
    ex = Exercise()
    ex.number = exercise["number"]
    ex.pre_prompt = exercise["pre_prompt"]
    ex.post_prompt = exercise["post_prompt"]
    ex.orig_type = exercise["orig_type"]
    ex.orig_name = exercise["orig_name"]
    ex.dest_type = exercise["dest_type"]
    ex.dest_name = exercise["dest_name"]
    ex.offer_type = exercise["offer_type"]
    ex.demand_type = exercise["demand_type"]
    ex.cost = exercise["transport_cost"]
    ex.offer = exercise["offer"]
    ex.demand = exercise["demand"]
    return ex


# TODO:
def load_manual_exercise():
    Printer.clear_console()
    Printer.print_generic_table()
    row_count = input("Ingrese la cantidad de filas (-) (sin contar la columna de las cantidades demandadas)")
    column_count = input("Ingrese la cantidad de columnas (|) sin contar la columna de las cantidades ofrecidas")


