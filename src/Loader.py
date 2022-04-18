import json
import Printer
from Exercise import Exercise


# Carga ejercicio de la práctica para ser resuelto y lo devuelve al finalizar
def load_known_exercise(ex_num):
    # Se abre el archivo "Problems.json" que contiene los ejercicios de la práctica
    with open('./src/Problems.json', encoding="utf-8") as file:
        exercise = json.load(file)["data"][ex_num - 1]

    # Se crea un objeto tipo "Exercise" vacío y se lo llena con los valores del ejercicio elegido
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
    ex.cost = exercise["cost"]
    ex.offer = exercise["offer"]
    ex.demand = exercise["demand"]
    return ex
