import json
import pprint
from copy import deepcopy

import Printer
from Exercise import Exercise


# Módulo LOADER
# Este módulo contiene funciones orientadas a leer archivos para colocar información en variables
# Esto le permite al programa manipular dicha información y realizar cálculos


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


# Carga un ejercicio personalizado con todos los valores a pedido del cliente y lo devuelve al finalizar
def load_custom_exercise():
    Printer.print_generic_table()
    # Se crea un objeto tipo "Exercise" vacío y se lo llena con los valores del ejercicio elegido
    ex = Exercise()
    ex.orig_type = input("Paso 1/11 - Ingrese el tipo de origen. Valor por defecto: [Orígenes] ") or "Orígenes"
    ex.dest_type = input("Paso 2/11 - Ingrese el tipo de destino. Valor por defecto: [Destinos] ") or "Destinos"
    ex.offer_type = input("Paso 3/11 - Ingrese el tipo de oferta. Valor por defecto: [Oferta] ") or "Oferta"
    ex.demand_type = input("Paso 4/11 - Ingrese el tipo de demanda. Valor por defecto: [Demanda] ") or "Demanda"
    orig_number = int(
        input("Paso 5/11 - Ingrese la cantidad de orígenes (filas) de la tabla. Valor por defecto: [3] ") or 3)
    dest_number = int(
        input("Paso 6/11 - Ingrese la cantidad de destinos (columnas) de la tabla. Valor por defecto: [4] ") or 4)
    for i in range(orig_number):
        num = str(i + 1)
        ex.orig_name.append(input("Paso 7/11 - Dato " + str(num) + "/" + str(orig_number)
                                  + " - Ingrese el nombre del origen N°" + num
                                  + ". Valor por defecto: [Origen-" + num + "] ") or "Origen-" + num)
    for j in range(dest_number):
        num = str(j + 1)
        ex.dest_name.append(input("Paso 8/11 - Dato " + str(num) + "/" + str(dest_number)
                                  + " - Ingrese el nombre del destino N°" + num
                                  + ". Valor por defecto: [Destino-" + num + "] ") or "Destino-" + num)
    for i in range(orig_number):
        num = str(i + 1)
        ex.offer.append(int(input("Paso 9/11 - Dato " + str(num) + "/" + str(orig_number)
                                  + " - Ingrese la cantidad total ofrecida para el origen " +
                                  ex.orig_name[i] + ". Valor por defecto [0] ") or 0))
    for j in range(dest_number):
        num = str(j + 1)
        ex.demand.append(int(input("Paso 10/11 - Dato " + str(num) + "/" + str(dest_number)
                                   + " - Ingrese la cantidad total demandada desde el destino " +
                                   ex.dest_name[j] + ". Valor por defecto [0] ") or 0))
    for i in range(orig_number):
        ex.cost.append([])
        for j in range(dest_number):
            ex.cost[i].append(int(input("Paso 11/11 - Dato " + str(i * dest_number + j + 1)
                                        + "/" + str(orig_number * dest_number)
                                        + " Ingrese el costo de traslado desde " + ex.orig_name[i] + " hasta " +
                                        ex.dest_name[j] + ". Valor por defecto [0] ") or 0))
    return ex
